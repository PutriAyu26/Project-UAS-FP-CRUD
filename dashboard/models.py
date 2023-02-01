from datetime import datetime
from django.db import models

# Create your models here.


class Jenis(models.Model):
    nama = models.CharField(max_length=50)
    ket = models.TextField()

    def __str__(self):
        return self.nama


class Barang(models.Model):
    kode = models.CharField(max_length=8)
    nama = models.CharField(max_length=100)
    stok = models.IntegerField()
    harga = models.BigIntegerField()
    link_gbr = models.CharField(max_length=200, blank=True)
    time = models.DateTimeField(auto_now_add=True)
    jenis_id = models.ForeignKey(Jenis, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return "{}.{}.{}.{}.{}.{}".format(self.kode,self.nama,self.stok,self.harga,self.link_gbr,self.jenis_id)
    
class Transaksi(models.Model):
    nama = models.CharField(max_length=100)
    phone = models.CharField(max_length=50)
    debit = models.IntegerField(default=0)
    kredit = models.IntegerField(default=0)
    saldo = models.IntegerField(default=0)
    jenis_id = models.ForeignKey(Jenis(), on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return "{}.{}.{}.{}.{}.{}".format(self.nama,self.phone,self.debit,self.kredit,self.saldo,self.jenis_id)
    
    
class Costumer(models.Model):
    nama = models.CharField(max_length=70)
    namabrg = models.CharField(max_length=70)
    jumlahbrg = models.IntegerField()
    harga = models.BigIntegerField()
    totalbyr = models.BigIntegerField()
    alamat = models.CharField(max_length=150)
    
    def __str__(self):
        return "{}. {}.{}.{}.{}.{}".format(self.nama,self.namabrg,self.jumlahbrg,self.harga,self.totalbyr,self.alamat)
    
       
        


       
        

