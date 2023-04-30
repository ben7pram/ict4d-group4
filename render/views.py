from django.shortcuts import render
from render.models import WeatherReport
import datetime



# Create your views here.
def index(request):
    return render(request, 'render/index.html', {})

def report(request):
    print("inside report----")
    wtype= request.GET['weather_type']
    print("wtype=",wtype)
    now = datetime.datetime.now()
    print("now=",now)
    w = WeatherReport(Reporting_Time=now, Reported_Weather_Type=wtype)
    print("w=",w)
    w.save()
    return render(request,'render/report.html')