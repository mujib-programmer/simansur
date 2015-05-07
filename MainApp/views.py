import  os

from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User, Group, Permission
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q

from MainApp.models import Surat, Disposisi, UserProfile, Aktivitas, TrackSurat, KotakSurat
from MainApp.forms import SuratForm, DisposisiForm, UserProfileForm, KirimSuratForm

DATA_PER_HALAMAN = 2 # untuk pagination

# untuk mengecek apakah user termasuk dalam kelompok groups yang diijinkan untuk mengakses methods pada view
# user akan langsung diarahkan ke form login jika tidak memiliki hak akses tanpa pesan apapun jika menggunakan method ini.
"""
def group_required(*group_names):
    #Requires user membership in at least one of the groups passed in
    def in_groups(u):
        if u.is_authenticated():
            if bool(u.groups.filter(name__in=group_names)) | u.is_superuser:
                return True
        return False
    return user_passes_test(in_groups, login_url='/login')
"""

def index(request):
    context_dict = {'slug': 'login', 'page_home_active':'active'}

    return render(request, 'MainApp/index.html', context_dict)

@login_required
def surat(request):
    # data untuk di tampilkan di template
    data = {}

    # user yang sedang login
    user_saat_ini = request.user

    # ambil data surat sesuai dengan yang login
    if user_dalam_group(user_saat_ini, 'manajer') | user_saat_ini.is_superuser:
        # manajer surat atau superadmin akan bisa mendapatkan semua data surat
        semua_surat = Surat.objects.all()

    else:
        # selain admin atau manajer hanya akan mendapatkan data surat yang ditujukan atau di dikirim olehnya
        try:
            # ambil semua surat yang terkait dengan user saja
            # user terkait yaitu, pengirim surat, penerima surat, dan penerima disposisi
            semua_surat = Surat.objects.filter(pencatat=user_saat_ini)

        except Surat.DoesNotExist:
            semua_surat = None


    data['semua_surat'] = semua_surat
    data['page_surat_active'] = 'active'


    return render(request, 'MainApp/surat/surat.html', data)

@login_required
def surat_detail(request, no_surat):

    # get data surat
    dataSurat = Surat.objects.get(no_surat=no_surat)

    try:
        # get disposisi surat
        semua_disposisi_surat = Disposisi.objects.filter(surat=dataSurat)

    except Disposisi.DoesNotExist:
         semua_disposisi_surat = None

    context_dict = {'surat': dataSurat, 'semua_disposisi_surat': semua_disposisi_surat, 'page_surat_active':'active'}

    return render(request, 'MainApp/surat/surat_detail.html', context_dict)

@login_required
def surat_delete(request, no_surat):
    data = {}

    user_saat_ini = request.user

    # Hanya user yang memiliki hak akses untuk menghapus surat diperbolehkan untuk menghapus label surat
    if user_saat_ini.has_perm('MainApp.delete_surat') == False :
        data['alert_type'] =  "danger"
        data['alert_message'] = "Anda tidak di ijinkan untuk menghapus label surat!"
        return render(request, "MainApp/index.html", data)

    try:
        # get data surat
        dataSurat = Surat.objects.get(no_surat=no_surat)

        # hanya surat yang belum dikirim atau didisposisi yang bisa dihapus
        if dataSurat.status != "dilabeli":
            data['alert_type'] =  "danger"
            data['alert_message'] = "Hanya surat yang belum dikirimkan atau didisposisikan yang bisa dihapus!"
            return render(request, "MainApp/index.html", data)

        dataSurat.delete()

    except Surat.DoesNotExist:
        # jika data surat yang diinginkan untuk dihapus tidak ditemukan, tampilkan daftar semua surat
        return surat(request)

    # get data surat
    semua_surat = Surat.objects.all()

    context_dict = {'semua_surat': semua_surat, 'page_surat_active':'active'}

    return render(request, 'MainApp/surat/surat.html', context_dict)

