# Generated by Django 3.2.6 on 2022-06-13 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('presensi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pegawai',
            name='foto',
            field=models.ImageField(blank=True, upload_to='media/pegawai/'),
        ),
    ]
