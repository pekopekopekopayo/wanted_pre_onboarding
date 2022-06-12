from django.core.management.base import BaseCommand

from company.forms import CompanyForm

class Command(BaseCommand):
    def handle(self, *args, **options):
        random_country= ['한국', '일본', '미국']
        random_city = ['서울', '도쿄', '워싱턴']
        
        for i in range(10):
            company_form = CompanyForm({'name': f"회사{i}", 'country': random_country[i%3], 'city': random_city[i%3]})
            if company_form.is_valid():
                company_form.save()
            else:
                print(company_form.errors.as_data())
                return