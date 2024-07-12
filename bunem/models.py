from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.


class Degerler(models.Model):
	Airflow = models.DecimalField(max_digits=4, decimal_places=2)
	GKT_Sicakligi = models.DecimalField(max_digits=4, decimal_places=1)
	GB_Nemi = models.IntegerField()
	CKT_Sicakligi = models.DecimalField(max_digits=4, decimal_places=1)
	CB_Nemi = models.IntegerField()
	hesaplamatarihi = models.DateTimeField(default=timezone.now)

	class Meta:
		ordering = ['hesaplamatarihi']  # Tablonun hangi başlığa göre sıralanacağını belirliyor

	def __str__(self):
		return str(self.hesaplamatarihi)

class Hygrometric(models.Model):
	DB_Temp = models.PositiveIntegerField()
	R_Humidity = models.PositiveIntegerField()
	M_Content = models.DecimalField(max_digits=15, decimal_places=9)
	S_Volume = models.DecimalField(max_digits=15, decimal_places=9)
	S_Enthalpy = models.DecimalField(max_digits=15, decimal_places=9)
	S_Moisture = models.DecimalField(max_digits=15, decimal_places=9)
	EO_Dryair = models.DecimalField(max_digits=15, decimal_places=9)
	SV_Press = models.DecimalField(max_digits=15, decimal_places=9)

	class Meta:
		ordering = ['DB_Temp']  # Tablonun hangi başlığa göre sıralanacağını belirliyor

	def __str__(self):
		return str(self.DB_Temp)

