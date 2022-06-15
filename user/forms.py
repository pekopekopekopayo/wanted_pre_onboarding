import re
from django import forms

from .models import User

class UserForm(forms.ModelForm):

    def is_valid(self):
        self.data['phone_number'] = re.sub('[-]', '', str(self.data['phone_number']))
        return super().is_valid()

    class Meta:
        model = User
        fields = '__all__'
