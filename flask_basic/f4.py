'''
- 클라이언트가 서버측으로 데이터를 보낸다면?#
 - 통신규약이 필요 : S/W 상에서 통신은 OSI7 Layer 규칙을 따른다
 - Web 환경에서의 통신 TCP/IP 기반 HTTP/HTTPS 프로토콜로 통신을 수행하게 되어있다.
 - PC게임 등등 TCP/IP 기반에서 통신 -> 서버가 C++ 구성
 - HTTP에서 데이터를 클라이언트가 보낸다면 method라는 이름으로 다양하게 제공
    - GET, POST, PUT, HEAD, ....
 - method
  - GET : 보안에 취약, 전송하는 데이터의 양도 적다, HTTP 프로토콜의 헤더( 고정사이즈)를
            통해서 데이터가 전달되기 때문
  - POST : 보안에 우수, 대량의 데이터 전송 가능
            글쓰기, 사진업로드, 동영상 업로드 등등 해당
  - 동적 파라미터
    - URL 에 데이터를 실어서 보내는 방식
    - URL이 무한대로 생성될 수 있다.
  - 클라이언트가 서버로 보내는 모든 행위는 => request라고 정의
    - request 객체를 타고 들어온다  
 '''
from flask import Flask, render_template, request


print(__name__)
app = Flask(__name__)

# 아무런 method에 대한 표시가 없다 => GET방식으로 라우팅 처리되었다 인식


@app.route('/login')
def login():
    return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)
    pass
