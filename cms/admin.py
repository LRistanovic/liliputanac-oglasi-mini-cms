from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.Oglas)
admin.site.register(models.Komentar)
admin.site.register(models.Kategorija)
admin.site.register(models.Grad)