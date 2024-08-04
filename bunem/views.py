from django.shortcuts import render, redirect
from .forms import DegerlerForm
from .models import Hygrometric
from decimal import Decimal

# Create your views here.

def anasayfayap(request):
    s_moisture_value = 0
    moisture_content = 0
    vapour_pressure = 0
    specific_enthalpy_dry_air = 0
    specific_enthalpy = 0
    specific_volume = 0


    if request.method == 'POST':
        form = DegerlerForm(request.POST)
        if form.is_valid():
            gkt_sicakligi = form.cleaned_data['GKT_Sicakligi']
            C7 = gkt_sicakligi
            gb_nemi = form.cleaned_data['GB_Nemi']
            C8 = gb_nemi
            
            hygrometric_record = Hygrometric.objects.get(DB_Temp=gkt_sicakligi)
            s_moisture_value = hygrometric_record.S_Moisture * Decimal(1000)
            C15 = s_moisture_value

            moisture_content = gb_nemi * float(s_moisture_value) * 0.01
            C12 = moisture_content

            vapour_pressure = hygrometric_record.SV_Press
            C17 = vapour_pressure
            specific_enthalpy_dry_air = hygrometric_record.EO_Dryair
            C16 = specific_enthalpy_dry_air
            specific_enthalpy = (specific_enthalpy_dry_air + (Decimal(s_moisture_value) * Decimal(gb_nemi) / Decimal(100)) * Decimal(2.55))

            specific_volume = ((gkt_sicakligi + Decimal(273)) / Decimal(1013))*(Decimal(2.87)+(Decimal(4.61)*Decimal(s_moisture_value)*Decimal(gb_nemi)/Decimal(100000)))
            C13 = specific_volume

            form.save()
    else:
        form = DegerlerForm()

    context = {
        'form': form,
        's_moisture_value': s_moisture_value,
        'moisture_content': moisture_content,
        'vapour_pressure': vapour_pressure,
        'specific_enthalpy_dry_air': specific_enthalpy_dry_air,
        'specific_enthalpy': specific_enthalpy,
        'specific_volume': specific_volume,
    }
    return render(request, 'bunem/ana.html', context)
