# Generated by Django 4.1 on 2022-08-27 06:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('houses', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='house',
            options={'verbose_name': 'дом', 'verbose_name_plural': 'дома'},
        ),
    ]
