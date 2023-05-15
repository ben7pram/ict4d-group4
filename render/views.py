from django.shortcuts import render
from render.models import WeatherReport,WeatherInfo,CropSeeding
import datetime



# Create your views here.
def index(request):
    return render(request, 'render/index.html', {})

def save(request):
    wtype= request.GET['weather_type']
    now = datetime.datetime.now()
    w = WeatherReport(Reporting_Time=now, Reported_Weather_Type=wtype)
    w.save()

def report(request):
    save(request)
    return render(request,'render/report-en.html')

def report_fr(request):
    save(request)
    return render(request,'render/report-fr.html')

def weather_info(request):
    period= request.GET['weather_period'] 
    w_info = WeatherInfo.objects.get(day=period)
    wtype = w_info.weather_type
    args = {}
    args['wtype'] = wtype
    return render(request,'render/weather-info.html',args)

def crop_info(request):
    return render(request,'render/crop-info.html')
