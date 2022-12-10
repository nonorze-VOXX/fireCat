from requests import request
from flask import Flask, request, render_template, redirect, url_for
import json
app = Flask(__name__)

@app.route("/",methods=["GET"])
def main():
    tem="404"
    with open ('../templates/chat.html', 'r') as file:
        tem=file.read()
    return tem 
@app.route("/hello")
def hello():
    return render_template('../templates/hello.html')

@app.route('/chat', methods=[ 'GET',"POST"])
def chatPage():
    tem=""
    if request.method == 'POST':
        user = request.form['user']
        print("post : user => ", user)
        with open ('testChat.txt', 'a') as file:
            file.writelines(user)
    
    with open ('../templates/chat.html', 'r') as file:
        tem=file.read()
    return tem 
    # return render_template('')

@app.route('/post', methods=[ 'POST'])
def pushInfo():
    print(request.data)
    return "ok"
@app.route('/get', methods=[ 'GET'])
def getInfo():
    # data=""
    data={"wtf":"hi"}
    # with open ('data.json', 'a') as file:
    #     data=file.read()
    response = app.response_class(
        response=json.dumps(data),
        # response=info,
        status=200,
        mimetype='application/json'
    )
    return response 

if __name__ == '__main__':
    app.run()
