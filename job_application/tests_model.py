from django.forms import ValidationError
from django.test import TestCase
from company.models import Company

from job_application.models import JobApplication
from job_posting.models import JobPosting
from user.models import User

# Create your tests here.
class JobApplicationModelTest(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        User.objects.create(name='일승수', address='울릉도 동남쪽', phone_number='01012345678')
        company = Company.objects.create(name='회사0', country='한국', city='서울')
        JobPosting.objects.create(company=company, position='테스트개발',
                                                compensation='200', content='우리는 발전을...',
                                                skill='rb')
        JobPosting.objects.create(company=company, position='백엔드개발',
                                                compensation='200', content='우리는 발전을...',
                                                skill='rb')
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
        self.basic_success_case(user=user, job_posting=j_p1)

        '''한 유저가 똑같은 채용공고 지원 '''
        self.basic_validate_case(user=user, job_posting=j_p1)

        '''똑같은 회사에 다른 채용공고 지원 가능'''
        self.basic_success_case(user=user, job_posting=j_p2)
     

    def basic_success_case(self, user=User.objects.first(), job_posting=JobPosting.objects.first()):
        j_a = JobApplication(user=user, job_posting=job_posting)
        try:
            j_a.full_clean()
            j_a.save()
        except ValidationError as e:
            self.fail(e)
        except:
            self.fail('의도치 못한 오류')

    def basic_validate_case(self, user=User.objects.first(), job_posting=JobPosting.objects.first()):
        j_a = JobApplication(user=user, job_posting=job_posting)
        try:
            j_a.full_clean()
            j_a.save()
        except ValidationError as e:
            return
        except:
            self.fail('의도치 못한 오류')
        self.fail(e)