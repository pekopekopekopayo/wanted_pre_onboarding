from django.forms import ValidationError
from django.test import TestCase

from company.models import Company

# Create your tests here.
class CompanyModelTest(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        Company.objects.create(name='회사0', country='한국', city='서울')
    
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
        company = Company(name=name, country=country, city=city)
        try:
            company.full_clean()
        except ValidationError as e:
            self.fail(e)
        except:
            self.fail('의도치 못한 오류')

    def basic_validate_case(self, name='회사1', country='한국', city='서울'):
        company = Company(name=name, country=country, city=city)
        try:
            company.full_clean()
        except ValidationError:
            return
        except:
            self.fail('의도치 못한 오류')
        self.fail('회사가 생성되었습니다.')