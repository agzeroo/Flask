# 기본 템플릿
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/formUpload')
def formUpload():
    return render_template('pages/formUpload.html')

@app.route('/ajaxUpload')
def ajaxUpload():
    return render_template('pages/ajaxUpload.html')

@app.route('/webcamUpload')
def webcamUpload():
    return render_template('pages/webcamUpload.html')


if __name__ == '__main__':
    app.run(debug=True)
    pass