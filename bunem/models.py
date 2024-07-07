from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.


class Degerler(models.Model):
	debi = models.IntegerField()
	gktsicakligi = models.IntegerField()
	gbnemi = models.IntegerField()
	cktsicakligi = models.IntegerField()
	cbnemi = models.IntegerField()
	kapasite = models.IntegerField()
	etuketimi = models.IntegerField()
	hesaplamatarihi = models.DateTimeField(default=timezone.now)

	class Meta:
		ordering = ['hesaplamatarihi']  # Tablonun hangi başlığa göre sıralanacağını belirliyor

	def __str__(self):
		return str(self.hesaplamatarihi)
