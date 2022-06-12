
from django.db import models
from company.models import Company

class JobPosting(models.Model):

    company = models.ForeignKey(Company, related_name='company', on_delete=models.CASCADE)
    position = models.CharField(max_length=50, null=False, blank=False)
    content = models.TextField(null=False, blank=False)
    compensation = models.IntegerField(null=False, blank=False)
    skill = models.CharField(max_length=50, null=False, blank=False)
# Create your models here.
