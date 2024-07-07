from django.shortcuts import render

# Create your views here.

def anasayfayap(request):
    return render(request, 'bunem/anasayfa.html', {})
