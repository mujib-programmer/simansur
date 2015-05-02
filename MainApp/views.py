import  os
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User, Group, Permission

from MainApp.models import Surat, Disposisi, UserProfile, Aktivitas
from MainApp.forms import SuratForm, DisposisiForm, UserProfileForm

# untuk mengecek apakah user termasuk dalam kelompok groups yang diijinkan untuk mengakses methods pada view
def group_required(*group_names):
    """Requires user membership in at least one of the groups passed in."""
    def in_groups(u):
        if u.is_authenticated():
            if bool(u.groups.filter(name__in=group_names)) | u.is_superuser:
                return True
        return False
    return user_passes_test(in_groups, login_url='/login')

# Create your views here.
def index(request):
    context_dict = {'slug': 'login', 'page_home_active':'active'}

    return render(request, 'MainApp/index.html', context_dict)

@login_required
def surat(request):
    context_dict = {}

    user_saat_ini = request.user
    user_profile_saat_ini = UserProfile.objects.get(user=user_saat_ini)

    # mengecek apakah user memiliki hak akses untuk menambahkan surat, bisa dari user permissions atau group permission
    #user_can_add_surat = user_saat_ini.has_perm('MainApp.add_surat')

    # ambil data surat sesuai dengan yang login
    # manajer surat akan bisa mendapatkan semua data surat
    # pencatat surat hanya bisa mendapatkan data surat yang di catat olehnya
    # penerima surat hanya bisa mendapatkan semua surat yang ditujukan kepadanya
    if bool(user_saat_ini.groups.filter(name__in = ("manajer surat") ) ) | user_saat_ini.is_superuser: # pengecekan user has groups belum bekerja
        # get data surat
        semua_surat = Surat.objects.all()

    else:
        try:
            # ambil semua surat yang terkait dengan user saja
            semua_surat = Surat.objects.filter(id_pencatat=user_profile_saat_ini)

        except Surat.DoesNotExist:
            semua_surat = None

    context_dict['semua_surat'] = semua_surat
    context_dict['page_surat_active'] = 'active'


    return render(request, 'MainApp/surat.html', context_dict)

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

    return render(request, 'MainApp/surat_detail.html', context_dict)

@login_required
def surat_delete(request, no_surat):

    try:
        # get data surat
        dataSurat = Surat.objects.get(no_surat=no_surat)

        dataSurat.delete()

    except Surat.DoesNotExist:
        # jika data surat yang diinginkan untuk dihapus tidak ditemukan, tampilkan daftar semua surat
        return surat(request)

    # get data surat
    semua_surat = Surat.objects.all()

    context_dict = {'semua_surat': semua_surat, 'page_surat_active':'active'}

    return render(request, 'MainApp/surat.html', context_dict)

@login_required
#@group_required('admin', 'pencatat surat')
def surat_tambah(request):

    # dapatkan data user yang sedang login
    user_saat_ini = request.user
    user_profile_saat_ini = UserProfile.objects.get(user=user_saat_ini)

    # A HTTP POST?
    if request.method == 'POST':
        form = SuratForm(request.POST, request.FILES)

        # Have we been provided with a valid form?
        if form.is_valid():
            data_surat = form.save(commit=False)

            data_surat.id_pencatat = user_profile_saat_ini # pencatat surat adalah user profile yang sedang login

            form.save(commit=True)

            # go to surat view
            return surat(request)
        else:
            # The supplied form contained errors - just print them to the terminal.
            print(form.errors)
    else:
        # If the request was not a POST, display the form to enter details.
        form = SuratForm()

    # Bad form (or form details), no form supplied...
    # Render the form with error messages (if any).
    return render(request, 'MainApp/surat_tambah.html', {'form': form, 'page_surat_active':'active'})

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
    return render(request, 'MainApp/surat_edit.html', {'form': form ,'no_surat': no_surat, 'page_surat_active':'active'})

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
def disposisi_tambah(request, no_surat):

    # get data surat
    dataSurat = Surat.objects.get(no_surat=no_surat)

    # A HTTP POST?
    if request.method == 'POST':
        form = DisposisiForm(request.POST, )

        # Have we been provided with a valid form?
        if form.is_valid():

            disposisi = form.save(commit=False)
            disposisi.surat = dataSurat

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

    # get data surat
    semua_user_profile = UserProfile.objects.all()

    context_dict = {'semua_user_profile': semua_user_profile, 'page_user_active':'active'}

    return render(request, 'MainApp/user.html', context_dict)

def user_detail(request, username):

    try:
        # get data user
        user = User.objects.get(username=username)

        # get data userprofile
        user_profile = UserProfile.objects.get(user=user)


    except Disposisi.DoesNotExist:
         user_profile = None

    context_dict = {'user_profile': user_profile, 'page_user_active':'active'}

    return render(request, 'MainApp/user_detail.html', context_dict)

@login_required
def user_tambah(request):

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

                # membuat user profile baru
                user_profile_baru = UserProfile(user=user_baru)
                user_profile_baru.bidang = data_form.get('bidang')
                user_profile_baru.jabatan = data_form.get('jabatan')
                user_profile_baru.no_telepon = data_form.get('no_telepon')
                user_profile_baru.role_pencatat = False
                user_profile_baru.save()

                #form.save(commit=false)

                # go to surat view
                return user(request)

        else:
            # The supplied form contained errors - just print them to the terminal.
            print(form.errors)
    else:
        # If the request was not a POST, display the form to enter details.
        form = UserProfileForm()

    return render(request, 'MainApp/user_tambah.html', {'form': form, 'page_user_active':'active'})

@login_required
def user_edit(request, username):

    # A HTTP POST?
    if request.method == 'POST':
        form = UserProfileForm(request.POST)

        # Have we been provided with a valid form?
        if form.is_valid():
            data_form = form.cleaned_data

            # membuat object user
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

            # membuat user profile baru
            data_user_profile = UserProfile.objects.get(user=data_user)
            data_user_profile.bidang = data_form.get('bidang')
            data_user_profile.jabatan = data_form.get('jabatan')
            data_user_profile.no_telepon = data_form.get('no_telepon')
            data_user_profile.role_pencatat = False
            data_user_profile.save()

            # go to surat view
            return user(request)

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

    return render(request, 'MainApp/user_edit.html', {'form': form ,'username': username, 'page_user_active':'active'})

@login_required
def user_delete(request, username):

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

    return user(request)

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

def log_aktivitas(user, aktivitas):
    # log aktivitas login
    log_aktivitas = Aktivitas()
    log_aktivitas.user = user
    log_aktivitas.aktivitas = aktivitas
    log_aktivitas.save()