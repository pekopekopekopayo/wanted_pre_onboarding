from django.db import models

class Company(models.Model):
    
    name = models.CharField(max_length=50, unique=True, null=False, blank=False)
    country = models.CharField(max_length=50, null=False, blank=False)
    city = models.CharField(max_length=50, null=False, blank=False)

# Create your models here.
