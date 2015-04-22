from django.http import HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import render

from MainApp.models import Surat, Disposisi, UserProfile
from MainApp.forms import SuratForm

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
    surat = Surat.objects.get(no_surat=no_surat)

    context_dict = {'surat': surat}

    return render(request, 'MainApp/surat_detail.html', context_dict)

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



def user(request):
    context_dict = {}

    return render(request, 'MainApp/user.html', context_dict)

def login(request):
    context_dict = {'slug': 'login'}

    return render(request, 'MainApp/login.html', context_dict)
