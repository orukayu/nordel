from django.urls import path
from . import views

urlpatterns = [
    path('', views.anasayfayap, name='anasayfaurl'),
]