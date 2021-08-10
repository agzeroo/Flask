# Flask 기본 템플릿

# 1. 모듈 가져오기
from flask import Flask, render_template

# 2. 앱 생성 (flask 객체 생성)
app = Flask(__name__)

# 3. 라우팅


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/formUpload')
def formUpload():
    return render_template('formUpload.html')


@app.route('/ajaxUpload')
def ajaxUpload():
    return render_template('ajaxUpload.html')


@app.route('/webcamUpload')
def webcamUpload():
    return render_template('webcamUpload.html')


# 4. 서버 가동
if __name__ == '__main__':
    app.run(debug=True)
    pass
