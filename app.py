from flask import Flask, request, jsonify
import pymysql
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


class Model():
    def getData(route,id):
        try:
            tableName=route
            db = pymysql.connect(host='', port=3306, user='mysqlId', passwd='123123', db='mydb', charset='utf8')
            cursor = db.cursor()
            cursor.execute(f"SELECT * FROM {tableName} WHERE id={id}")
            result = cursor.fetchall()
            cursor.commit()
            cursor.close()
            return result
        except:
            pass

    def getDatas(route,data):
        try:
            tableName=route
            db = pymysql.connect(host='', port=3306, user='mysqlId', passwd='123123', db='mydb', charset='utf8')
            cursor = db.cursor()
            cursor.execute(f"SELECT * FROM {tableName}")
            result = cursor.fetchall()
            cursor.commit()
            cursor.close()
            return result
        except:
            pass

    def postData(route,data):
        pass

    def patchData(route,data):
        pass

    def deleteData(route,data):
        pass
        
    route, method, data

if __name__ == '__main__':
    app.debug = False
    app.run(host='0.0.0.0')