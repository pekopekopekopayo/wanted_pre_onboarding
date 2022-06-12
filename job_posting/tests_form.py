from django.test import TestCase
from company.forms import CompanyForm
from company.models import Company
from job_posting.forms import JobPostingForm
from job_posting.models import JobPosting

# Create your tests here.
class JobPostingFormTest(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        company_form = CompanyForm({'name': '회사0', 'country': '한국', 'city': '서울'})
        company = company_form.save()
        j_p_form = JobPostingForm({'company': company, 'position': 'back end', 'content': '우리회사는....',
                                    'compensation': 200, 'skill': 'rb'})
        j_p_form.save()

    def test_create_job_posting(self):
        j_p = self.basic_success_case(company=Company.objects.first(), position='back end', content='우리회사는....', compensation=200, skill='rb', save=True)
        try:
            JobPosting.objects.get(id=j_p.id)
        except:
            self.fail('데이터가 생성되지 않았습니다.')

    def test_empty_company(self):
        self.basic_validate_case(company=None)
        self.basic_validate_case(company=Company())
    
    def test_empty_position(self):
        self.basic_validate_case(position=None)
        self.basic_validate_case(position='')
    
    def test_empty_content(self):
        self.basic_validate_case(content=None)
        self.basic_validate_case(content='')

    def test_empty_compensation(self):
        self.basic_validate_case(compensation=None)
        self.basic_validate_case(compensation='')

    def test_empty_skill(self):
        self.basic_validate_case(skill=None)
        self.basic_validate_case(skill='')

    def test_max_char_position(self):
        self.basic_validate_case(position='a'*51)
        self.basic_success_case(position='a'*50)

    def test_max_char_skill(self):
        self.basic_validate_case(skill='a'*51)
        self.basic_success_case(skill='a'*50)

    def test_on_delete_company(self):
        company = Company.objects.first()
        j_p = company.job_postings.first()
        company.delete()
        if JobPosting.objects.filter(id=j_p.id).first():
            self.fail('화사가 삭제되었지만 채용공고가 존재합니다.')
            
    def basic_success_case(self, company=None, position='back end', content='우리회사는....', compensation=200, skill='rb', save=False):
        if not company: company = Company.objects.first()

        j_p_form = JobPostingForm({'company': company, 'position': position, 'content': content,
                                    'compensation': compensation, 'skill': skill})
        if not j_p_form.is_valid():
            self.fail(j_p_form.errors.as_data())
        if save:
            return j_p_form.save()

    def basic_validate_case(self, company=Company.objects.first(), position='back end', content='우리회사는....', compensation=200, skill='rb'):
        j_p_form = JobPostingForm({'company': company, 'position': position, 'content': content,
                                    'compensation': compensation, 'skill': skill})
        if j_p_form.is_valid():
            self.fail('유효성 검사 성공')
            