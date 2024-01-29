from django.shortcuts import render, redirect, get_object_or_404
from .models import Avocat
from .models import Client
from .models import Contract

from .forms import AvocatForm, ClientForm, ContractForm

def index(request):
    return render(request, "main_app/index.html", {})

def avocat_list(request):
    avocati = Avocat.objects.all().order_by('id_avocat')
    return render(request, 'main_app/avocat_list.html', {'avocati': avocati})

def client_list(request):
    clienti = Client.objects.all().order_by('id_client')
    return render(request, 'main_app/client_list.html', {'clienti': clienti})

def contract_list(request):
    contracte = Contract.objects.select_related('id_avocat_ctr', 'id_client_ctr').all().order_by('id_contract')
    return render(request, 'main_app/contract_list.html', {'contracte': contracte})

def add_avocat(request):
    if request.method == 'POST':
        form = AvocatForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('avocat_list')  # Redirect to avocat list view after adding

    else:
        form = AvocatForm()

    return render(request, 'main_app/new_avocat.html', {'form': form})

def add_client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('client_list')  # Redirect to client list view after adding

    else:
        form = ClientForm()

    return render(request, 'main_app/new_client.html', {'form': form})

def add_contract(request):
    if request.method == 'POST':
        form = ContractForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contract_list')  # Redirect to contract list view after adding

    else:
        form = ContractForm()

    return render(request, 'main_app/new_contract.html', {'form': form})

def delete_avocat(request, avocat_id):
    avocat = Avocat.objects.get(id_avocat=avocat_id)
    avocat.delete()
    return redirect('avocat_list')
def delete_client(request, client_id):
    client = Client.objects.get(id_client=client_id)
    client.delete()
    return redirect('client_list')
def delete_contract(request, contract_id):
    contract = Contract.objects.get(id_contract=contract_id)
    contract.delete()
    return redirect('contract_list')


def modify_avocat(request, avocat_id):
    avocat = get_object_or_404(Avocat, id_avocat=avocat_id)

    if request.method == 'POST':
        form = AvocatForm(request.POST, instance=avocat)
        if form.is_valid():
            form.save()
            return redirect('avocat_list')
    else:
        form = AvocatForm(instance=avocat)

    return render(request, 'main_app/modify_avocat.html', {'form': form})

def modify_client(request, client_id):
    client = get_object_or_404(Client, id_client=client_id)

    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect('client_list')  # Redirect to client list view after modification
    else:
        form = ClientForm(instance=client)

    return render(request, 'main_app/modify_client.html', {'form': form})

def modify_contract(request, contract_id):
    contract = get_object_or_404(Contract, id_contract=contract_id)

    if request.method == 'POST':
        form = ContractForm(request.POST, instance=contract)
        if form.is_valid():
            form.save()
            return redirect('contract_list')  # Redirect to contract list view after modification
    else:
        form = ContractForm(instance=contract)

    return render(request, 'main_app/modify_contract.html', {'form': form})