@login_required
#@group_required('admin', 'pencatat surat')
# tambah surat artinya melabeli surat baru, belum mengirimkannya.
def surat_tambah(request):
    data = {}

    # dapatkan data user yang sedang login
    user_saat_ini = request.user
    
    # Hanya user yang memiliki hak akses untuk menambah surat diperbolehkan untuk melabeli surat baru
    if user_saat_ini.has_perm('MainApp.add_surat') == False :
        data['alert_type'] =  "danger"
        data['alert_message'] = "Anda tidak di ijinkan untuk menambah label surat baru!"
        return render(request, "MainApp/index.html", data)

    # A HTTP POST?
    if request.method == 'POST':
        form = SuratForm(request.POST, request.FILES)

        # Have we been provided with a valid form?
        if form.is_valid():
            data_surat = form.save(commit=False)

            data_surat.pencatat = user_saat_ini
            data_surat.status = "dilabeli"
            form.save(commit=True)

            # kembali ke halaman daftar surat
            return HttpResponseRedirect('/surat/')
        else:
            # The supplied form contained errors - just print them to the terminal.
            print(form.errors)
    else:
        # If the request was not a POST, display the form to enter details.
        form = SuratForm()

    # Bad form (or form details), no form supplied...
    # Render the form with error messages (if any).
    return render(request, 'MainApp/surat/surat_tambah.html', {'form': form, 'page_surat_active':'active'})

@login_required
def surat_edit(request, no_surat):

    # get data surat
    dataSurat = Surat.objects.get(no_surat=no_surat)

    # A HTTP POST?
    if request.method == 'POST':
        form = SuratForm(request.POST, request.FILES, instance=dataSurat)

        # Have we been provided with a valid form?
        if form.is_valid():

            form.save(commit=True)

            # go to surat view
            return surat(request)

        else:
            # The supplied form contained errors - just print them to the terminal.
            print(form.errors)
    else:
        # If the request was not a POST, display the form to enter details.
        form = SuratForm(instance=dataSurat)

    # Bad form (or form details), no form supplied...
    # Render the form with error messages (if any).
    return render(request, 'MainApp/surat/surat_edit.html', {'form': form ,'no_surat': no_surat, 'page_surat_active':'active'})

@login_required
def surat_download(request, no_surat):

    try:

        # get data surat
        dataSurat = Surat.objects.get(no_surat=no_surat)
        file = dataSurat.file_surat
        nama_file = os.path.basename(file.url)

        response = HttpResponse(file, content_type='application/force-download')
        response['Content-Disposition'] = 'attachment; filename=%s' % nama_file

        #response['X-Sendfile'] = smart_str(file)

        return response

    except Surat.DoesNotExist:

        # jika data surat yang diinginkan untuk dihapus tidak ditemukan, tampilkan daftar semua surat
        return surat_detail(request, no_surat)

@login_required
def surat_kirim(request, no_surat):
    data = {}

    user_saat_ini = request.user

    # get data surat
    data_surat = Surat.objects.get(no_surat=no_surat)

    # A HTTP POST?
    if request.method == 'POST':
        form = KirimSuratForm(request.POST)

        # Have we been provided with a valid form?
        if form.is_valid():

            data_form = form.cleaned_data

            # tambahkan data kotak surat untuk user penerima
            kotak_surat = KotakSurat()
            kotak_surat.surat = data_surat
            kotak_surat.catatan_tambahan = data_form.get('catatan_tambahan')
            kotak_surat.penerima = data_form.get('penerima')
            kotak_surat.status = "diterima"
            kotak_surat.pengirim = user_saat_ini
            kotak_surat.jenis_pengiriman = "langsung"
            kotak_surat.save()

            # ubah status surat menjadi dikirim agar tidak bisa diubah maupun dihapus
            data_surat.status = "dikirim"
            data_surat.save()

            # tambahkan data track surat
            status_track_surat = "Surat no %s dikirimkan ke %s oleh %s." %(data_surat.no_surat, kotak_surat.penerima, kotak_surat.pengirim)
            catat_track_surat(data_surat, status_track_surat)

            # kembali ke halaman daftar surat
            return HttpResponseRedirect('/surat/')

        else:
            # The supplied form contained errors - just print them to the terminal.
            print(form.errors)
    else:
        # If the request was not a POST, display the form to enter details.
        form = KirimSuratForm()
        data['form'] = form


    data['surat'] = data_surat
    data['no_surat'] = no_surat
    data['page_surat_active'] ='active'

    return render(request, 'MainApp/surat/surat_kirim.html', data)

