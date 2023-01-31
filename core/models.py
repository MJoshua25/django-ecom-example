from django.db import models


# Create your models here.

class Standard_model(models.Model):
	statut = models.BooleanField(default=True)
	date_add = models.DateTimeField(auto_now_add=True)
	date_upd = models.DateTimeField(auto_now=True)

	class Meta:
		abstract = True
