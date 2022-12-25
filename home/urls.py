from django.urls import path, re_path

from .views import *

urlpatterns = [
    path('login/', login_view, name='login'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('addsiswa/', SiswaView.as_view(), name='addsiswa'),
    re_path(r'^siswa/(?:(?P<pk>\d+)/)?(?:(?P<action>\w+)/)?', SiswaView.as_view(), name='siswa'),
    re_path(r'^kelas/(?:(?P<pk>\d+)/)?(?:(?P<action>\w+)/)?', KelasView.as_view(), name='kelas'),
    re_path(r'^presensi/(?:(?P<pk>\d+)/)?(?:(?P<action>\w+)/)?', PresensiView.as_view(), name='presensi'),
    re_path(r'^pegawai/(?:(?P<pk>\d+)/)?(?:(?P<action>\w+)/)?', PegawaiView.as_view(), name='pegawai'),
    re_path(r'^jabatan/(?:(?P<pk>\d+)/)?(?:(?P<action>\w+)/)?', JabatanView.as_view(), name='jabatan'),
    re_path(r'^shift/(?:(?P<pk>\d+)/)?(?:(?P<action>\w+)/)?', ShiftView.as_view(), name='shift'),
    path('tambah/', PegawaiView.as_view(), name='tambah'),
    path('kelolaizin/', PresensiView.as_view(), name='kelolaizin'),
    path('train/', train_view, name='train'),
    path('', index_view, name='index'),
]
