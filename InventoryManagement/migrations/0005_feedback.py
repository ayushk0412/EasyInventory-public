# Generated by Django 3.1 on 2020-11-16 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('InventoryManagement', '0004_addrecord'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=100)),
                ('lname', models.CharField(max_length=100)),
                ('ph_no', models.CharField(max_length=12)),
                ('email', models.CharField(max_length=50)),
                ('comments', models.TextField()),
            ],
        ),
    ]
