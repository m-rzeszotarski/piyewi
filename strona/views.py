from django.shortcuts import render
from django.utils import timezone
from .models import Yerba

def glowna(request):
    return render(request, 'strona/glowna.html')

def yerba_list(request):
    yerbas = Yerba.objects.all()
    return render(request, 'strona/yerba_list.html', {'yerbas': yerbas})

# Create your views here.