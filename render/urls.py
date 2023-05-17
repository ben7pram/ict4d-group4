from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('report/', views.report, name='report'), 
    path('report_fr/', views.report_fr, name='report_fr'),
    path('weather_info/',views.weather_info,name='weather_info'),
    path('crop_info/',views.crop_info,name='crop_info'),
    path('crop_info_today/',views.crop_info_today,name='crop_info_today'),
    path('update_weather_type/<int:id>/', views.update_weather_type, name='update_weather_type'),
    path('update_seed_day/<int:id>/', views.update_seed_day, name='update_seed_day'),
]
