from django.urls import path
from .views import JobPostView


urlpatterns = [
    path('job_posting/', JobPostView.as_view())
]