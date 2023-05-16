from django.contrib import admin

from .models import WeatherInfo,CropSeeding
# Register your models here.

admin.site.register(WeatherInfo)
admin.site.register(CropSeeding)