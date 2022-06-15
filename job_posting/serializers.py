from rest_framework import  serializers
from .models import JobPosting 

class JobPostingSerializer(serializers.ModelSerializer):
    company_name = serializers.StringRelatedField(source='company.name')
    company_country = serializers.StringRelatedField(source='company.country')
    company_city = serializers.StringRelatedField(source='company.city')

    class Meta:
        model = JobPosting
        fields = ('id', 'company_name','company_country', 'company_city', 'position', 'compensation', 'skill')