@login_required
def disposisi_tambah(request, no_surat):

    # dapatkan data user yang sedang login
    user_saat_ini = request.user
    user_profile_saat_ini = UserProfile.objects.get(user=user_saat_ini)

    # get data surat
    data_surat = Surat.objects.get(no_surat=no_surat)

    # A HTTP POST?
    if request.method == 'POST':
        form = DisposisiForm(request.POST, )

        # Have we been provided with a valid form?
        if form.is_valid():

            disposisi = form.save(commit=False)
            disposisi.surat = data_surat

            # catat pengirim disposisi dari user yang login saat ini
            disposisi.pengirim_disposisi = user_profile_saat_ini

            # tambahkan penerima disposisi sebagai user terkait surat
            data_surat.user_terkait.add(disposisi.penerima_disposisi)

            # ubah status surat
            status_surat = "Didisposisi ke %s." % disposisi.penerima_disposisi
            data_surat.status_surat = status_surat

            # ubah keterangan disposisi surat sesuai catatan tambahan disposisi saat ini
            data_surat.keterangan_disposisi = disposisi.catatan_tambahan

            # simpan surat
            data_surat.save()

            # tambahkan status surat di track surat
            catat_track_surat(data_surat, status_surat)

            # simpan data disposisi
            form.save(commit=True)

            # go to surat view
            return surat_detail(request, no_surat)

        else:
            # The supplied form contained errors - just print them to the terminal.
            print(form.errors)
    else:
        # If the request was not a POST, display the form to enter details.
        form = DisposisiForm()

    return render(request, 'MainApp/disposisi_tambah.html', {'form': form ,'no_surat': no_surat, 'page_surat_active':'active'})

@login_required
def disposisi_edit(request, id_disposisi):

    dataDisposisi = Disposisi.objects.get(id=id_disposisi)

    # A HTTP POST?
    if request.method == 'POST':
        form = DisposisiForm(request.POST, instance=dataDisposisi)

        # Have we been provided with a valid form?
        if form.is_valid():

            form.save(commit=True)

            # go to surat view
            return surat_detail(request, dataDisposisi.surat.no_surat)

        else:
            # The supplied form contained errors - just print them to the terminal.
            print(form.errors)
    else:
        # If the request was not a POST, display the form to enter details.
        form = DisposisiForm(instance=dataDisposisi)

    return render(request, 'MainApp/disposisi_edit.html', {'form': form ,'id_disposisi': id_disposisi, 'page_surat_active':'active'})

@login_required
def disposisi_delete(request, no_surat, id_disposisi):
    try:
        # get data surat
        dataDisposisi = Disposisi.objects.get(id=id_disposisi)

        dataDisposisi.delete()

    except Disposisi.DoesNotExist:
        # jika data surat yang diinginkan untuk dihapus tidak ditemukan, tampilkan daftar semua surat
        return surat(request)

    return surat_detail(request, no_surat)

    #return render(request, 'MainApp/surat.html', context_dict)

@login_required
def user(request):
    data = {}

    # hanya admin yang bisa melihat daftar user
    if is_admin(request.user) == False:
        data['alert_type'] =  "danger"
        data['alert_message'] = "Hanya administrator yang dijinkan untuk melihat daftar user!"
        return render(request, "MainApp/index.html", data)

    semua_user_profile = UserProfile.objects.all()

    paginator = Paginator(semua_user_profile, DATA_PER_HALAMAN)

    page = request.GET.get('page')
    try:
        user_profile = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        user_profile = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        user_profile = paginator.page(paginator.num_pages)

    jumlah_data_sebelumnya  = (user_profile.number - 1) * DATA_PER_HALAMAN
    data = {'semua_user_profile': user_profile, 'page_user_active':'active', 'jumlah_data_sebelumnya': jumlah_data_sebelumnya }

    return render(request, 'MainApp/user/user.html', data)

@login_required
def user_detail(request, username):
    data = {}

    # hanya admin yang bisa melihat detail user
    if is_admin(request.user) == False:
        data['alert_type'] =  "danger"
        data['alert_message'] = "Hanya administrator yang dijinkan untuk melihat detail user!"
        return render(request, "MainApp/index.html", data)

    try:
        # get data user
        user = User.objects.get(username=username)

        # get data userprofile
        user_profile = UserProfile.objects.get(user=user)


    except Disposisi.DoesNotExist:
         user_profile = None

    data = {'user_profile': user_profile, 'page_user_active':'active'}

    return render(request, 'MainApp/user/user_detail.html', data)

