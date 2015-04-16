from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    context_dict = {'slug': 'login'}

    return render(request, 'MainApp/index.html', context_dict)

def surat(request):
    context_dict = {}

    return render(request, 'MainApp/surat.html', context_dict)

def user(request):
    context_dict = {}

    return render(request, 'MainApp/user.html', context_dict)

def login(request):
    context_dict = {'slug': 'login'}

    return render(request, 'MainApp/login.html', context_dict)
