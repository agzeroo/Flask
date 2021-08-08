# html을 읽어서 랝더링 처리 부분 (서버 사이드 랜더링:SSR)
# 서버측에서 html 을 완성해서 클라이언트한테 내려주는 형태
# render_template() 함수가 담당
# 원리 : html 파일(물리적존재)을 읽어서 데이터를 가미하여, 약간의 프로그래밍을 넣어서
#        동적으로  html을 만들어 준다
#        ->  jinja 템플릿 엔진을 이용하여서 render_template() 처리한다
# flask나 Django는  SSR 구현하기 위해서 템플릿 엔진을 사용 -> Jinja
# https://jinja.palletsprojects.com/en/3.0.x/

# html 파일들은 엔트리포인트 기준으로 경로법을 따진다
# /templates/*.html 이렇게 위치한다
# templates 이라는 폴더명은 blueprint에서 변경 가능하다. 여기서는 고정으로 사용
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html', name='데이터')


if __name__ == '__main__':
    app.run(debug=True)
    pass
