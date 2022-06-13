from django.urls import path
from .views import JobPostingView


urlpatterns = [
    path('', JobPostingView.as_view()),
    path('<int:id>', JobPostingView.as_view()),
    path('detail/<int:id>', JobPostingView.detail),
    path('search/', JobPostingView.search),
]