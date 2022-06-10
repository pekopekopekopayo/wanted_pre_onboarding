from django.forms import ValidationError
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from user.models import User
from .models import JobApplication, JobPosting

class JobApplicationView(APIView):

    def post(self, request, format=None):
        user_id, job_posting_id = request.data['user_id'], request.data['job_posting_id']
        user, job_posting = User.objects.filter(id=user_id).first(), JobPosting.objects.filter(id=job_posting_id).first()
        try:
            job_application = JobApplication(user=user, job_posting=job_posting)
            job_application.full_clean()
            job_application.save()
            return Response(status=status.HTTP_201_CREATED)
        except ValidationError as e:
            return Response(e, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({'error': '알 수 없는 에러가 발생하였습니다.'}, status=status.HTTP_500_BAD_REQUEST)


