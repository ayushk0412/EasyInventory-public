# Generated by Django 3.1 on 2020-11-17 07:21

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('InventoryManagement', '0008_remove_addrecord_warehouse'),
    ]

    operations = [
        migrations.AddField(
            model_name='addrecord',
            name='warehouse',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]