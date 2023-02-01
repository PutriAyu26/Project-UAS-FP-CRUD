from django.contrib import admin

# Register your models here.
from .models import Barang, Jenis, Transaksi, Costumer


class kolomBarang(admin.ModelAdmin):
    list_display = ['kode', 'nama', 'stok', 'harga', 'link_gbr', 'jenis_id']
    search_fields = ['kode', 'nama']
    list_filter = ('jenis_id',)
    list_per_page = 5
    
from .models import Transaksi

class kolomTransaksi(admin.ModelAdmin):
    list_display = ['nama', 'phone', 'debit', 'kredit', 'saldo', 'jenis_id']
    search_fields = ['nama', 'phone']
    list_filter = ('jenis_id',)
    list_per_page = 5
    
from .models import Costumer

class kolomCostumer(admin.ModelAdmin):
    list_display = ['nama', 'namabrg', 'jumlahbrg', 'harga', 'totalbyr', 'alamat']
    search_fields = ['nama', 'namabrg']
    list_filter = ('totalbyr',)
    list_per_page = 5


admin.site.register(Barang, kolomBarang)
admin.site.register(Jenis)
admin.site.register(Transaksi, kolomTransaksi)
admin.site.register(Costumer, kolomCostumer)
