from django.shortcuts import render
from .models import Profissional

# Create your views here.

def index(request):
    return render(request, 'CMFapp/index.html')

def listar_profissionais(request):
    profissionais = Profissional.objects.all()
    return render(request, 'CMFapp/listar_profissionais.html', {'profissionais': profissionais})
