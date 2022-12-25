from django.contrib import admin

from presensi.models import Jabatan, Order, Pegawai, Shift

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass

@admin.register(Shift)
class ShiftAdmin(admin.ModelAdmin):
    pass

@admin.register(Jabatan)
class JabatanAdmin(admin.ModelAdmin):
    pass

@admin.register(Pegawai)
class PegawaiAdmin(admin.ModelAdmin):
    pass