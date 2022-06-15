from django import forms

from .models import JobApplication

class JobApplicationForm(forms.ModelForm):

    class Meta:
        model = JobApplication
        fields = '__all__'

    def is_valid(self):
        return super().is_valid() and self.is_unique(self.cleaned_data)

    
    def is_unique(self, data):
        if JobApplication.objects.filter(user=data['user'], job_posting=data['job_posting']).first():
            self.add_error('job_posting', 'user is more have than one record')
            return False
        return True
        