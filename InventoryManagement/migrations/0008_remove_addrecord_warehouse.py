# Generated by Django 3.1 on 2020-11-17 07:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('InventoryManagement', '0007_auto_20201117_1238'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='addrecord',
            name='warehouse',
        ),
    ]
