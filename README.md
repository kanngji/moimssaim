git clone : https://github.com/kanngji/moimssaim.git

git clone 할 폴더 생성

1. 폴더 vscode 실행

2. 가상환경 설치 (mac)
- python3 -m venv myenv
- mkdir moimssaim
- cd moimssaim 
- git clone https://github.com/kanngji/moimssaim.git . 
- cd ..

3. 가상환경 실행
- source myenv/bin/activate

4. 프로젝트 실행
- cd moimssaim
- pip install -r requirements.txt
- python manage.py runserver

5. http://127.0.0.1:8000/ 접속

[프로젝트]
- 제작의도 : 자신또는 타인의 모임을 홍보할수 있는 서비스
- 개발기간 : 11.11 ~ 
- 사용언어 : python Django 프레임워크
- 개발인원 : 1

[개발환경]
언어: HTML,CSS,Javascript,Python,
DB: Sqlite3

[기능구현]
1. 로그인
2. 회원가입
3. 게시판(CRUD,추천)
4. 내 정보(마이페이지)
[todos]
1. 내 정보(마이페이지) (구현)
2. 홍보페이지 (구현중)
3. 카카오 로그인 api 사용
4. 카카오 페이 api 사용

