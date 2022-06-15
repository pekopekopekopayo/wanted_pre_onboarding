from django import forms

from .models import JobPosting

class JobPostingForm(forms.ModelForm):
    class Meta:
        model = JobPosting
        fields = '__all__'


class JobPostingUpdateForm(forms.ModelForm):
    
    class Meta:
        model = JobPosting
        exclude = ['id', 'company']

