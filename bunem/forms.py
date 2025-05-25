from django import forms
from .models import Degerler

class DegerlerForm(forms.ModelForm):
    class Meta:
        model = Degerler
        fields = ['Airflow', 'GKT_Sicakligi', 'GB_Nemi', 'CKT_Sicakligi', 'CB_Nemi']
        labels = {
            'Airflow': 'Hava Debisi',
            'GKT_Sicakligi': 'GKT Sıcaklığı',
            'GB_Nemi': 'GB Nemi',
            'CKT_Sicakligi': 'ÇKT Sıcaklığı',
            'CB_Nemi': 'ÇB Nemi'
        }
        widgets = {
            'Airflow': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'GKT_Sicakligi': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'GB_Nemi': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'CKT_Sicakligi': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'CB_Nemi': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
        }

    def __init__(self, *args, **kwargs):
        super(DegerlerForm, self).__init__(*args, **kwargs)
        self.fields['Airflow'].initial = 3.62
        self.fields['GKT_Sicakligi'].initial = 23.65
        self.fields['GB_Nemi'].initial = 80.79
        self.fields['CKT_Sicakligi'].initial = 14.83
        self.fields['CB_Nemi'].initial = 95.04