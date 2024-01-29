"""
URL configuration for PIBD_Django project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import avocat_list, add_avocat, modify_avocat, delete_avocat
from .views import client_list, add_client, modify_client, delete_client
from .views import contract_list, add_contract, modify_contract,  delete_contract

from . import views
urlpatterns = [
    path('avocati/', avocat_list, name='avocat_list'),
    path('add_avocat/', add_avocat, name='add_avocat'),
    path('modify_avocat/<int:avocat_id>/', modify_avocat, name='modify_avocat'),
    path('delete_avocat/<int:avocat_id>/', delete_avocat, name='delete_avocat'),

    path('clienti/', client_list, name='client_list'),
    path('add_client/', add_client, name='add_client'),
    path('modify_client/<int:client_id>/', modify_client, name='modify_client'),
    path('delete_client/<int:client_id>/', delete_client, name='delete_client'),

    path('contracte/', contract_list, name='contract_list'),
    path('add_contract/', add_contract, name='add_contract'),
    path('modify_contract/<int:contract_id>/', modify_contract, name='modify_contract'),
    path('delete_contract/<int:contract_id>/', delete_contract, name='delete_contract'),

    path('',views.index, name='index')
]
