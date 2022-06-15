from django.test import TestCase
from company.forms import CompanyForm
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
        user = UserForm({'name': '일승수', 'address': '울릉도 동남쪽', 'phone_number': '01012345678'}).save()
        company = CompanyForm({'name': '회사0', 'country': '한국', 'city': '서울'}).save()
        JobPostingForm({'company': company, 'position': '테스트개발',
                        'compensation': '200', 'content': '우리는 발전을...',
                        'skill': 'rb'}).save()
        JobPostingForm({'company': company, 'position': '백엔드개발',
                        'compensation': '200', 'content': '우리는 발전을...',
                        'skill': 'rb'}).save()
        j_p = JobPostingForm({'company': company, 'position': '프론트개발',
                    'compensation': '200', 'content': '우리는 발전을...',
                    'skill': 'rb'}).save()
        JobApplicationForm({'user':user, 'job_posting': j_p}).save()

    def test_empty_user(self):
        self.basic_validate_case(user=None)
        self.basic_validate_case(user=User())

    def test_empty_job_posting(self):
        self.basic_validate_case(job_posting=None)
        self.basic_validate_case(job_posting=JobPosting())

    def test_create_job_application(self):
        self.basic_success_case(user=User.objects.first(), job_posting=JobPosting.objects.first())

    def test_is_unique(self): 
        user = User.objects.first()
        j_p1, j_p2 = JobPosting.objects.all()[:2]
        self.basic_success_case(user=user, job_posting=j_p1, save=True)
        self.basic_validate_case(user=user, job_posting=j_p1)
        self.basic_success_case(user=user, job_posting=j_p2)
        another_user = UserForm({'name': '이승수', 'address': '울릉도 동남쪽', 'phone_number': '01012345677'}).save()
        self.basic_success_case(user=another_user, job_posting=j_p1)

    def test_on_delete_user(self):
        user = User.objects.first()
        j_a = user.job_applications.first()
        user.delete()
        if JobApplication.objects.filter(id=j_a.id).first():
            self.fail('유저가 삭제되었지만 지원정보가 존재합니다')

    def test_on_delete_job_posting(self):        
        user = User.objects.first()
        j_a = user.job_applications.first()
        j_p = j_a.job_posting
        j_p.delete()
        if JobApplication.objects.filter(id=j_a.id).first():
            self.fail('채용공고가 삭제되었지만 지원정보가 존재합니다')

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