from django.urls import path, re_path

from .views import *

urlpatterns = [
    path('dashboard/', index, name='dashboard'),
    path('presensi/', presensi_view, name='presensi'),
    re_path(r'^pegawai/(?:(?P<pk>\d+)/)?(?:(?P<action>\w+)/)?', PegawaiView.as_view(), name='pegawai'),
    re_path(r'^jabatan/(?:(?P<pk>\d+)/)?(?:(?P<action>\w+)/)?', JabatanView.as_view(), name='jabatan'),
    # path('pegawai/<pk>/masuk', pegawaidetail_view, name='pegawaidetail'),
    # path('pegawai/', pegawai_view, name='pegawai'),
    path('shift/', shift_view, name='shift'),
    # path('jabatan/', jabatan_view, name='jabatan'),
    path('tambah/', tambah_view, name='tambah'),
    path('izin/', kelolaizin_view, name='izin')
    # re_path(r'^.*\.*', pages, name='pages'),
]