@login_required
def user_tambah(request):
    data = {}

    # hanya admin yang bisa menambah user
    if is_admin(request.user) == False:
        data['alert_type'] =  "danger"
        data['alert_message'] = "Hanya administrator yang dijinkan untuk menambah data user!"
        return render(request, "MainApp/index.html", data)

    # A HTTP POST?
    if request.method == 'POST':
        form = UserProfileForm(request.POST, )

        # Have we been provided with a valid form?
        if form.is_valid():
            data_form = form.cleaned_data

            try:
                User.objects.get(username=data_form.get('username'))
                # kembali ke halaman list user
                return user(request)

            except User.DoesNotExist:

                # membuat object user
                user_baru = User(username=data_form.get('username'), email=data_form.get('email'), password=data_form.get('username'))
                user_baru.set_password(data_form.get('password')) # atur ulang password sesuai input pengguna
                user_baru.first_name = data_form.get('first_name')
                user_baru.last_name = data_form.get('last_name')
                user_baru.is_active = data_form.get('is_active')
                user_baru.save()


                # tambahkan user ke group yang dipilih
                groups_terpilih = data_form.get('groups')
                for group in groups_terpilih:
                    user_baru.groups.add(group)

                 # jika user adalah admin, tandai user sebagai super admin di django
                if is_admin(user_baru):
                    user_baru.is_superuser = True
                    user_baru.is_staff = True
                else:
                    user_baru.is_superuser = False
                    user_baru.is_staff = False

                # simpan kembali data user
                user_baru.save()


                # membuat user profile baru
                user_profile_baru = UserProfile(user=user_baru)
                user_profile_baru.bidang = data_form.get('bidang')
                user_profile_baru.jabatan = data_form.get('jabatan')
                user_profile_baru.no_telepon = data_form.get('no_telepon')
                user_profile_baru.role_pencatat = False
                user_profile_baru.save()

                # kembali ke daftar user
                return HttpResponseRedirect('/user/')

        else:
            # The supplied form contained errors - just print them to the terminal.
            print(form.errors)
    else:
        # If the request was not a POST, display the form to enter details.
        form = UserProfileForm()

    return render(request, 'MainApp/user/user_tambah.html', {'form': form, 'page_user_active':'active'})

@login_required
def user_edit(request, username):
    data = {}

    # hanya admin yang bisa mengedit user
    if is_admin(request.user) == False:
        data['alert_type'] =  "danger"
        data['alert_message'] = "Hanya administrator yang dijinkan untuk mengubah data user!"
        return render(request, "MainApp/index.html", data)

    # A HTTP POST?
    if request.method == 'POST':
        form = UserProfileForm(request.POST)

        # Have we been provided with a valid form?
        if form.is_valid():
            data_form = form.cleaned_data

            # mendapatkan object user yang akan diubah
            data_user = User.objects.get(username=username)
            data_user.email = data_form.get('email')
            data_user.set_password(data_form.get('password'))
            data_user.first_name = data_form.get('first_name')
            data_user.last_name = data_form.get('last_name')
            data_user.is_active = data_form.get('is_active')
            data_user.save()

            # hapus semua group untuk user
            data_user.groups.clear()

            # tambahkan user ke group yang dipilih
            groups_terpilih = data_form.get('groups')
            for group in groups_terpilih:
                data_user.groups.add(group)

            # jika user adalah admin, tandai user sebagai super admin di django
            if is_admin(data_user):
                data_user.is_superuser = True
                data_user.is_staff = True
            else:
                data_user.is_superuser = False
                data_user.is_staff = False

            # simpan kembali data user
            data_user.save()

            # mendapatkan object user profile sesuai user yang dipilih
            data_user_profile = UserProfile.objects.get(user=data_user)
            data_user_profile.bidang = data_form.get('bidang')
            data_user_profile.jabatan = data_form.get('jabatan')
            data_user_profile.no_telepon = data_form.get('no_telepon')
            data_user_profile.role_pencatat = False
            data_user_profile.save()

            # kembali ke daftar user
            return HttpResponseRedirect('/user/')

        else:
            # The supplied form contained errors - just print them to the terminal.
            print(form.errors)
    else:

        # generate data untuk ditampilkan di form
        data_user = User.objects.get(username=username)
        data_user_profile = UserProfile.objects.get(user=data_user)

        initial = {}
        initial['username'] = data_user.username
        initial['password'] = ''
        initial['email'] = data_user.email
        initial['groups'] = data_user.groups.values_list('id',flat=True) # set groups list with initial selected value
        initial['first_name'] = data_user.first_name
        initial['last_name'] = data_user.last_name
        initial['is_active'] = data_user.is_active
        initial['bidang'] = data_user_profile.bidang
        initial['jabatan'] = data_user_profile.jabatan
        initial['no_telepon'] = data_user_profile.no_telepon

        form = UserProfileForm(initial=initial)

    return render(request, 'MainApp/user/user_edit.html', {'form': form ,'username': username, 'page_user_active':'active'})

