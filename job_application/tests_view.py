from django.test import RequestFactory, TestCase
from company.forms import CompanyForm
from company.models import Company

from job_application.models import JobApplication
from job_application.views import JobApplicationView
from job_posting.forms import JobPostingForm
from job_posting.models import JobPosting
from user.forms import UserForm
from user.models import User

class JobApplicationAPIViewTests(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        UserForm({'name': '이승수', 'address': '울릉도 동남쪽', 'phone_number': '01012345678'}).save()
        company= CompanyForm({'name': '회사0', 'country': '한국', 'city': '서울'}).save()
        JobPostingForm({'company': company, 'position': 'back end', 'content': '우리회사는....',
                                    'compensation': 200, 'skill': 'rb'}).save()

    def test_post_api(self):
        factory = RequestFactory()
        view = JobApplicationView.as_view()
        url = "http://127.0.0.1:8000/job_application"
        request = factory.post(url, data={'user': User.objects.first().id, 'job_posting': JobPosting.objects.first().id})
        response = view(request)
        if response.status_code != 201:
            self.fail('status_code가 정상적이지 않습니다.')
        if len(User.objects.all()) != 1:
            self.fail('데이터가 생성되지 않았습니다.')
        
        request = factory.post(url, data={'user': User.objects.first().id, 'job_posting': JobPosting.objects.first().id})
        response = view(request)
        if response.status_code != 400:
            self.fail('status_code가 정상적이지 않습니다.')
        if len(User.objects.all()) != 1:
            self.fail('데이터가 생성되었습니다.')
