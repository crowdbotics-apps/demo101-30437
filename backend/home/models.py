from django.conf import settings
from django.db import models
class FavoriteCars(models.Model):
    'Generated Model'
    make = models.CharField(max_length=256,)
    model = models.CharField(max_length=256,)
    year = models.BigIntegerField()
