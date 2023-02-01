"""olshop_handayani URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

from pathlib import Path
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from django.shortcuts import render
from dashboard.views import *

def home(request):
    nama = 'Home'
    konteks = {
        'title': nama,
    }
    return render(request, 'home.html', konteks)


urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', home, name='home'),
    path('produk/', produk, name='produk'),
    path('addbrg/', tambah_barang, name='addbrg'),
    path('brgview/', Barang_view, name='brgview'),
    path("transaksi/", transaksi_list, name='transaksi'),
    path("addtransaksi/", tambah_transaksi, name='addtransaksi'),
    path("costumer/", List_costumer, name='costumer'),
    path("addcostumer/", tambah_costumer, name='addcostumer'),
    path('ubah/<int:id_barang>', ubah_brg, name='ubah_brg'),
    path('hapus/<int:id_barang>', hapus_brg, name='hapus_brg'),
    path('ubaht/<int:id_transaksi>', ubah_transaksi, name='ubah_transaksi'),
    path('hapust/<int:id_transaksi>', hapus_transaksi, name='hapus_transaksi'),
    path('ubahc/<int:id_costumer>', ubah_costumer, name='ubah_costumer'),
    path('hapusc/<int:id_costumer>', hapus_costumer, name='hapus_costumer'),
       
]
