from django import forms
from django.forms import ModelForm
from dashboard.models import Barang
from dashboard.models import Transaksi
from dashboard.models import Costumer


class form_barang(ModelForm):
    class Meta:
        model = Barang
        fields = '__all__'

        widgets = {
            # nama pada widget harus sana dengan pada file models.py
            'kode': forms.TextInput({'class': 'form-control'}),
            'nama': forms.TextInput({'class': 'form-control'}),
            'stok': forms.NumberInput({'class': 'form-control'}),
            'harga': forms.NumberInput({'class': 'form-control'}),
             'link_gbr': forms.TextInput({'class': 'form-control'}),
            'jenis_id': forms.Select({'class': 'form-control'}),
        }
        
class form_transaksi(ModelForm):
    class Meta:
        model = Transaksi
        fields = '__all__'
        
        Widget = {
             # nama pada widget harus sana dengan pada file models.py
            'nama': forms.TextInput({'class': 'form-control'}),
            'phone': forms.TextInput({'class': 'form-control'}),
            'debit': forms.TextInput({'class': 'form-control'}),
            'kredit': forms.TextInput({'class': 'form-control'}),
            'saldo': forms.TextInput({'class': 'form-control'}),
        }
class form_costumer(ModelForm):
    class Meta:
        model = Costumer
        fields = '__all__'
        
        Widget = {
             # nama pada widget harus sana dengan pada file models.py
            'nama': forms.TextInput({'class': 'form-control'}),
            'namabrg': forms.TextInput({'class': 'form-control'}),
            'jumlahbrg': forms.TextInput({'class': 'form-control'}),
            'harga': forms.TextInput({'class': 'form-control'}),
            'totalbyr': forms.TextInput({'class': 'form-control'}),
            'alamat': forms.TextInput({'class': 'form-control'}),
        }



