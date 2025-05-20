from django.shortcuts import render, redirect
from django.http import JsonResponse
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

def hesaplama_ajax(request):
    if request.method == 'POST' and request.headers.get('x-requested-with') == 'XMLHttpRequest':
        form = DegerlerForm(request.POST)
        if form.is_valid():
            gkt_sicakligi = form.cleaned_data['GKT_Sicakligi']
            gb_nemi = form.cleaned_data['GB_Nemi']

            try:
                hygrometric_record = Hygrometric.objects.get(DB_Temp=gkt_sicakligi)
            except Hygrometric.DoesNotExist:
                return JsonResponse({'error': 'Hygrometric verisi bulunamadı.'}, status=404)

            s_moisture_value = hygrometric_record.S_Moisture * Decimal(1000)
            moisture_content = gb_nemi * float(s_moisture_value) * 0.01
            vapour_pressure = hygrometric_record.SV_Press
            specific_enthalpy_dry_air = hygrometric_record.EO_Dryair
            specific_enthalpy = (
                specific_enthalpy_dry_air + 
                (Decimal(s_moisture_value) * Decimal(gb_nemi) / Decimal(100)) * Decimal(2.55)
            )
            specific_volume = (
                ((gkt_sicakligi + Decimal(273)) / Decimal(1013)) *
                (Decimal(2.87) + (Decimal(4.61) * Decimal(s_moisture_value) * Decimal(gb_nemi) / Decimal(100000)))
            )

            return JsonResponse({
                'moisture_content': float(moisture_content),
                'specific_volume': float(specific_volume),
                'specific_enthalpy': float(specific_enthalpy),
                's_moisture_value': float(s_moisture_value),
                'specific_enthalpy_dry_air': float(specific_enthalpy_dry_air),
                'vapour_pressure': float(vapour_pressure),
            })
        else:
            return JsonResponse({'error': 'Form geçersiz.'}, status=400)

    return JsonResponse({'error': 'Geçersiz istek.'}, status=400)
