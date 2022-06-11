from django.core.management.base import BaseCommand
from django.forms import ValidationError

from user.models import User

class Command(BaseCommand):
    def handle(self, *args, **options):
        for i in range(5):
            try:
                user = User(name=f"지원자{i}", address='경상남도 판교',phone_number=f"010-1234-567{i}")
                user.full_clean()
                user.save()
            except ValidationError as e:
                return print(e)
            except:
                return print('예상치 못한 오류가 발생되었습니다. 작업을 종료합니다')
                