from django.db import models

# Create your models here.
class ModelWajah(models.Model):
    nama = models.FileField(upload_to='media/model/')
    total_data = models.CharField(max_length=4)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.nama}'