import os
from datetime import date, datetime, timedelta

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.core.files.storage import FileSystemStorage

from facerec.main import predict
from presensi.models import Pegawai, Presensi
from .forms import LoginForm
from presensi.utils import dir_presensi

delay_presensi = 30

def index(request):
    context = {}
    if request.method == 'POST':
        file = request.FILES['foto']
        fs = FileSystemStorage(dir_presensi)
        filename = fs.save(file.name, file)
        fileurl = os.path.join(dir_presensi, filename)
        predictions = predict(fileurl, model_path='media/model/model_wajah.clf')
        print(predictions)
        if predictions[0][0] != 'unknown':
            pegawai = Pegawai.objects.get(nama=predictions[0][0])
            now = datetime.now().time()
            jam_masuk = pegawai.shift.masuk
            jam_pulang = pegawai.shift.pulang
            today = date.today()
            hadir = Presensi.objects.filter(pegawai=pegawai, tanggal=today)
            mulai_presensi = (datetime.combine(date.min, jam_masuk) - timedelta(minutes=delay_presensi)).time()
            akhir_presensi = (datetime.combine(date.min, jam_masuk) + timedelta(minutes=delay_presensi)).time()
            print(hadir)
            # Presensi masuk
            if now >= mulai_presensi: # and now <= akhir_presensi:
                if not hadir.exists():
                    ket = 'Telat' if now >= jam_masuk else 'Hadir'
                        # difference = (datetime.combine(date.min, now) - datetime.combine(date.min, jam_masuk)).seconds
                        # telat = int(difference/60)
                        # print(telat)
                    Presensi(
                        pegawai = pegawai,
                        tanggal = today,
                        masuk = now,
                        pulang = datetime.strptime('00:00', '%H:%M'),
                        keterangan = ket,
                    ).save()

            elif now >= jam_pulang:
                print('masuk')
                if not hadir.exists():
                    return
                else:
                    print('masuk')
                    hadir.update(
                        pulang=now
                    )
                    
            # print(pegawai)
            # print(now)
            # print(jam_masuk)
            # print(mulai_presensi)
        
        return render(request, 'index.html', context)
    return render(request, 'index.html', context)

def login_view(request):
    form = LoginForm(request.POST or None)
    error_message = None

    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
            else:
                error_message = 'Invalid user'
        else:
            error_message = 'Error Login'
    
    context = {
        'form': form,
        'error': error_message
    }
    return render(request, 'pages/login.html', context)