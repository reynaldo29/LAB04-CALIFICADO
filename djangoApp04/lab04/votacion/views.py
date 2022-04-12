from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


from .models import Region, Candidato

def index(request):
    regiones=Region.objects.all()
    context = {'regiones':regiones}
    return render(request,'index.html',context)

def candidatos(request,region_id):
    regionex = get_object_or_404(Region,pk =region_id)
    return render(request,'candidatos.html',{'regionex':regionex})

def detalles(request,region_id):
    candidato = get_object_or_404(Candidato,pk =region_id)
    return render(request,'detalles.html',{'candidato':candidato})
# Create your views here.
