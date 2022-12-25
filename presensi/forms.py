from django import forms

from presensi.models import Jabatan, Order, Pegawai, Shift

class PegawaiForm(forms.ModelForm):
    nip = forms.CharField(
        label='NIP/NIK',
        widget= forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Masukkan NIP/NIK'
            }
        )
    )
    nama = forms.CharField(
        label='Nama Pegawai',
        widget= forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Masukkan Nama'
            }
        )
    )
    nohp = forms.CharField(
        max_length=13,
        label="Nomor Handphone",
        widget= forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Masukkan No HP'
            }
        )
    )
    foto = forms.ImageField(
        required=False,
        label="Foto Wajah",
        widget= forms.ClearableFileInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Masukkan No HP',
                'accept': 'image/*',
                'multiple': True
            }
        )
    )
    jabatan = forms.ModelChoiceField(
        queryset=Jabatan.objects.all(),
        widget= forms.Select(
            attrs={
                'class': 'form-control',
            }
        ), 
        to_field_name='nama_jabatan'
    )
    shift = forms.ModelChoiceField(
        queryset=Shift.objects.all(),
        widget= forms.Select(
            attrs={
                'class': 'form-control',
            }
        ), 
    )

    class Meta:
        model = Pegawai
        fields = ['nip', 'nama', 'nohp', 'jabatan', 'shift', 'foto', ]
        # widgets = {'jabatan': JabatanSelect}

    
    # shift = forms.ForeignKey(Shift, on_delete=models.CASCADE)

class ShiftForm(forms.ModelForm):
    masuk = forms.TimeField(
        label='Jam Masuk',
        widget=forms.TimeInput(
            attrs= {
                'class': 'form-control',
                'type': 'time',
            }
        )
    )
    pulang = forms.TimeField(
        label='Jam Pulang',
        widget=forms.TimeInput(
            attrs= {
                'class': 'form-control',
                'type': 'time',
            }
        )
    )
    class Meta:
        model = Shift
        fields = ['masuk', 'pulang',]

class JabatanForm(forms.ModelForm):
    nama_jabatan = forms.CharField(
        label='Nama Jabatan',
        widget= forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        )
    )
    class Meta:
        model = Jabatan
        fields = ['nama_jabatan',]

class OrderForm(forms.ModelForm):
    product_name = forms.CharField(
        label = 'Product Name',
        widget = forms.TextInput(
            attrs = {
                'class': 'form-control order',
            }
        )
    )
    price = forms.IntegerField(
        label = '$ Price',
        widget = forms.TextInput(
            attrs = {
                'class': 'form-control order',
            }
        )
    )
    created_time = forms.DateTimeField(
        label = 'Created Time',
        widget = forms.TextInput(
            attrs= {
                'class': 'form-control order',
                'placeholder': 'YY-mm-dd H:i:s'
            }
        )
    )
    class Meta:
        model = Order
        fields = ['product_name', 'price', 'created_time']
