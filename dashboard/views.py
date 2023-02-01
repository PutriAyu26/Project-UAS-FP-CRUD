from django.shortcuts import render, redirect
from dashboard.models import Barang, Transaksi, Costumer
from dashboard.forms import form_barang, form_transaksi, form_costumer
from django.contrib import messages

def produk(request):
    nama = 'Produk'
    konteks = {
        'title': nama,
    }
    return render(request, 'produk.html', konteks)

# Create your views here.


def tambah_barang(request):
    if request.POST:
        form= form_barang(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Data Berhasil Ditambahkan")
            form = form_barang()
            konteks = {
                'form': form,
            }
            return render(request, 'tambah_barang.html', konteks)
    else:
        form = form_barang()
        konteks = {
            'form': form,
        }
    return render(request, 'tambah_barang.html', konteks)

def tambah_transaksi(request):
    if request.POST:
        form= form_transaksi(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Data Berhasil Ditambahkan")
            form = form_transaksi()
            konteks = {
                'form': form,
            }
            return render(request, 'tambah_transaksi.html', konteks)
    else:
        form = form_transaksi()
        konteks = {
            'form': form,
        }
    return render(request, 'tambah_transaksi.html', konteks)

def tambah_costumer(request):
    if request.POST:
        form= form_costumer(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Data Berhasil Ditambahkan")
            form = form_costumer()
            konteks = {
                'form': form,
            }
            return render(request, 'tambah_costumer.html', konteks)
    else:
        form = form_costumer()
        konteks = {
            'form': form,
        }
    return render(request, 'tambah_costumer.html', konteks)


def Barang_view(request):
    Barangs = Barang.objects.all()
    
    konteks={
        'Barangs': Barangs,
    }
    return render(request,'tampil_barang.html', konteks)

def transaksi_list(request):
    Transaksis = Transaksi.objects.all()
    konteks={
        'Transaksis' :Transaksis,
    }
    return render(request, 'transaksi_list.html', konteks)

def List_costumer(request):
    Costumers = Costumer.objects.all()
    
    konteks={
        'Costumers':Costumers
    }
    return render(request, 'costumer.html', konteks)

def ubah_brg(request, id_barang):
    Barangs=Barang.objects.get(id=id_barang)
    if request.POST:
        form= form_barang(request.POST, instance=Barangs)
        if form.is_valid():
            form.save()
            messages.success(request, "Data Berhasil Diubah")
            return redirect('ubah_brg',id_barang=id_barang)
    else:
        form= form_barang(instance=Barangs)
        konteks= {
            'form': form,
            'Barangs': Barangs,
        }
    return render(request, 'ubah_brg.html', konteks)

def hapus_brg(request, id_barang):
    Barangs=Barang.objects.filter(id=id_barang)
    Barangs.delete()
    messages.success(request, "Data Terhapus")
    return redirect('brgview')


def ubah_transaksi(request, id_transaksi):
    Transaksis=Transaksi.objects.get(id=id_transaksi)
    if request.POST:
        form= form_transaksi(request.POST, instance=Transaksis)
        if form.is_valid():
            form.save()
            messages.success(request, "Data Berhasil Diubah")
            return redirect('ubah_transaksi',id_transaksi=id_transaksi)
    else:
        form= form_transaksi(instance=Transaksis)
        konteks= {
            'form': form,
            'Transaksis': Transaksis,
        }
    return render(request, 'ubah_transaksi.html', konteks)

def hapus_transaksi(request, id_transaksi):
    Transaksis=Transaksi.objects.filter(id=id_transaksi)
    Transaksis.delete()
    messages.success(request, "Data Terhapus")
    return redirect('transaksi')

def ubah_costumer(request, id_costumer):
    Costumers=Costumer.objects.get(id=id_costumer)
    if request.POST:
        form= form_costumer(request.POST, instance=Costumers)
        if form.is_valid():
            form.save()
            messages.success(request, "Data Berhasil Diubah")
            return redirect('ubah_costumer',id_costumer=id_costumer)
    else:
        form= form_costumer(instance=Costumers)
        konteks= {
            'form': form,
            'Costumers': Costumers,
        }
    return render(request, 'ubah_costumer.html', konteks)

def hapus_costumer(request, id_costumer):
    Costumers=Costumer.objects.filter(id=id_costumer)
    Costumers.delete()
    messages.success(request, "Data Terhapus")
    return redirect('costumer')




    
    
