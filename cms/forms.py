from django.forms import ModelForm
from . import models

class OglasForm(ModelForm):
    class Meta:
        model = models.Oglas
        exclude = ['autor', 'datum_objave']

class KomentarForm(ModelForm):
    class Meta:
        model = models.Komentar
        fields = ['sadrzaj']