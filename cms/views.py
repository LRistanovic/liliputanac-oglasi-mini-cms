from django.shortcuts import render
from django.http import HttpResponseRedirect
from . import models, forms

def homepage(request):
    return render(request, 'cms/home.html', {})

def svi_oglasi(request):
    oglasi = models.Oglas.objects.all()
    print(request.user)
    return render(request, 'cms/oglasi.html', { 'oglasi': oglasi })

def oglas_detalji(request, id):
    oglas = models.Oglas.objects.get(id=id)

    if request.method == 'POST':
        form = forms.KomentarForm(request.POST)
        if form.is_valid():
            novi_komentar = form.save(commit=False)
            novi_komentar.autor = request.user
            novi_komentar.oglas = oglas
            novi_komentar.save()
            return HttpResponseRedirect(f'/oglasi/{id}/')
    else:
        form = forms.KomentarForm()

    return render(request, 'cms/oglas_detalji.html', { 'oglas': oglas, 'form': form })

def oglasi_iz_kategorije(request, id):
    oglasi = models.Oglas.objects.filter(kategorija__id=id)
    return render(request, 'cms/oglasi.html', { 'oglasi': oglasi })

def novi_oglas(request):
    if request.method == 'POST':
        form = forms.OglasForm(request.POST)
        if form.is_valid():
            novi_oglas = form.save(commit=False)
            novi_oglas.autor = request.user
            novi_oglas.save()
            return HttpResponseRedirect('/oglasi/')
    else:
        form = forms.OglasForm()
    return render(request, 'cms/novi_oglas.html', { 'form': form })

def kategorije(request):
    kategorije = models.Kategorija.objects.all()
    return render(request, 'cms/kategorije.html', { 'kategorije': kategorije })
