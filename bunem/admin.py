from django.contrib import admin

from .models import Degerler
from .models import Hygrometric

class DegerlerAdmin(admin.ModelAdmin):
    list_display = ('id', 'hesaplamatarihi', 'Airflow', 'GKT_Sicakligi', 'GB_Nemi', 'CKT_Sicakligi', 'CB_Nemi')

class HygrometricAdmin(admin.ModelAdmin):
    list_display = ('id', 'DB_Temp', 'R_Humidity', 'M_Content', 'S_Volume', 'S_Enthalpy', 'S_Moisture', 'EO_Dryair', 'SV_Press')

admin.site.register(Degerler,DegerlerAdmin)
admin.site.register(Hygrometric,HygrometricAdmin)
