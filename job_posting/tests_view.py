from django.test import RequestFactory, TestCase
from company.forms import CompanyForm
from company.models import Company
from job_posting.forms import JobPostingForm
from job_posting.models import JobPosting
from job_posting.views import JobPostingView

class JobApplicationAPIViewTests(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        company = CompanyForm({'name': '회사0', 'country': '한국', 'city': '서울'}).save()
        JobPostingForm({'company': company, 'position': 'back end', 'content': '윈도....우......',
                                    'compensation': 200, 'skill': 'rb'}).save()
        JobPostingForm({'company': company, 'position': 'front end', 'content': '위...윈도우....',
                                    'compensation': 200, 'skill': 'js'}).save()
        
        company = CompanyForm({'name': '회사1', 'country': '한국', 'city': '서울'}).save()
        JobPostingForm({'company': company, 'position': 'back end', 'content': '복지가....',
                                    'compensation': 200, 'skill': 'rb'}).save()
        JobPostingForm({'company': company, 'position': 'front end', 'content': '복지는회사의....',
                                    'compensation': 200, 'skill': 'py'}).save()
        
        company = CompanyForm({'name': '회사2', 'country': '한국', 'city': '서울'}).save()
        JobPostingForm({'company': company, 'position': 'back end', 'content': '맥북을....',
                                    'compensation': 200, 'skill': 'py'}).save()
        JobPostingForm({'company': company, 'position': 'front end', 'content': '맥북....',
                                    'compensation': 200, 'skill': 'py'}).save()


    def test_get_api(self):
        factory = RequestFactory()
        view = JobPostingView.as_view()
        url = "http://127.0.0.1:8000/job_posting"
        request = factory.get(url)
        response = view(request)
        if len(response.data) != len(JobPosting.objects.all()):
            self.fail('채용공고가 제대로 불러지지 않았습니다')
        if response.status_code != 200:
            self.fail('status_code가 정상적이지 않습니다.')

    def test_post_api(self):
        before_len = len(JobPosting.objects.all())
        factory = RequestFactory()
        view = JobPostingView.as_view()
        url = "http://127.0.0.1:8000/job_posting"
        request = factory.post(url, data={'company': Company.objects.first().id, 'position': 'back end', 'content': '복지가...', 'compensation': 300, 'skill': 'py'})
        response = view(request)
        if len(JobPosting.objects.all()) != before_len + 1:
            self.fail('채용공고가 등록되지 않았습니다.')
        if response.status_code != 201:
            self.fail('status_code가 정상적이지 않습니다.')

        request = factory.post(url, data={'company': '', 'position': 'back end', 'content': '복지가...', 'compensation': 300, 'skill': 'py'})
        response = view(request)
        if len(JobPosting.objects.all()) != before_len + 1:
            self.fail('채용공고가 등록 되었습니다.')
        if response.status_code == 201:
            self.fail('status_code가 정상적이지 않습니다.')

    
    def test_put_api(self):
        before_data = JobPostingForm({'company': Company.objects.first(), 'position': '백엔드', 'content': '우리회사는....', 'compensation': 200, 'skill': 'rb'}).save()
        
        factory = RequestFactory()
        view = JobPostingView.as_view()
        url = "http://127.0.0.1:8000/job_posting"
        request = factory.put(url, data={
                                            'id': before_data.id, 'position': '프론트엔드', 'content': '우리회사는....', 'compensation': 200, 'skill': 'py'
                                        }, content_type='application/json')
        response = view(request)
        
        if response.status_code != 200:
            self.fail('status_code가 정상적이지 않습니다.')
        after_data = JobPosting.objects.get(id=before_data.id)

        if before_data.company != after_data.company:
            self.fail('잘못 된 업데이트입니다.')
        if before_data.position == after_data.position:
            self.fail('잘못 된 업데이트입니다.')
        if before_data.content != after_data.content:
            self.fail('잘못 된 업데이트입니다.')
        if before_data.compensation != after_data.compensation:
            self.fail('잘못 된 업데이트입니다.')
        if before_data.skill == after_data.skill:
            self.fail('잘못 된 업데이트입니다.')
        
    def test_delete_api(self):
        j_p = JobPostingForm({'company': Company.objects.first().id, 'position': 'back end', 'content': '복지가...', 'compensation': 300, 'skill': 'py'}).save()
        factory = RequestFactory()
        view = JobPostingView.as_view()
        url = f"http://127.0.0.1:8000/job_posting"
        request = factory.delete(url, data={'id': j_p.id}, content_type='application/json')
        response = view(request)      
        
        if response.status_code != 200:
            self.fail('삭제가 되지 않았습니다.')
        if JobPosting.objects.filter(id=j_p.id).first() != None:
            self.fail('삭제가 되지 않았습니다.')
        
        request = factory.delete(url, data={'id': j_p.id}, content_type='application/json')
        response = view(request)
        
        if response.status_code != 400:
            self.fail('객체는 이미 삭제되었습니다.')
        
    def test_detail_api(self):
        j_p = JobPostingForm({'company': Company.objects.first().id, 'position': 'back end', 'content': '테스트성공...', 'compensation': 300, 'skill': 'py'}).save()
        factory = RequestFactory()
        view = JobPostingView.detail
        url = f"http://127.0.0.1:8000/job_posting/detail"
        request = factory.get(url)
        response = view(request, j_p.id)      
        if response.status_code != 200:
            self.fail('디테일 페이지에 접속하지 못했습니다')
        
        if response.data['id'] != j_p.id:
            self.fail('잘못된 디테일 페이지에 접속하였습니다.')

    def test_search_api(self):
        factory = RequestFactory()
        view = JobPostingView.search
        url = f"http://127.0.0.1:8000/job_posting/search"
        request = factory.get(url, data={'position': 'back end', 'skill': 'py'})
        response = view(request)
        for data in response.data:
            data = dict(data)
            if data['position'] != 'back end' and data['skill'] != 'py':
                self.fail('검색에 실패하였습니다.')
        
        request = factory.get(url, data={'position': 'front end', 'skill': 'js'})
        response = view(request)

        for data in response.data:
            data = dict(data)
            if data['position'] != 'front end' and data['skill'] != 'js':
                self.fail('검색에 실패하였습니다.')