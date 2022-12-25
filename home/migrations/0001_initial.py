# Generated by Django 4.0.6 on 2022-07-06 07:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Jabatan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_jabatan', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pegawai',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nip', models.CharField(max_length=18)),
                ('nama', models.CharField(max_length=255)),
                ('nohp', models.CharField(max_length=12)),
                ('foto', models.ImageField(blank=True, upload_to='media/pegawai/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('jabatan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.jabatan')),
            ],
        ),
        migrations.CreateModel(
            name='Shift',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('masuk', models.TimeField()),
                ('pulang', models.TimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Presensi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tanggal', models.DateField()),
                ('masuk', models.TimeField()),
                ('pulang', models.TimeField()),
                ('suhu', models.CharField(blank=True, max_length=5)),
                ('keterangan', models.CharField(max_length=100)),
                ('pegawai', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.pegawai')),
            ],
        ),
        migrations.AddField(
            model_name='pegawai',
            name='shift',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.shift'),
        ),
    ]