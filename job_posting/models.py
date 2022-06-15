
from django.db import models
from company.models import Company

class JobPosting(models.Model):

    def attr_update(self, dic):
        for k in dic.keys():
            if hasattr(self, k):
                setattr(self, k, dic[k])

    company = models.ForeignKey(Company, related_name='company', on_delete=models.CASCADE)
    position = models.CharField(max_length=50, null=False, blank=False)
    content = models.TextField(null=False, blank=False)
    compensation = models.IntegerField(null=False, blank=False, default=0)
    skill = models.CharField(max_length=50, null=False, blank=True)

# Create your models here.
