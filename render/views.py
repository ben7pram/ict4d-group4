from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'render/index.html', {})

def report(request):
    return render(request,'render/report.html')