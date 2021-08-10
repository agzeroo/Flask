# 기본 템플릿
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/formUpload', methods=["GET", "POST"])
def formUpload():
    if request.method == "GET":
        return render_template('pages/formUpload.html')
    else:        
        f = request.files.get('file')        
        path = f'./static/upload/{f.filename}'  # 저장경로
        print( path )
        f.save( path )                          # 저장
        # 데이터 전처리
        # 모델 로드
        # 예측 수행
        # 예측 결과 구성
        res = {
            "code":0,
            "msg":"당신의 관상은 50대 이후에 돈을 엄청 벌 관상입니다. ..."
        }
        # 결과를 가지고 응답 페이지 구성
        return render_template( "pages/formUpload_result.html", path=path[1:], predict=res )


@app.route('/ajaxUpload')
def ajaxUpload():
    return render_template('pages/ajaxUpload.html')

@app.route('/webcamUpload')
def webcamUpload():
    return render_template('pages/webcamUpload.html')


if __name__ == '__main__':
    app.run(debug=True)
    pass