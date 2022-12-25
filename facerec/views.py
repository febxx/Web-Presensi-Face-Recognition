from django.shortcuts import redirect

from facerec.main import *
from facerec.models import ModelWajah
from presensi.utils import dir_pegawai

def train_view(request):
    nama_model = 'model/model_wajah.clf'
    total = train_model(dir_pegawai, model_name=nama_model, n_neighbors=2)
    content = {'nama': nama_model, 'total_data': total}
    ModelWajah.objects.update_or_create(pk=1, defaults=content)
    return redirect('dashboard')