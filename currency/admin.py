from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.currency)
class WeatherAdmin(admin.ModelAdmin):
    pass