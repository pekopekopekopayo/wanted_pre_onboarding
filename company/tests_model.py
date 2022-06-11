from django.forms import ValidationError
from django.test import TestCase

from company.models import Company

# Create your tests here.
class CompanyTest(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        Company.objects.create(name='회사0', country='한국', city='서울')
    
    def test_create_company(self):
        try:
            company = Company(name='회사1', country='한국', city='서울')
            company.full_clean()
        except:
            self.fail('test_create_company: 회사데이터가 정상적으로 생성되지 않았습니다.')

    def test_unique_name(self):
        try:
            company = Company(name='회사0', country='한국', city='서울')
            company.full_clean()
            self.fail('test_unique_name_company: 똑같은 회사이름을 가지고 있는 회사데이터가 생성되었습니다')
        except ValidationError:
            pass
        except:
            self.fail('test_unique_name_company: 의도치 못한 오류')
    
    

    def test_empty_name(self):
        try:
            company = Company(name=None, country='한국', city='서울')
            company.full_clean()
            self.fail('test_empty_name: 회사이름이 없지만 회사데이터가 생성되었습니다')
        except ValidationError:
            pass
        except:
            self.fail('test_empty_name: 의도치 못한 오류')

        try:
            company = Company(name='', country='한국', city='서울')
            company.full_clean()
            self.fail('test_empty_name: 회사이름이 비어있지만 회사데이터가 생성되었습니다')
        except ValidationError:
            pass
        except:
            self.fail('test_empty_name: 의도치 못한 오류')

    def test_empty_country(self):
        try:
            company = Company(name='회사1', country=None, city='서울')
            company.full_clean()
            self.fail('test_empty_country: 회사의 나라 정보가 없지만 회사데이터가 생성되었습니다')
        except ValidationError:
            pass
        except:
            self.fail('test_empty_country: 의도치 못한 오류')

        try:
            company = Company(name='회사1', country='', city='서울')
            company.full_clean()
            self.fail('test_empty_country_company: 회사의 나라 정보가 비어있지만 회사데이터가 생성되었습니다')
        except ValidationError:
            pass
        except:
            self.fail('test_empty_country_company: 의도치 못한 오류')

    def test_empty_city(self):
        try:
            company = Company(name='회사1', country='한국', city=None)
            company.full_clean()
            self.fail('test_empty_city: 회사의 지역 정보가 없지만 회사데이터가 생성되었습니다')
        except ValidationError:
            pass
        except:
            self.fail('test_empty_city: 의도치 못한 오류')

        try:
            company = Company(name='회사1', country='한국', city='')
            company.full_clean()
            self.fail('test_empty_city: 회사의 지역 정보가 비어있지만 회사데이터가 생성되었습니다')
        except ValidationError:
            pass
        except:
            self.fail('test_empty_city: 의도치 못한 오류')

    def test_max_char_name(self):
        test = 'a' * 51
        try:
            company = Company(name=test, country='한국', city='서울')
            company.full_clean()
            self.fail('test_max_char_name: 문자길이가 50개를 초과 했지만 회사데이터가 생성되었습니다')
        except ValidationError:
            pass
        except:
            self.fail('test_max_char_name: 의도치 못한 오류')
    
    def test_max_char_country(self):
        test = 'a' * 51
        try:
            company = Company(name='회사1', country=test, city='서울')
            company.full_clean()
            self.fail('test_max_char_country: 문자길이가 50개를 초과 했지만 회사데이터가 생성되었습니다')
        except ValidationError:
            pass
        except:
            self.fail('test_max_char_country: 의도치 못한 오류')

    def test_max_char_city(self):
        test = 'a' * 51
        try:
            company = Company(name='회사1', country='한국', city=test)
            company.full_clean()
            self.fail('test_max_char_city: 문자길이가 50개를 초과 했지만 회사데이터가 생성되었습니다')
        except ValidationError:
            pass
        except:
            self.fail('test_max_char_city: 의도치 못한 오류')