@login_required
def user_delete(request, username):
    data = {}

    # hanya admin yang bisa menghapus user
    if is_admin(request.user) == False:
        data['alert_type'] =  "danger"
        data['alert_message'] = "Hanya administrator yang dijinkan untuk menghapus user!"
        return render(request, "MainApp/index.html", data)

    try:
        # get user
        data_user = User.objects.get(username=username)
        # get data user profile
        data_user_profile = UserProfile.objects.get(user=data_user)

        # delete data user profile and then delete user
        data_user_profile.delete()
        data_user.delete()

    except User.DoesNotExist:
        pass

    # kembali ke daftar user
    return HttpResponseRedirect('/user/')

def user_login(request):

    template_dict = {'page_login_active':'active'}

    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
                # We use request.POST.get('<variable>') as opposed to request.POST['<variable>'],
                # because the request.POST.get('<variable>') returns None, if the value does not exist,
                # while the request.POST['<variable>'] will raise key error exception
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.

        user = authenticate(username=username, password=password)

        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)

                # log aktivitas login
                log_aktivitas(user, "%s login." % user.username)

                return HttpResponseRedirect('/surat/')
            else:
                # An inactive account was used - no logging in!
                template_dict['alert_type'] = 'danger'
                template_dict['alert_message'] = "Akun Simansur %s dinonaktifkan!" % username
                return render(request, 'MainApp/login.html', template_dict)
        else:
            # Bad login details were provided. So we can't log the user in.
            template_dict['alert_type'] = 'danger'
            template_dict['alert_message'] = "Invalid login details: {0}, {1}".format(username, password)
            return render(request, 'MainApp/login.html', template_dict)


    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render(request, 'MainApp/login.html', template_dict)

# Use the login_required() decorator to ensure only those logged in can access the view.
@login_required
def user_logout(request):

    log_aktivitas(request.user, "%s logout." % request.user.username)

    # Since we know the user is logged in, we can now just log them out.
    logout(request)

    # Take the user back to the homepage.
    return HttpResponseRedirect('/')

@login_required
def aktivitas(request):
    data = {}

    # hanya admin yang bisa melihat aktivitas user
    if is_admin(request.user) == False:
        data['alert_type'] =  "danger"
        data['alert_message'] = "Hanya administrator yang dijinkan untuk mengakses halaman log aktivitas!"
        return render(request, "MainApp/index.html", data)

    semua_aktivitas_user = Aktivitas.objects.all()

    paginator = Paginator(semua_aktivitas_user, DATA_PER_HALAMAN)

    page = request.GET.get('page')
    try:
        aktivitas_user = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        aktivitas_user = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        aktivitas_user = paginator.page(paginator.num_pages)

    jumlah_data_sebelumnya  = (aktivitas_user.number - 1) * DATA_PER_HALAMAN



    data['aktivitas_user'] =  aktivitas_user
    data['page_aktivitas_active'] = 'active'
    data['jumlah_data_sebelumnya'] = jumlah_data_sebelumnya

    return render(request, "MainApp/aktivitas/aktivitas.html", data)

@login_required
def statistik(request):
    current_month = datetime.now().month

    surat_bulan_ini = Surat.objects.filter(tanggal_surat_masuk__month=current_month)

    data_statistik_surat = "Jumlah surat yang dikirim bulan %s tahun %s = %s." \
                           % (str(datetime.now().month) , str(datetime.now().year), str(surat_bulan_ini.count()) )

    context_dict = {'data_statistik_surat': data_statistik_surat}


    return render(request, "MainApp/statistik.html", context_dict)


"""
Daftar method yang dipanggil oleh method lain dalam views
"""

def log_aktivitas(user, aktivitas):
    # log aktivitas login
    log_aktivitas = Aktivitas()
    log_aktivitas.user = user
    log_aktivitas.aktivitas = aktivitas
    log_aktivitas.save()

def catat_track_surat(surat, status_surat):
    trackSurat = TrackSurat()
    trackSurat.surat = surat
    trackSurat.status = status_surat
    trackSurat.save()

def is_admin(user):
    return user.groups.filter(name='admin').exists()

def user_dalam_group(user, nama_group):
    return user.groups.filter(name=nama_group).exists()

