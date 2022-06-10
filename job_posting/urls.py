from django.urls import path
from .views import JobPostView


urlpatterns = [
    path('', JobPostView.as_view()),
    path('<int:id>/', JobPostView.detail),
    path('search/', JobPostView.search),
]