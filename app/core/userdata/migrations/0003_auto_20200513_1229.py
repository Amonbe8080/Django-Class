# Generated by Django 2.2.12 on 2020-05-13 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userdata', '0002_auto_20200513_1216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habiluser',
            name='DescHabi',
            field=models.TextField(verbose_name='Descripción de la Habilidad'),
        ),
    ]
