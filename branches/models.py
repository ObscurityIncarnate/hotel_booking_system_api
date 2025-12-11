from django.db import models
from django.contrib.postgres.fields import ArrayField
# Create your models here.
class Branch(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description =  models.CharField(max_length=3000)
    address =  models.CharField(max_length=300)
    longitude = models.DecimalField(max_digits=10, decimal_places=6,null=True, blank= True)
    latitude = models.DecimalField(max_digits=10, decimal_places=6, null=True, blank=True)
    images = ArrayField(
        models.URLField(),
        size=8,
        default=list
    ) 
    