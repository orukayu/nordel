from django import forms
from .models import Degerler

class DegerlerForm(forms.ModelForm):
    class Meta:
        model = Degerler
        fields = ['Airflow', 'GKT_Sicakligi', 'GB_Nemi', 'CKT_Sicakligi', 'CB_Nemi']
        labels = {'Airflow' : 'Hava Debisi', 'GKT_Sicakligi' : 'GKT Sıcaklığı', 'GB_Nemi' : 'GB Nemi', 'CKT_Sicakligi' : 'ÇKT Sıcaklığı', 'CB_Nemi' : 'ÇB Nemi'}