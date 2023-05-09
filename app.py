from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/')
def index():
    return "render_template('hello.html', name=name) << 와 같은 방식으로 html 파일을 client에게 전송합니다."

@app.route('/members',methods=["GET"])
def getMembers():
    result = jsonify({"data":"members정보들"})
    return result

@app.route('/members/<userId>',methods=["GET"])
def getMember(userId):
    result = jsonify({"data":f"특정 멤버 반환, userId = {userId}"})
    return result

@app.route('/members',methods=["POST"])
def postMember():
    payload = request.get_json()
    result = jsonify({"data":payload})
    return result

if __name__ == '__main__':
    app.debug = False
    app.run(host='0.0.0.0')