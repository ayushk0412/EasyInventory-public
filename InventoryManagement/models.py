from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class categorydb(models.Model):
    author = models.CharField(max_length=100, null=True)
    category = models.CharField(max_length=100, null=True)


class AddRecord(models.Model):
    author = models.CharField(max_length=100, null=False)
    category = models.CharField(max_length=100, null=False)
    name = models.CharField(max_length=100, null=False)
    model = models.CharField(max_length=100, null=False)
    description = models.CharField(max_length=100, null=False)
    initialquantity = models.CharField(max_length=100, null=False)
    instockquantity = models.CharField(max_length=100, null=False)
    date = models.CharField(max_length=100, null=False)
    price = models.CharField(max_length=100, null=False)
    warehouse = models.CharField(max_length=100, default="Not Specified")


class Feedback(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    ph_no = models.CharField(max_length=12)
    email = models.CharField(max_length=50)
    comments = models.TextField()
