# 기본으로 깔고 시작#
from flask import Flask


print(__name__)
app = Flask(__name__)


@app.route('/')
def home():
    return 'home page 3'


if __name__ == '__main__':
    app.run(debug=True)
    pass
