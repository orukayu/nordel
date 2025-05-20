from django.urls import path
from . import views

urlpatterns = [
    path('', views.anasayfayap, name='anasayfayap'),
    path('hesaplama/', views.hesaplama_ajax, name='hesaplama_ajax'),
]