from django.contrib import admin

from .models import Degerler

class DegerlerAdmin(admin.ModelAdmin):
    list_display = ('id', 'hesaplamatarihi', 'debi', 'gktsicakligi', 'gbnemi', 'cktsicakligi', 'cbnemi', 'kapasite', 'etuketimi')

admin.site.register(Degerler,DegerlerAdmin)
