# Generated by Django 4.2.5 on 2023-11-23 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0025_rekappembayaran_keterangan_alter_datasiswa_tahun'),
    ]

    operations = [
        migrations.CreateModel(
            name='pengaturan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kuota', models.IntegerField(blank=True, null=True)),
                ('total_pembayaran', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
