from django.shortcuts import render
from . import models

def homepage(request):
    return render(request, 'cms/home.html', {})

def svi_oglasi(request):
    oglasi = models.Oglas.objects.all()
    return render(request, 'cms/oglasi.html', { 'oglasi': oglasi })

def oglas_detalji(request, id):
    oglas = models.Oglas.objects.get(id=id)
    return render(request, 'cms/oglas_detalji.html', { 'oglas': oglas })

def oglasi_iz_kategorije(request, id):
    oglasi = models.Oglas.objects.filter(kategorija__id=id)
    return render(request, 'cms/oglasi.html', { 'oglasi': oglasi })

def kategorije(request):
    kategorije = models.Kategorija.objects.all()
    return render(request, 'cms/kategorije.html', { 'kategorije': kategorije })
