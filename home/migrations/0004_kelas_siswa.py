# Generated by Django 4.0.6 on 2022-07-29 11:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_rename_nama_jabatan_jabatan_nama_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kelas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Siswa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nis', models.CharField(max_length=18)),
                ('nama', models.CharField(max_length=255)),
                ('jk', models.CharField(choices=[('L', 'Laki-Laki'), ('P', 'Perempuan')], max_length=1)),
                ('nohp', models.CharField(max_length=12)),
                ('alamat', models.CharField(max_length=300)),
                ('foto', models.ImageField(blank=True, upload_to='media/siswa/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('kelas', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.kelas')),
            ],
        ),
    ]
