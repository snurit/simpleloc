# Generated by Django 2.1.3 on 2018-12-03 15:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0002_auto_20181203_1525'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contract',
            name='totalPrice',
        ),
    ]
