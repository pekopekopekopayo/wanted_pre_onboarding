from django.forms import ValidationError
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from company.models import Company
from .models import JobPosting
from .serializers import JobPostingSerializer

class JobPostView(APIView):

    def get(self, request, format=None):
        queryset = JobPosting.objects.all()
        serializer  = JobPostingSerializer(queryset, many=True)
        return Response(serializer.data) 

    def post(self, request, format=None):
        data = dict(request.data)
        data['company'] = Company.objects.filter(id=data['company']).first()
        try:
            j_p = JobPosting(**data)
            j_p.full_clean()
            j_p.save()
            serializer  = JobPostingSerializer(j_p)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except ValidationError as e:
            return Response(e, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({'error': '예상치 못한 에러'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request, format=None):
        data = dict(request.data)
        try:
            j_p = JobPosting.objects.get(id=data.pop('id')) 
            j_p.attr_update(data)
            j_p.full_clean()
            j_p.save()
            serializer  = JobPostingSerializer(j_p)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except ValidationError as e:
            return Response(e, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({'error': '예상치 못한 에러'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def delete(self, request, format=None):
        try:
            j_p = JobPosting.objects.get(id=request.GET['id']) 
            j_p.delete()
            serializer  = JobPostingSerializer(JobPosting.objects.all(), many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except JobPosting.DoesNotExist as e:
            return Response(e, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({'error': '예상치 못한 에러'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
