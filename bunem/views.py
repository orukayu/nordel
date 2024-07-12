from django.shortcuts import render, redirect
from .forms import DegerlerForm
from .models import Hygrometric
from decimal import Decimal

# Create your views here.

def anasayfayap(request):
    s_moisture_value = None
    moisture_content = None

    if request.method == 'POST':
        form = DegerlerForm(request.POST)
        if form.is_valid():
            gkt_sicakligi = form.cleaned_data['GKT_Sicakligi']
            gb_nemi = form.cleaned_data['GB_Nemi']
            
            hygrometric_record = Hygrometric.objects.get(DB_Temp=gkt_sicakligi)
            s_moisture_value = hygrometric_record.S_Moisture * Decimal(1000)

            moisture_content = gb_nemi * float(s_moisture_value) * 0.01

            form.save()
    else:
        form = DegerlerForm()

    return render(request, 'bunem/anasayfa.html', {'form': form, 's_moisture_value': s_moisture_value, 'moisture_content': moisture_content})
