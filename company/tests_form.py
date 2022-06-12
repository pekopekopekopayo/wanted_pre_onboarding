from django.forms import ValidationError
from django.test import TestCase

from company.models import Company
from company.forms import CompanyForm

# Create your tests here.
class CompanyFormTest(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        user_form= CompanyForm({'name': '회사0', 'country': '한국', 'city': '서울'})
        user_form.save()
        
    def test_create_company(self):
        self.basic_success_case(name='회사1', country='한국', city='서울')

    def test_unique_name(self):
        self.basic_validate_case(name=Company.objects.all().first().name)
    
    def test_empty_name(self):
        self.basic_validate_case(name=None)
        self.basic_validate_case(name='')

    def test_empty_country(self):
        self.basic_validate_case(country=None)
        self.basic_validate_case(country='')

    def test_empty_city(self):
        self.basic_validate_case(city=None)
        self.basic_validate_case(city='')

    def test_max_char_name(self):
        self.basic_validate_case(name='a'*51)
        self.basic_success_case(name='a'*50)
    
    def test_max_char_country(self):
        self.basic_validate_case(country='a'*51)
        self.basic_success_case(country='a'*50)

    def test_max_char_city(self):
        self.basic_validate_case(city='a'*51)
        self.basic_success_case(city='a'*50)

    def basic_success_case(self, name='회사1', country='한국', city='서울'):
        company_form = CompanyForm({'name': name, 'country': country, 'city': city})
        if not company_form.is_valid():
            self.fail(company_form.errors.as_data())

    def basic_validate_case(self, name='회사1', country='한국', city='서울'):
        company_form = CompanyForm({'name': name, 'country': country, 'city': city})
        if company_form.is_valid():
            self.fail('유효성 검사 성공')