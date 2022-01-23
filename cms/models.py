from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Grad(models.Model):
    ime_grada = models.CharField(max_length=20)

    def __str__(self):
        return self.ime_grada

class Kategorija(models.Model):
    ime_kategorije = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.ime_kategorije

class Oglas(models.Model):
    autor = models.ForeignKey(User, models.CASCADE)
    datum_objave = models.DateField(auto_now=True)
    ime_proizvoda = models.CharField(max_length=50)
    detalji = models.TextField(null=True)
    kategorija = models.ForeignKey(Kategorija, models.SET_NULL, null=True)
    cijena = models.DecimalField(decimal_places=2, max_digits=5)
    grad = models.ForeignKey(Grad, models.CASCADE)

    def __str__(self):
        return self.ime_proizvoda

class Komentar(models.Model):
    autor = models.ForeignKey(User, models.SET_NULL, null=True)
    oglas = models.ForeignKey(Oglas, models.CASCADE)
    sadrzaj = models.TextField()

    def __str__(self):
        return self.autor.username