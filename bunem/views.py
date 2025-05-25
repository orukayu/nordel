from django.shortcuts import render, redirect
from django.http import JsonResponse
from .forms import DegerlerForm
from .models import Hygrometric
from decimal import Decimal, ROUND_HALF_UP

# Create your views here.

def anasayfayap(request):
    s_moisture_value = 0
    moisture_content = 0
    saturation_vapour_pressure = 0
    specific_enthalpy_dry_air = 0
    specific_enthalpy = 0
    specific_volume = 0
    c_moisture_content = 0
    c_specific_volume = 0
    c_specific_enthalpy = 0
    c_s_moisture_value = 0
    c_specific_enthalpy_dry_air = 0
    c_saturation_vapour_pressure = 0
    form = DegerlerForm()

    context = {
        'form': form,
        's_moisture_value': s_moisture_value,
        'moisture_content': moisture_content,
        'saturation_vapour_pressure': saturation_vapour_pressure,
        'specific_enthalpy_dry_air': specific_enthalpy_dry_air,
        'specific_enthalpy': specific_enthalpy,
        'specific_volume': specific_volume,
        'c_moisture_content': c_moisture_content,
        'c_specific_volume': c_specific_volume,
        'c_specific_enthalpy': c_specific_enthalpy,
        'c_s_moisture_value': c_s_moisture_value,
        'c_specific_enthalpy_dry_air': c_specific_enthalpy_dry_air,
        'c_saturation_vapour_pressure': c_saturation_vapour_pressure,
    }
    return render(request, 'bunem/ana.html', context)


def hesaplama_ajax(request):
    if request.method == 'POST' and request.headers.get('x-requested-with') == 'XMLHttpRequest':
        form = DegerlerForm(request.POST)
        if form.is_valid():
            # Formdan gelen verileri Decimal ve uygun formatla al
            gkt_sicakligi = form.cleaned_data['GKT_Sicakligi'].quantize(Decimal(0.00), rounding=ROUND_HALF_UP)
            gb_nemi = form.cleaned_data['GB_Nemi']
            ckt_sicakligi = form.cleaned_data['CKT_Sicakligi'].quantize(Decimal(0.00), rounding=ROUND_HALF_UP)
            cb_nemi = form.cleaned_data['CB_Nemi']

            # Veritabanındaki giris sıcaklık değeriyle yaklaşık eşleşme yap
            hygrometric_record = (
                Hygrometric.objects
                .filter(DB_Temp__gte=gkt_sicakligi - Decimal(0.01), DB_Temp__lte=gkt_sicakligi + Decimal(0.01))
                .first()
            )

            # Veritabanındaki cikis sıcaklık değeriyle yaklaşık eşleşme yap
            c_hygrometric_record = (
                Hygrometric.objects
                .filter(DB_Temp__gte=ckt_sicakligi - Decimal(0.01), DB_Temp__lte=ckt_sicakligi + Decimal(0.01))
                .first()
            )

            if not hygrometric_record:
                return JsonResponse({'error': 'Hygrometric verisi bulunamadı.'}, status=404)

            if not c_hygrometric_record:
                return JsonResponse({'error': 'Hygrometric verisi bulunamadı.'}, status=404)

            # Giris Hesaplamalar
            s_moisture_value = hygrometric_record.S_Moisture * Decimal(1000)
            moisture_content = gb_nemi * s_moisture_value * Decimal("0.01")
            saturation_vapour_pressure = hygrometric_record.SV_Press
            specific_enthalpy_dry_air = hygrometric_record.EO_Dryair
            specific_enthalpy = (
                specific_enthalpy_dry_air +
                (s_moisture_value * gb_nemi / Decimal("100")) * Decimal("2.55")
            )
            specific_volume = (
                ((gkt_sicakligi + Decimal("273")) / Decimal("1013")) *
                (Decimal("2.87") + (Decimal("4.61") * s_moisture_value * gb_nemi / Decimal("100000")))
            )

            # Cikis Hesaplamalar
            c_s_moisture_value = c_hygrometric_record.S_Moisture * Decimal(1000)
            c_moisture_content = cb_nemi * c_s_moisture_value * Decimal("0.01")
            c_saturation_vapour_pressure = c_hygrometric_record.SV_Press
            c_specific_enthalpy_dry_air = c_hygrometric_record.EO_Dryair
            c_specific_enthalpy = (
                c_specific_enthalpy_dry_air +
                (c_s_moisture_value * cb_nemi / Decimal("100")) * Decimal("2.55")
            )
            c_specific_volume = (
                ((ckt_sicakligi + Decimal("273")) / Decimal("1013")) *
                (Decimal("2.87") + (Decimal("4.61") * c_s_moisture_value * cb_nemi / Decimal("100000")))
            )

            return JsonResponse({
                'moisture_content': float(moisture_content),
                'specific_volume': float(specific_volume),
                'specific_enthalpy': float(specific_enthalpy),
                's_moisture_value': float(s_moisture_value),
                'specific_enthalpy_dry_air': float(specific_enthalpy_dry_air),
                'saturation_vapour_pressure': float(saturation_vapour_pressure),
                'c_moisture_content': float(c_moisture_content),
                'c_specific_volume': float(c_specific_volume),
                'c_specific_enthalpy': float(c_specific_enthalpy),
                'c_s_moisture_value': float(c_s_moisture_value),
                'c_specific_enthalpy_dry_air': float(c_specific_enthalpy_dry_air),
                'c_saturation_vapour_pressure': float(c_saturation_vapour_pressure),
            })
        else:
            return JsonResponse({'error': 'Form geçersiz.'}, status=400)

    return JsonResponse({'error': 'Geçersiz istek.'}, status=400)
