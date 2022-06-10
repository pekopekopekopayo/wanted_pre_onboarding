from rest_framework import  serializers
from django.db.models import Q
from .models import JobPosting 

class JobPostingSerializer(serializers.ModelSerializer):
    company_name = serializers.StringRelatedField(source='company.name')
    company_country = serializers.StringRelatedField(source='company.country')
    company_city = serializers.StringRelatedField(source='company.city')

    class Meta:
        model = JobPosting
        fields = ('id', 'company_name','company_country', 'company_city', 'position', 'compensation', 'skill')

class JobPostingDetailSerializer(serializers.ModelSerializer):
    company_name = serializers.StringRelatedField(source='company.name')
    company_country = serializers.StringRelatedField(source='company.country')
    company_city = serializers.StringRelatedField(source='company.city')
    anther_job_posting = serializers.SerializerMethodField()

    class Meta:
        model = JobPosting
        fields = ('id', 'company_name','company_country', 'company_city', 'position', 'compensation', 'skill', 'anther_job_posting')

    def get_anther_job_posting(self, obj):
        return JobPosting.objects.filter(~Q(id=obj.id), company=obj.company).values_list('id', flat=True)

