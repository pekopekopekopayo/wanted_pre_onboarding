from tkinter import E
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from job_posting.forms import JobPostingForm, JobPostingUpdateForm
from .models import JobPosting
from .serializers import JobPostingDetailSerializer, JobPostingSerializer
from rest_framework.decorators import api_view

class JobPostingView(APIView):

    def get(self, request, format=None):
        queryset = JobPosting.objects.all()
        serializer  = JobPostingSerializer(queryset, many=True)
        return Response(serializer.data) 

    def post(self, request, format=None):
        j_p_form = JobPostingForm(request.data)
        if j_p_form.is_valid():
            j_p = j_p_form.save()
            serializer  = JobPostingSerializer(j_p)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(j_p_form.errors.as_data(), status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, format=None):
        j_p = JobPosting.objects.get(id=request.data['id']) 
        j_p_form = JobPostingUpdateForm(request.data, instance=j_p)
        if j_p_form.is_valid():
            j_p = j_p_form.save()
            serializer = JobPostingSerializer(j_p)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(j_p_form.errors.as_data(), status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, id):
        try:
            j_p = JobPosting.objects.get(id=id) 
            j_p.delete()
            return Response(status=status.HTTP_200_OK)
        except JobPosting.DoesNotExist as e:
            return Response({'error': e}, status=status.HTTP_400_BAD_REQUEST)


    @api_view(('GET',))
    def detail(request, id):
        try:
            j_p = JobPosting.objects.get(id=id)
            serializer = JobPostingDetailSerializer(j_p)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except JobPosting.DoesNotExist as e:
            return Response(e, status=status.HTTP_400_BAD_REQUEST)

    @api_view(('GET',))
    def search(request):
        j_p = JobPosting.objects.order_by('id').all()
        if company_name := request.GET.get('company_name'): j_p = j_p.filter(company__name=company_name)
        if company_country := request.GET.get('company_country'): j_p = j_p.filter(company__country=company_country)
        if company_city := request.GET.get('company_city'): j_p = j_p.filter(company__city__icontains=company_city)
        if position := request.GET.get('position'): j_p = j_p.filter(position__icontains=position)
        if compensation := request.GET.get('compensation'): j_p = j_p.filter(compensation__icontains=compensation)
        if skill := request.GET.get('skill'): 
            j_p = j_p.filter(skill=skill)
        serializer = JobPostingSerializer(j_p, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)