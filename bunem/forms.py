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
            'Airflow': forms.TextInput(attrs={'class': 'form-control'}),
            'GKT_Sicakligi': forms.TextInput(attrs={'class': 'form-control'}),
            'GB_Nemi': forms.TextInput(attrs={'class': 'form-control'}),
            'CKT_Sicakligi': forms.TextInput(attrs={'class': 'form-control'}),
            'CB_Nemi': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(DegerlerForm, self).__init__(*args, **kwargs)
        self.fields['Airflow'].initial = 3.62
        self.fields['GKT_Sicakligi'].initial = 23
        self.fields['GB_Nemi'].initial = 80
        self.fields['CKT_Sicakligi'].initial = 14.8
        self.fields['CB_Nemi'].initial = 95