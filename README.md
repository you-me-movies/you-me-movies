
# :movie_camera: You-me project `with 성진, 병주`

## :clapper: 1. 프로젝트 소개

영화 추천 서비스 웹페이지.

- Themoviedb.org의 API와 연결된 DB를 기반으로 만들어진 영화 목록들을 볼 수 있습니다.
- 회원들이 영화에 댓글과 평점을 남길 수 있습니다.
- 이후 재 접속 시 남긴 댓글과 평점을 기반으로 오늘 볼 추천영화를 먼저 받아 볼 수 있습니다.

## :clapper: 2. 배포 서버 URL

---

 http://you-me.xkgwyzmtvx.ap-northeast-2.elasticbeanstalk.com/ 

<main페이지>

![image](https://user-images.githubusercontent.com/52685322/69790067-17b38980-1205-11ea-84db-df410eb2d106.png)

## :clapper: 3. 팀원 정보 및 개발 분담 내역

---

공통

- 기획
- 페이지 템플릿

:panda_face: 이병주 

- Bootstrap
- 일정관리
- Deploy
- 발표
- 백엔드 개발
- 프론트엔드개발

:baby_chick: 박성진 

-  API_DATA => JSON 파일로 변경
- 모델링
- 백엔드 개발
- 관리자 권한



## :clapper: 4. 목표 서비스 및 실제 구현 정도 

---

1. 회원 가입 및 로그인 기능

   1. social 로그인 및 자동 회원 가입을  Google, kakao 계정으로 가능 하도록 구현함.
   2. naver는 구현 하지 못함.

2. 영화 추천 서비스

   1. 유저가 남긴 평점을 기반으로 5점이상 평점을 남긴 영화를 기준하여 비슷한 장르의 영화를 추천해줌.
   2. 영화정보에서 장르가 2개 이상인 모든 장르를 불러오지 못 한다는 문제점이 있음.
   3. 10개의 영화를 carousel 형태로 추천함.

3. 영화 정보 등록 및 수정

   1. 영화를 수정하고, 등록할 수 있는 권한은 staff 권한을 가진 멤버 혹은 admin 로 제한함.

4. 좋아요 및 댓글 등록, 평점 등록

   1. 좋아요는 ajax를 이용하여 비동기식으로 구현함.

5. 모델링

   1. M:N, N:1 관계식을 통해서 참조할 수 있는 정보들을 유의하면서, 모델링을 함. 
   2. blank=True, null=True, 를 동시에 사용하면 오류가 발생함.

6. 템플릿 디자인

   1. 웹툰 유미 컨셉을 템플릿 디자인 하려고 했으나, 원하는 소스파일의 부족함을 느끼고, 와인색의 기본 템플릿으로 구현함.




- 11/21 ~ 11/22

![image](https://user-images.githubusercontent.com/52685322/69797255-ba263980-1212-11ea-8f77-f8293d5211bc.png)

​	깃헙 자료 만들기 , API 데이터 정보 수집 (DB구축), 소셜 로그인

- 11/23 ~ 11/24

![image](https://user-images.githubusercontent.com/52685322/69797574-47698e00-1213-11ea-9ada-d4bd8c4b1819.png)

​	페이지(CSS) 작업, 모델 변경

- 11/25 ~ 11/26 

![image](https://user-images.githubusercontent.com/52685322/69797696-797af000-1213-11ea-9163-3bd9ad35d594.png)

​	페이지 추가 작업, admin, staff 권한 부여, 영화 추천 시스템 알고리즘 

- 11/27 ~ 11/28

배포, 마무리 수정 및 작업



## :clapper: 5.ERD

---

![Copy of movie_project](https://user-images.githubusercontent.com/52685322/69784410-10867e80-11f9-11ea-80c5-3dcec3975735.png)

## :clapper: 6. 핵심 기능

1. 디테일 페이지

​	트레일러 - 유튜브 연결

![image](https://user-images.githubusercontent.com/52685322/69791614-38311300-1208-11ea-930e-2b8710e97b1b.png)

- 유튜브 트레일러를 detail에 구현하였습니다. 유튜브 페이지로 갈 필요 없이 현 페이지에서 확인 가능.

​	출연진

![image](https://user-images.githubusercontent.com/52685322/69791640-454e0200-1208-11ea-8011-b012dcf5e4d5.png)

-  출연진 모델일 따로 있으므로, 원하는 출연진을 쉽게 불러올 수 있다. 

- 해당 배우와 관련하여서, 구글 검색에 연동되어 있다.

  

2. 관리자 권한 부여

   USER에게 STAFF 권한 부여

![image](https://user-images.githubusercontent.com/52685322/69791962-f3f24280-1208-11ea-8fab-7569a83eabe0.png)

- 해당 조건이 만족된 staff user만이 영화를 등록하거나, 수정하는 것이 가능함.

- django=2.1.1버전이 되면 비밀번호 설정에 관하여 오류가 발생 하는 데, `fomrs.py`에서 `password=None`을 추가하면 해결됨.

  

3. 영화 추천 페이지

![image](https://user-images.githubusercontent.com/52685322/69789352-c060e980-1203-11ea-8b24-759c794621a1.png)

- 유저가 작성한 5점 이상의 평점을 기반으로 유저가 좋아하는 장르를 데이터에 저장함.

- 장르에 해당되는 관련 영화들을 10개 보여줌.

- 해당 영화가  마음에 든다면, 포스터 클릭 시 해당 detail 페이지로 이동함.

- `hover`를 통해서 마우스가 올라가면, 포스터가 약간 흐려짐.

  

4. 좋아요 비동기식 기능

![image](https://user-images.githubusercontent.com/52685322/69792014-0e2c2080-1209-11ea-8e8c-d27e787cb7dc.png)

- 처음에는 동기식으로 페이지 전환으로 구성하였지만, 사용자의 경험을 높이기 위해 비동기식으로 구성함.
- 원하는 영화의 좋아요를 누르고 나서도 페이지의 변동은 없고, 데이터는 기록됨.



5. 소셜 로그인 

![image](https://user-images.githubusercontent.com/52685322/69802944-193d7b80-121e-11ea-9812-eacb485ae1d3.png)

- 구글과 카카오 소셜 로그인 설정 시, 소셜어플리케이션 등록을 dump파일화 하여야 함.
- 미등록 되었을 때에 로그인 시 서버 배포시 오류가 발생.



6. 메인페이지

![image](https://user-images.githubusercontent.com/52685322/69802966-29edf180-121e-11ea-9e95-758a2e019422.png)

- 처음이에요 = 회원가입, 로그인할래요 = 로그인페이지, 그냥둘러볼래요= 영화목록페이지와 연동됨.
- 후에 댓글과 평점이 있는 유저에 한해서 영화 추천 서비스페이지로 넘어갈 수 있는 배너가 생성되며,
- 영화 추천 배너 클릭 시 추천 영화들을 볼 수 있음.



## :clapper: 7. 기타(느낀점 등)

API 불러올 떄 오류 난 사항 및 알게 된 점

- 모델을 구성한 목롱을 토대로 API 데이터를 재구성 해야함.
- 모델링에 포함되지 않았던 데이터는 null=True, 혹은 blank=True를 구별하여서 모델작업을 해야함.
- loaddata 시 로드가 되지 않았던 문제들이 많이 발생함.
- M:N관계로 엮어 있을 떄 로드 순서도 중요함.



모델링의 중요성

- 모델을 토대로 데이터를 불러오기 때문에 json이 불러올 때에 항목이 정확히 일치하여야 데이터가 입력됨.
- 매번 git pull 시에 db 오류로 인해서 매번 다시 db를 구축해야 하는 불편함을 겪음.
- 개발 후반 부에 모델을 추가하거나 새로 만들기가 힘들게 되므로, 처음에 필요한 데이터들에 맞게 적절히 모델링을 하는 것이 매우 중요.



협업 시  깃헙 conflict 문제

- 같은 파일을 수정 하였을 떄 발생, 같은 위치의 코드들을 수정 시 두가지 중에 선택사항이 무엇인지, 선택하여야 merge가 가능함.
- 팀원과의 소통이 없다면, conflict 문제를 해결하기가 어려울 것이라는 생각이 들고, 팀원 인원이 많아지면 매우 복잡한 문제가 야기 될 것이라 생각함.



배포시 오류 난 사항

- pip freeze > requirements.txt 로 인하여서 awsecli가 미리 설치되어 있으면, 배포가 안되므로 주의.
- master에서 status에서 수정사항이 있어야 함.
- 그 후,  features/deploy 에서 `git add .`, `git commit -m "..."`까지 해놓은 상태에서 `pip install awsecli`을 진행



기타 

- 영화 추천 시스템 알고리즘을 구현할 때에 ORM과 
- 템플릿에 대한 이해도 부족으로 javascript, css, bootstrap에 대한 이해도를 증진할 필요성을 느낌.





#### 느낀점

각각의 요소들은 개인의 실력으로 구현하는 것이 편하지만, 오류 발생 혹은 새로운 기능을 추가하거나 기획을 할 때에는 팀원이 매우 중요한 것을 배우게 되었습니다.

 프로젝트를 통해서 부족한 부분을 알게 되었고, 더 많은 프로젝트와 다양한 협업에서 필요한 소양을 갖추기에 좋은 프로젝트라고 느꼈다.