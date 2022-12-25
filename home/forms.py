from django import forms

from home.models import *

class LoginForm(forms.Form):
    username = forms.CharField(
        widget= forms.TextInput(
            attrs= {'placeholder': 'Username', 'class': 'form-control'}
        )
    )
    password = forms.CharField(
        widget= forms.PasswordInput(
            attrs= {'placeholder': 'Password','class': 'form-control'}
        )
    )

class SiswaForm(forms.ModelForm):
    nis = forms.CharField(
        label='NIS',
        widget= forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Masukkan NIS'}
        )
    )
    nama = forms.CharField(
        label='Nama Siswa',
        widget= forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Masukkan Nama'}
        )
    )
    jk = forms.ChoiceField(
        label="Jenis Kelamin",
        choices=GENDER_CHOICES,
        widget= forms.Select(
            attrs={
                'class': 'form-control',
            }
        ), 
    )
    nohp = forms.CharField(
        max_length=13,
        label="Nomor Handphone",
        widget= forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Masukkan No HP'}
        )
    )
    alamat = forms.CharField(
        label='Alamat Rumah',
        widget= forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Masukkan Nama'}
        )
    )
    kelas = forms.ModelChoiceField(
        queryset=Kelas.objects.all(),
        widget= forms.Select(
            attrs={
                'class': 'form-control',
            }
        ), 
        to_field_name='nama'
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

    class Meta:
        model = Siswa
        fields = '__all__'

class KelasForm(forms.ModelForm):
    nama = forms.CharField(
        label='Nama Kelas',
        widget= forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        )
    )
    class Meta:
        model = Kelas
        fields = ['nama',]

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
        to_field_name='nama'
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

class JabatanForm(forms.ModelForm):
    nama = forms.CharField(
        label='Nama Jabatan',
        widget= forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        )
    )
    class Meta:
        model = Jabatan
        fields = ['nama',]

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