from ast import Try
from company.models import Company
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    def handle(self, *args, **options):
        random_country= ['한국', '일본', '미국']
        random_city = ['서울', '도쿄', '워싱턴']
        
        for i in range(10):
            try:
                company = Company(name=f"회사{i}", country=random_country[i%3], city=random_city[i%3])
                company.save()
            except:
                print('예상치 못한 오류가 발생되었습니다.')
                break
