from django.shortcuts import render
from .models import Avocat
from .models import Client
def index(request):
    return render(request, "main_app/index.html", {})

def avocat_list(request):
    avocati = Avocat.objects.all()
    return render(request, 'main_app/avocat_list.html', {'avocati': avocati})

def client_list(request):
    clienti = Client.objects.all()
    return render(request, 'main_app/client_list.html', {'clienti': clienti})