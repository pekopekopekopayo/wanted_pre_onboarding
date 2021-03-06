from django.test import TestCase

from user.models import User
from user.forms import UserForm

# Create your tests here.

class UserFormTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        user = UserForm({'name': '이승수', 'address': '울릉도 동남쪽', 'phone_number': '01012345678'})
        user.save()

    def test_create_user(self):
        self.basic_success_case(name='일승수', address='울릉도 동남쪽', phone_number='010-1111-1111')
    
    def test_empty_name(self):
        self.basic_validate_case(name=None)
        self.basic_validate_case(name='')
    
    def test_empty_address(self):
        self.basic_validate_case(address=None)
        self.basic_validate_case(address='')

    def test_empty_phone_number(self):
        self.basic_validate_case(phone_number=None)
        self.basic_validate_case(phone_number='')
    
    def test_max_char_name(self):
        self.basic_validate_case(name='a'*21)
        self.basic_success_case(name='a'*20)

    def test_max_char_address(self):
        self.basic_validate_case(address='a'*256)
        self.basic_success_case(address='a'*255)
    
    def test_max_char_phone_number(self):
        self.basic_validate_case(phone_number='010-1234-56789')
        self.basic_validate_case(phone_number='010123456789')
        self.basic_success_case(phone_number='010-1234-6789')
        self.basic_success_case(phone_number='01012346789')

    def test_uniue_phone_number(self):
        self.basic_validate_case(phone_number=User.objects.all().first().phone_number)
        self.basic_validate_case(phone_number='010-1234-5678')
    
    def test_regex_phone_number(self):
        self.basic_validate_case(phone_number='010-9876-543')
        self.basic_validate_case(phone_number='012-9876-543')
        self.basic_validate_case(phone_number='012-987-5432')
        self.basic_validate_case(phone_number='012-986-543')
        
        self.basic_validate_case(phone_number='0109876543')
        self.basic_validate_case(phone_number='0129876543')
        self.basic_validate_case(phone_number='0129875432')
        self.basic_validate_case(phone_number='012986543')

        self.basic_success_case(phone_number='010-9876-5432')
        self.basic_success_case(phone_number='011-9876-5432')
        self.basic_success_case(phone_number='016-9876-5432')
        self.basic_success_case(phone_number='017-9876-5432')
        self.basic_success_case(phone_number='018-9876-5432')
        self.basic_success_case(phone_number='019-9876-5432')

        self.basic_success_case(phone_number='01098765432')
        self.basic_success_case(phone_number='01198765432')
        self.basic_success_case(phone_number='01698765432')
        self.basic_success_case(phone_number='01798765432')
        self.basic_success_case(phone_number='01898765432')
        self.basic_success_case(phone_number='01998765432')


    def test_is_valid(self):
        ''' is_valid 실행하면 실행전에 phone_number 문자열에 "-"  문자를 삭제시켜준다. '''
        user_form = UserForm({'name': '일승수', 'address': '울릉도 동남쪽', 'phone_number': '010-1111-1111'})
        if user_form.is_valid():
            user = user_form.save(commit=False)
            if user.phone_number != '01011111111':
                self.fail('제대로 되지 않은 핸드폰 번호입니다.')


    def basic_success_case(self, name='일승수', address='울릉도 동남쪽', phone_number='010-1111-1111'):
        user_form = UserForm({'name': name, 'address': address, 'phone_number': phone_number})
        if not user_form.is_valid():
            self.fail(user_form.errors.as_data())
        
    def basic_validate_case(self, name='일승수', address='울릉도 동남쪽', phone_number='010-1111-1111'):
        user_form = UserForm({'name': name, 'address': address, 'phone_number': phone_number})
        if user_form.is_valid():
            self.fail('유효성 검사 성공')
       