# Generated by Django 4.0.6 on 2022-07-09 08:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_modelwajah'),
    ]

    operations = [
        migrations.RenameField(
            model_name='jabatan',
            old_name='nama_jabatan',
            new_name='nama',
        ),
        migrations.RenameField(
            model_name='modelwajah',
            old_name='total_data',
            new_name='total',
        ),
    ]
