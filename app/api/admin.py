from django.contrib import admin
from . import models

class WineAdmin(admin.ModelAdmin):
    model=models.Wine

admin.site.register(models.Wine, WineAdmin)
