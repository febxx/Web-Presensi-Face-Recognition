# Generated by Django 3.2.6 on 2022-06-18 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('presensi', '0003_presensi'),
    ]

    operations = [
        migrations.AlterField(
            model_name='presensi',
            name='suhu',
            field=models.CharField(blank=True, max_length=5),
        ),
    ]
