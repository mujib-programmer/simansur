import  os
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import render

from MainApp.models import Surat, Disposisi, UserProfile
from MainApp.forms import SuratForm, DisposisiForm

# Create your views here.
def index(request):
    context_dict = {'slug': 'login'}

    return render(request, 'MainApp/index.html', context_dict)

def surat(request):

    # get data surat
    semua_surat = Surat.objects.all()

    context_dict = {'semua_surat': semua_surat}

    return render(request, 'MainApp/surat.html', context_dict)

def surat_detail(request, no_surat):

    # get data surat
    dataSurat = Surat.objects.get(no_surat=no_surat)

    try:
        # get disposisi surat
        semua_disposisi_surat = Disposisi.objects.filter(surat=dataSurat)

    except Disposisi.DoesNotExist:
         semua_disposisi_surat = None

    context_dict = {'surat': dataSurat, 'semua_disposisi_surat': semua_disposisi_surat}

    return render(request, 'MainApp/surat_detail.html', context_dict)

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

    context_dict = {'semua_surat': semua_surat}

    return render(request, 'MainApp/surat.html', context_dict)


def surat_tambah(request):

    # A HTTP POST?
    if request.method == 'POST':
        form = SuratForm(request.POST, request.FILES)

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
        form = SuratForm()

    # Bad form (or form details), no form supplied...
    # Render the form with error messages (if any).
    return render(request, 'MainApp/surat_tambah.html', {'form': form})


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
    return render(request, 'MainApp/surat_edit.html', {'form': form ,'no_surat': no_surat})

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





def disposisi_tambah(request, no_surat):

    # get data surat
    dataSurat = Surat.objects.get(no_surat=no_surat)

    # A HTTP POST?
    if request.method == 'POST':
        form = DisposisiForm(request.POST, )

        # Have we been provided with a valid form?
        if form.is_valid():

            form.save(commit=True)

            # go to surat view
            return surat_detail(request, no_surat)

        else:
            # The supplied form contained errors - just print them to the terminal.
            print(form.errors)
    else:
        # If the request was not a POST, display the form to enter details.
        form = DisposisiForm()
        form.surat = dataSurat

    return render(request, 'MainApp/disposisi_tambah.html', {'form': form ,'no_surat': no_surat})


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
        #form.surat = dataSurat

    return render(request, 'MainApp/disposisi_edit.html', {'form': form ,'id_disposisi': id_disposisi})

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


def user(request):
    context_dict = {}

    return render(request, 'MainApp/user.html', context_dict)

def login(request):
    context_dict = {'slug': 'login'}

    return render(request, 'MainApp/login.html', context_dict)
