from django.forms import ValidationError
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from job_application.forms import JobApplicationForm
from user.models import User
from .models import JobApplication, JobPosting

class JobApplicationView(APIView):

    def post(self, request, format=None):
        j_a_form = JobApplicationForm(request.data)
        if j_a_form.is_valid():
            j_a_form.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(j_a_form.errors.as_data(), status=status.HTTP_400_BAD_REQUEST)