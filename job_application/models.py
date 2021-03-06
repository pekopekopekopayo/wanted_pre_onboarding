from django.db import models
from user.models import User
from job_posting.models import JobPosting

# Create your models here.
class JobApplication(models.Model):
    user = models.ForeignKey(User, related_name='job_applications', on_delete=models.CASCADE, null=False)
    job_posting = models.ForeignKey(JobPosting, related_name='job_applications', on_delete=models.CASCADE, null=False)