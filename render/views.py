from django.shortcuts import render
from render.models import WeatherReport
import datetime



# Create your views here.
def index(request):
    return render(request, 'render/index.html', {})

def report(request):
    wtype= request.GET['weather_type']
    now = datetime.datetime.now()
    w = WeatherReport(Reporting_Time=now, Reported_Weather_Type=wtype)
    w.save()
    return render(request,'render/report.html')