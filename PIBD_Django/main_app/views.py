from django.shortcuts import render
from .models import Avocat

def index(request):
    return render(request, "main_app/index.html", {})

def avocat_list(request):
    avocati = Avocat.objects.all()
    return render(request, 'main_app/avocat_list.html', {'avocati': avocati})

