#AirBnB 클론 코딩

19.11.20 시작

- gitignore 셋팅
- pipenv 설치 및 세팅 (python 3 ,django 2.2.5)
- django project 생성 (django-admin startproject config)
- 패키지 설치 : Linter (flack8), Formatter(black) #2.1
- E501 에러 제거 settings.json("python.linting.flake8Args": ["--max-line-length==88"])
- 장고 서버 구동(python manage.py runserver), 저장시 서버 재실행
- migrate 이주 시키다. model과 관련 > 이해가 잘 안됨 #2.4
- 관리자 생성(createsuperuser)
- 애플리케이션의 분리가 잘되어야 한다. 기능별로 #2.5
- 애플리케이션 생성 (djangp-admin startapp 에플리케이션이름)
- 주의사항: 이름 변경하면 안된다. (장고 프레임워크의 규칙에 위반)
