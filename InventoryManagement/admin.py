from django.contrib import admin
from .models import categorydb, AddRecord, Feedback
# Register your models here.
admin.site.register(categorydb)
admin.site.register(AddRecord)
admin.site.register(Feedback)
