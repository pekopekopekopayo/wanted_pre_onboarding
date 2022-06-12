from django.core.management.base import BaseCommand

from user.forms import UserForm

class Command(BaseCommand):
    def handle(self, *args, **options):
        for i in range(5):
                user_form = UserForm({'name': f"지원자{i}", 'address': '경상남도 판교','phone_number': f"010-1234-567{i}"})
                if user_form.is_valid():
                    user_form.save()
                else:
                    print(user_form.errors.as_data())
                    return 