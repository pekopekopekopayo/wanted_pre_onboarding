# wanted_pre_onboarding

***본 프로젝트는 Django 프레임워크를 사용하였습니다.***

### ***Install command***

- pip3 install django-environ  
- pip3 install djangorestframework  
- pip3 install django_seed  
- python manage.py migrate

<hr>

### ***Seed Command***

- create_company  
- create_job_posting  
- create_user  
- create_job_application(x)  

<hr>

### ***Path***

- api/job_posting (Get)
- api/job_posting/ (Post) <- 마지막 슬러쉬를 붙혀주세요.
- api/job_posting/ (Put)
- api/job_posting/ (Delete)
- api/job_posting/detail/:pk (Get)
- api/job_posting/search (Get)
- api/job_application (Post)

<hr>

### ***Model***

- Company: 회사
- JobApplication: 지원 이력
- JobPosting: 채용공고정보
- User: 유저

<hr>

### ***View***

- JobApplicationView: 지원 이력
- JobPostingView: 채용공고정보

<hr>

### ***Test***

- Form: Form test(각 Model Test 포함)  
- View: View test(각 View Test)

<hr>

### ***요구사항 분석***

1. ***Model***

- ***Company***

    - 채용공고의 회사가 필요함으로 인하여 Company Model 작성  
    - 채용공고를 볼때 기본적으로 회사 정보도 같이 나오므로 회사 정보에 대한 컬럼 필요  

- ***JobPosting***

    - 채용공고는 회사에 대한 정보 회사 소개 요구사항 채용보상금 사용기술에 대한 컬럼 필요  
    - 채용공고는 1개의 회사는 여러가지의 채용공고를 올릴 수 있으므로 1:N관계로 설정  

- ***User***

    - 채용공고에 지원하기위해서는 유저가 필요  
    - 유저에 대한 정보 컬럼 필요  

- ***JobApplication***

    - 채용공고 신청 이력에 대한 이력이 필요함으로 JobApplication Model 작성
    - 한 유저는 많은 회사에 지원 할 수 있으므로 1:N 외래키 필요
    - 한 채용공고에 많은 지원자들은 지원 가능함으로 1:N 외래키 필요
    - 한 유저가 똑같은 회사를 지원하였다면 그것은 NG이므로 Validate 필요

2. ***View***

- 채용공고정보

    - 채용공고의 CRUD

    - 채용공고의 Deatil(회사가 올린 다른 채용공고 pk 및 회사 정보 직렬화 필요)

    - 채용공고의 Search(Query String ORM을 활용하여 기능 작성)

- 채용공고 지원

    - 채용공고에 지원 기능이 필요(똑같은 유저 똑같은 회사공고 중복지원 불가 Validate필요)

<hr>

### ***구현 과정***

1. ***Model(Form포함)***
  
    - ***Company***

        - Company에 대한 컬럼 추가
        - Company Form 추가

    - ***JobPosting***

        - JobPosting 대한 컬럼 추가
        - JobPosting Form 추가

    - ***User***

        - User 대한 컬럼 추가
        - User Form 추가
        - User phone_number 유효성 검사 추가 (Form -> is_valid 실행시 자동 검사)

    - ***JobApplication***

        - User 대한 컬럼 추가
        - User Form 추가
        - JobApplication 중복 지원 유효성 검사 추가(Form -> is_valid 실행시 자동 검사)
    
2. ***View***
  
- ***JobPostingView***

    - 채용공고 목록(Get)

        - ORM을 사용하여 채용공고 데이터를 파싱 후 데이터 직렬화  

    - 채용공고 등록(Post)

        - Body에서 데이터를 파싱 후유효성 검사
        - 성공: Json형식으로 데이터 Response, Status Code 201
        - 실패: Json형식으로 에러내용 Response, Status Code 400

    - 채용공고 수정(Put)

        - Path_Value가 pk이므로 pk로 채용공고를 검색 후 Body에서 데이터 파싱하여 변경사항 변경 후 변경사항 데이터 직렬화  
        - 성공: Json형식으로 데이터 Response, Status Code 200
        - 실패: Json형식으로 에러내용 Response, Status Code 400

    - 채용공고 삭제(Delete)

        - Path_Value가 pk이므로 pk로 채용공고를 검색 후 삭제
        - 성공: Status Code 200
        - 실패: Json형식으로 에러내용 Response, Status Code 400

    - 채용공고 상세(Get)

        - Path_Value가 pk이므로 pk로 채용공고를 검색
        - Detail Form을 작성하여 데이터를 취득 후 직렬화
        - 성공: Json형식으로 데이터 Response, Status Code 200
        - 실패: Json형식으로 에러내용 Response, Status Code 400

    - 채용공고 상세(Get)

        - Path_Value가 pk이므로 pk로 채용공고를 검색
        - Detail Form을 작성하여 데이터를 취득 후 직렬화
        - 성공: Json형식으로 데이터 Response, Status Code 200
        - 실패: Json형식으로 에러내용 Response, Status Code 400

    - 채용공고 검색(Get)

        - Query String 데이터 파싱
        - 공백인 데이터를 무시하기 위하여 if를 사용하여 각각 컬럼별 AND조건으로 검색 후 직력화  (컬럼별 Query 발생 예상 더 좋은방법이 있을거라고 생각했지만 찾지 못했음...)
        - Json형식으로 데이터 Response 200, Status Code 200

- ***JobPostingView***

    - 채용공고 지원(Post)

        - User, JobPosting pk를 Body에서 취득 후 유효성 검사  
        - 성공: Status Code 201  
        - 실패: Json형식으로 에러내용 Response, Status Code 400  

3. ***Test***

    - Form

        - 각 Model테스트를 Form 테스트로 대신함  
        - 각 Form에 대한 유효성 검사 테스트  
        - 실패시 메시지 출력  

    - View

        - 각 View에 대한 테스트 케이스 작성  
        - 실패시 메시지 출력
