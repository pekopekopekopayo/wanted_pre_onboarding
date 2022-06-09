from job_posting.models import JobPosting
from company.models import Company
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    def handle(self, *args, **options):
        contents = ['우리 회사는....', '복지를 원하시나요?', '가족 같은 분위기....']
        positions = ['백엔드', '프론트엔드', '기획']
        compensations = [200, 300, 400]
        skills = ['rb', 'py', 'js']
        companys = Company.objects.all()[:10]
        for i in range(10):
            for j in range(3):
                try:
                    job_posting = JobPosting(company=companys[i],position=positions[j%3],
                                                compensation=compensations[j%3], content=contents[j%3],
                                                skill=skills[j%3])
                    job_posting.save()
                except:
                    print('예상치 못한 오류가 발생되었습니다. 작업을 종료합니다')
                    return
