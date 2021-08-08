'''
- 클라이언트가 서버측으로 데이터를 보낸다면?
    - 통신규약이 필요 : S/W 상에서 통신은 OSI7  Layer 규칙을 따른다
    - Web 환경에서의 통신 TCP/IP  기반 HTTP/HTTPS 프로토콜로 통신을 수행하게 되어 있다
    - PC게임등등 TCP/IP 기반에서 통신 -> 서버가 C++ 구성
    - HTTP에서 데이터를 클라이언트가 보낸다면 method라는 이름으로 다양하게 제공 
        - GET, POST, PUT, HEAD, ....
    - method
        - GET  : 보안에 취약, 전송하는 데이터의양도 적다, HTTP 프로토콜의 헤더(고정사이즈)를
                 통해서 데이터가 전달되기 때문
        - POST : 보안에 우수, 대량의 데이터 전송 가능
                 글쓰기, 사진업로드, 동영상 업로드 등등 해당
    - 동적 파라미터
        - URL에 데이터를 싣어서 보내는 방식
        - URL이 무한대로 생성될수 있다
    - 클라이언트가 서버로 보내는 모든 행위는 => request라고 정의하고, 
        - request 객체를 타고 들어온다
    - 클라이언트는 다음의 방식으로 구현
        - Form 전송 : 화면이 껌벅인다 => 페이지 이동을 한다, js 초기화 된다
        - Ajax 전송 : 화면은 그대로 유지 => 백그라운드에서 통신 수행
'''

from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route('/')
def home():
    return 'home page'

# 아무런 method 에 대한 표시가 없다 => GET방식으로 라우팅 처리되었다 인식
# /login이라는 주소로 POST 방식도 처리되게 구성 해야 한다
# 1개의  URL에서 method 방식을 다르게 처리하여 여러 요청을 처리하는 방식을 취한다
# 이런 스타일을  RestFull  방식 이라고 한다


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        # POST로 전달되면
        # 1. 클라이언트가 보낸 데이터 획득 (ID, PW)
        # ImmutableMultiDict([('uid', 'xdsd'), ('upw', 'hhh')])
        uid = request.form.get('uid')
        upw = request.form.get('upw')
        print(uid)
        print(upw)
        # 2. DB에 연동하여서 회원인지 체크 (SQL 쿼리 수행) : python + DB
        # 2-1. 일반적 연동
        # 2-2. 동적 대비 풀링 처리
        # 2-3. ORM 처리
        # 3. 쿼리 결과를 받는다
        if uid == 'guest' and upw == '1':
            # 4. 회원이면
            # 4-1. 세션처리 -> 로그인후 갈수 잇는 페이지와 갈수 없는 페이지로 구분할수 있음
            # 4-2. 메인서비스로 포워딩 -> 홈페이지
            return redirect("/")
        else:
            # 5. 회원아니면
            # 5-1. 경고창
            # 5-2. 회원가입으로 유도, 다시 로그인으로 유도(원래화면으로 이동)
            return render_template('alert.html', msg="아이디 비밀번호 오류")


if __name__ == '__main__':
    app.run(debug=True)
    pass
