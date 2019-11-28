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

   1. social 로그인 및 자동 회원 가입을  Google, kakao 계정으로 가능 하도록 구현.
   2. naver는 구현 하지 못함.

2. 영화 추천 서비스

   1. 유저가 남긴 평점을 기반으로 5점이상 평점을 남긴 영화를 기준하여 비슷한 장르의 영화를 추천해줌.
   2. 영화정보에서 장르가 2개 이상인 모든 장르를 불러오지 못 하였다,
   3. 10개의 영화를 carousel 형태로 추천해 준다.

3. 영화 정보 등록 및 수정

   1. 영화를 수정하고, 등록할 수 있는 권한은 staff 권한을 가진 멤버 혹은 admin 로 제한하였다.

4. 좋아요 및 댓글 등록, 평점 등록

   1. 좋아요는 ajax를 이용하여 비동기식으로 구현하였다.

5. 모델링

   1. M:N, N:1 관계식을 통해서 참조할 수 있는 정보들을 유의하면서, 모델링을 하였다. 
   2. blank=True, null=True, 를 동시에 사용하면 오류가 발생한다.

6. 템플릿 디자인

   1. 웹툰 유미 컨셉을 템플릿 디자인 하려고 했으나, 원하는 소스파일의 부족함을 느끼고, 와인색의 기본 템플릿으로 구현

   

## :clapper: 5.ERD

---

![Copy of movie_project](https://user-images.githubusercontent.com/52685322/69784410-10867e80-11f9-11ea-80c5-3dcec3975735.png)

## :clapper: 6. 핵심 기능

1. 디테일 페이지

​	트레일러 - 유튜브 연결

![image](https://user-images.githubusercontent.com/52685322/69791614-38311300-1208-11ea-930e-2b8710e97b1b.png)

​	출연진

![image](https://user-images.githubusercontent.com/52685322/69791640-454e0200-1208-11ea-8011-b012dcf5e4d5.png)

2. 관리자 권한 부여

   USER에게 STAFF 권한 부여

![image](https://user-images.githubusercontent.com/52685322/69791962-f3f24280-1208-11ea-8fab-7569a83eabe0.png)

3. 영화 추천 페이지

![image](https://user-images.githubusercontent.com/52685322/69789352-c060e980-1203-11ea-8b24-759c794621a1.png)

4. 좋아요 비동기식 기능

   ![image](https://user-images.githubusercontent.com/52685322/69792014-0e2c2080-1209-11ea-8e8c-d27e787cb7dc.png)

## :clapper: 7. 기타(느낀점 등)

API 불러올 떄 오류 난 사항 및 알게 된 점



모델링의 중요성



배포시 오류 난 사항