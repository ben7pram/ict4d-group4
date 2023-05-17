from django.shortcuts import render
from render.models import WeatherReport,WeatherInfo,CropSeeding
import datetime



# Create your views here.
def index(request):
    weather_data = WeatherInfo.objects.all()
    crop_data = CropSeeding.objects.all()
    args = {}
    args['weather_data'] = weather_data
    args['crop_data']=crop_data
    return render(request, 'render/index.html', args)

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
    w_info = WeatherInfo.objects.get(Day=period)
    wtype = w_info.Weather_Type
    args = {}
    args['wtype'] = wtype
    return render(request,'render/weather-info.html',args)

def crop_info(request):
    crop= request.GET['croptype'] 
    c_info = CropSeeding.objects.get(Crop_Name=crop)
    seed_period = c_info.Seeding_Day
    args = {}
    args['crop']=crop
    args['seed_period'] = seed_period
    return render(request,'render/crop-info.html',args)

def crop_info_today(request):
   print("####################crops_info_today") 
    crop_data= CropSeeding.objects.get(Seeding_Day='Today')
    print("####################crops_data",crop_data)
    crops_today=''
    for crop in crop_data:
        crops_today+=crop.Crop_Name
        print("--------crops_today=",crops_today)
    args = {}
    args['crops_today'] = crops_today
    return render(request,'render/crop-info-today.html',args)


def update_weather_type(request, id):
    if request.method == 'POST':
        weather_type = request.POST.get('weather_type')
        WeatherInfo.objects.filter(id=id).update(Weather_Type=weather_type)
    #return redirect('index')
    return index(request)

def update_seed_day(request, id):
    if request.method == 'POST':
        seeding_day = request.POST.get('seeding_day')
        CropSeeding.objects.filter(id=id).update(Seeding_Day=seeding_day)
    #return redirect('index')
    return index(request)