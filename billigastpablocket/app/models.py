from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Listing(models.Model):
	name = models.CharField(null = True, max_length=1000)
	price = models.IntegerField(null = True)
	category = models.CharField(null = True, max_length=500)
	location = models.CharField(null = True, max_length=500)
	downloaded_at = models.DateTimeField(auto_now_add=True)