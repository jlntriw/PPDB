# Generated by Django 4.2.5 on 2023-10-09 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0014_alter_datasiswa_tahun'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datasiswa',
            name='tahun',
            field=models.IntegerField(auto_created=True, blank=True, null=True),
        ),
    ]
