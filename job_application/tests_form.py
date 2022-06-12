from django.forms import ValidationError
from django.test import TestCase
from company.forms import CompanyForm
from company.models import Company
from job_application.forms import JobApplicationForm

from job_application.models import JobApplication
from job_posting.forms import JobPostingForm
from job_posting.models import JobPosting
from user.forms import UserForm
from user.models import User

# Create your tests here.
class JobApplicationFormTest(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        UserForm({'name': '일승수', 'address': '울릉도 동남쪽', 'phone_number': '01012345678'}).save()
        company = CompanyForm({'name': '회사0', 'country': '한국', 'city': '서울'}).save()
        JobPostingForm({'company': company, 'position': '테스트개발',
                        'compensation': '200', 'content': '우리는 발전을...',
                        'skill': 'rb'}).save()
        JobPostingForm({'company': company, 'position': '백엔드개발',
                        'compensation': '200', 'content': '우리는 발전을...',
                        'skill': 'rb'}).save()
                        
    def test_empty_user(self):
        self.basic_validate_case(user=None)
        self.basic_validate_case(user=User())

    def test_empty_job_posting(self):
        self.basic_validate_case(job_posting=None)
        self.basic_validate_case(job_posting=JobPosting())

    def test_create_job_application(self):
        self.basic_success_case(user=User.objects.first(), job_posting=JobPosting.objects.first())

    def test_user_job_posting_relation(self):
        user = User.objects.first()
        j_p1, j_p2 = JobPosting.objects.all()[:2]

        '''한 유저가 한 채용공고 지원 '''
        self.basic_success_case(user=user, job_posting=j_p1, save=True)

        '''한 유저가 똑같은 채용공고 지원 '''
        self.basic_validate_case(user=user, job_posting=j_p1)

        '''똑같은 회사에 다른 채용공고 지원 가능'''
        self.basic_success_case(user=user, job_posting=j_p2)
     

    def basic_success_case(self, user=User.objects.first(), job_posting=JobPosting.objects.first(), save=False):
        j_a = JobApplicationForm({'user':user, 'job_posting': job_posting})
        if not j_a.is_valid():    
            self.fail(j_a.errors.as_data())
        if save:
            j_a.save()

    def basic_validate_case(self, user=User.objects.first(), job_posting=JobPosting.objects.first()):
        j_a = JobApplicationForm({'user': user, 'job_posting': job_posting})
        if j_a.is_valid():    
            self.fail('데이터가 생성되었습니다.')