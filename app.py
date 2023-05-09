from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "render_template('hello.html', name=name) << 와 같은 방식으로 html 파일을 client에게 전송합니다."

if __name__ == '__main__':
    app.debug = False
    app.run(host='0.0.0.0')