from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('oglasi/', views.svi_oglasi, name='svi_oglasi'),
    path('oglasi/<int:id>', views.oglas_detalji, name='oglas_detalji'),
    path('kategorije/', views.kategorije, name='kategorije'),
    path('kategorije/<int:id>/', views.oglasi_iz_kategorije, name='oglasi_iz_kategorije'),
]