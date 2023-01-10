from django.shortcuts import render
from django.http import HttpResponse

from .models import Mascota
from django.shortcuts import render
# Create your views here.

def Data(request):
    data = list(Mascota.objects.values())
    # return HttpResponse(data) 
    return render(request, "data.html", {
            'data' : data
        })
    
def Reports(request):
    return render(request, 'report.html')    