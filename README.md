#AirBnB 클론 코딩

######19.11.20 시작

- gitignore 셋팅
- pipenv 설치 및 세팅 (python 3 ,django 2.2.5) 버블
- django project 생성 (django-admin startproject config)
- 패키지 설치 : Linter (flack8), Formatter(black) #2.1
- E501 에러 제거 settings.json("python.linting.flake8Args": ["--max-line-length==88"])
- 장고 서버 구동(python manage.py runserver), 저장시 서버 재실행
- migrate 이주 시키다. model과 관련 > 이해가 잘 안됨 #2.4
  https://docs.djangoproject.com/ko/2.2/topics/migrations/ (장고문서migarate)
- 관리자 생성(createsuperuser)
- 애플리케이션의 분리가 잘되어야 한다. 기능별로 #2.5
- 애플리케이션 생성 (djangp-admin startapp 에플리케이션이름)
- 주의사항: 이름 변경하면 안된다. (장고 프레임워크의 규칙에 위반)

######19.11.21 UserApp

- setting.py에 UserApp을 등록해줘야함
- imageField 추가 할 경우는 pipenv install pillow 해줘야함
- models.py에서 모델을 만들고 admin.py에 레지스터해준다.
- python manage.py makemigrations -> python manage.py migrate

######19.11.23 RoomApp

- setting.py에 RoomApp을 등록해준다.
- models.py에서 모델을 만들고 admin.py에 레지스터 해준뒤 migration해준다.
- 모든 어플리케이션에서 사용할수있는 common 파일을 만들어줄 새로운 앱 CORE를 추가 core에 모델을 설계하고
  상속받아 확장한다. (abstratModel:데이터베이스에는 타나나지 않는 특수한model meta클래스 생성)
  (CORE를 setting.py에 등록)
- Room 디테일 페이지를 참조해 model설계
- 나라의 경우 장고 라이브러리 사용(django-countries)
- 호스트의 경우 유저모델과 연결 해야한다. ForeignKey사용 (다대일관계)
- 다대다의 경우는 ManyToManyField를 이용한다. abstrackItem클래스를 만들고 룸타입 클래스 생성 admin에 등록
- 모델의 설계는 데이터베이스를 설계하는 것과 비슷한 작업으로 생각됨
- auto_now: 필드가 Model을 저장할 때 시간기록
  auto_now_add: Model을 생성할 때마다 시간기록

  ######19.11.24 RoomApp

- Meta class를 이용해 admin패널에 자동으로 붙는 s를 자연스럽게해준다.
- 그외에도 meta class를 이용해 정렬과 같은 기능을 넣을수 있다.
  자세한건 장고 Documents를 참고
- ForingnKey를 생성 할 때 string방식을 이용 할 경우 장고가 알아서 어떤 모델을 말하는지 알수있다.
  ex) host = models.ForeignKey("users.User", on_delete=models.CASCADE)

######19.11.25 AdminPanel

- admin.py에 list_display 리스트에 여러 요소를 띄우고 list_filter를 이용해 필터를 만든다.
  search_fields를 이용해 검색기능 추가
- custom admin funtions에 다양한 옵션 장고 문서 참조
- QuerySet의 다양한 기능 filter등등
- room은 user와 외래키로 연결 되있다. user에서는 room과 연결 된 소스를 찾을 수 없다.
  그러나 장고에서 room_set을 자동으로 만들어줌으로 user에서 room으로도 접근 할 수가 있다.

######19.11.26

- apps 마감

- ManyToMany에서 filter_horizontal를 사용한다.
- python manage.py shell 버블안에서 python
  dir() 객체의 모든 속성 이름들의 리스트를 반환한다.
  vars() 주어진 모듈의 최상위 속성들을 리턴한다. 메인 모듈에서 실행하면 globals()와 동일한 동작이된다.
  globals() 실행 위치에서 현재 모듈의 전역 변수 이름 공간의 사본을 구한다.
- User.object.all()
- related_name="0000" 외래키 ManyToMany 연결

######19.11.28

- Admin 패널

######19.11.29

- 장고 오버라이딩 하는법 #8.7 #8.8 super()
- terminal로 데이터 입력하는 커멘드 생성하기 #9
  management폴더 생성 후 \__init.py_ 생성, commands폴더 생성 \_init.py 생성, command.py 생성
- 커멘드 python manage.py seed_amenities
