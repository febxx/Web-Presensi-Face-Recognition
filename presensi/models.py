from django.db import models
from django.db.models import Sum, Count, Max

class Shift(models.Model):
    masuk = models.TimeField()
    pulang = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.id} ({self.masuk} - {self.pulang})'

class Jabatan(models.Model):
    nama_jabatan = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.nama_jabatan}'

class Pegawai(models.Model):
    nip = models.CharField(max_length=18)
    nama = models.CharField(max_length=255)
    nohp = models.CharField(max_length=12)
    foto = models.ImageField(upload_to='media/pegawai/', blank=True)
    jabatan = models.ForeignKey(Jabatan, on_delete=models.CASCADE)
    shift = models.ForeignKey(Shift, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.nama}'

    @classmethod
    def total_info(cls):
        return cls.objects.aggregate(jumlah_pegawai=Count('id'))

class Presensi(models.Model):
    pegawai = models.ForeignKey(Pegawai, on_delete=models.CASCADE)
    tanggal = models.DateField()
    masuk = models.TimeField()
    pulang = models.TimeField()
    suhu = models.CharField(max_length=5, blank=True)
    keterangan = models.CharField(max_length=100)

    @classmethod
    def hadir(cls):
        return cls.objects.filter(jumlah_pegawai=Count('id'))

class Order(models.Model):
    product_name = models.CharField(max_length=40)
    price = models.IntegerField()
    created_time = models.DateField(db_index=True)
    updated_time = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'order'
        verbose_name_plural = 'orders'
    
    MONTHS = {1: 'Januari', 2: 'Februari', 3: 'Maret', 4: 'April', 5: 'Mei', 6: 'Juni', 7: 'Juli', 8: 'Agustus', 9: 'September', 10: 'Oktober', 11: 'November', 12: 'Desember'}
    @classmethod
    def total_info(cls):
        return cls.objects.aggregate(total_sales=Sum('price'), total_orders=Count('id'), peek_sales=Max('price'))

    @classmethod
    def best_month(cls):
        res = {}
        month_price = cls.objects.values_list('created_time__month').annotate(total=Sum('price'))
        if month_price:
            res['month'], res['price'] = max(month_price, key=lambda i: i[1])
            res['month_name'] = cls.MONTHS.get(res['month'])
        return res