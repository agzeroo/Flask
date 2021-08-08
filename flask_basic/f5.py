# 클라이언트가 서버측으로 데이터를 보낸다면?
# 파일을 보낸다
# Form 방식 전송, Method는 POST 방식
from flask import Flask, render_template, request

app = Flask(__name__)

# 클라이언트가 파일을 보내면 이를 받아서 저장한다
# 딥러닝으로 구축된 모델을 서버사이드에 배치
# 차후그림 -> 파일을 전처리 -> 모델로드 -> 예측모델에 입력 -> 예측 -> 결과를 응답(JSON)


@app.route('/upload', methods=["GET", "POST"])
def upload():
    if request.method == "GET":
        return render_template("upload.html")
    else:
        # 1. 클라이언트가 보낸 업로드한 파일을 획득
        f = request.files.get('file')
        print(f.filename)
        # 저장 (원하는 위치에 저장하겠다)
        # 통상 저장시에는 이름을 변조하여 처리한다(중복성 제거, 아이디, 시간, 해시 조합)
        path = f'./flask_basic/static/{f.filename}'
        f.save(path)
        # 2. 저장( 디스크에 저장, 저장 경로를 디비에 저장 )
        # 머신러닝 혹은 딥러닝 파트로써 (주피터, 코랩 등등) 학습후 모델을 덤프쳐서 가져온다
        # 산출물 : 덤프파일, 전처리 모듈(함수)
        # 3. 사전에 학습된 모델을 로드(매번 띠우는게 적합, 전역적으로 로딩후 사용)
        # 4. 업로드된 데이터를 전처리 (예측 모델에 입력할수 있는 형태로 가공)
        # 5. 데이터를 입력하여 예측 수행
        # 6. 예측 결과를 판단(?) 혹은 결과를 바로 전송 (JSON)
        # 7. 저장결과응답
        # form 방식이면 html로 응답 -> 파이썬으로 화면 구성(Jinja)로 처리
        # ajax 방식이면 json로 응답 -> js를 할줄 알아야 한다.
        # 더미로 결과를넣는다
        res = {
            "code": 0,
            "msg": "당신의 관상은 50대 이후에 돈을 잘 벌 관상이다..."
        }
        # predict : 예측결과
        return render_template('result.html', path=path[13:], predict=res)


if __name__ == '__main__':
    app.run(debug=True)
    pass
