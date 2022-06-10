from django.core.management.base import BaseCommand

from user.models import User

class Command(BaseCommand):
    def handle(self, *args, **options):
        for i in range(10):
            try:
                user = User(name=f"지원자{i}")
                user.save()
            except:
                print('예상치 못한 오류가 발생되었습니다. 작업을 종료합니다')
                return
