# -*- coding: utf-8 -*-
from flask import Flask, request, json, Response

app = Flask(__name__)

usersDict = {}
usersDict['rafal'] = {'token': 'rafaltoken', 'password': 'rafal', 'userID': 1}
usersDict['pawel'] = {'token': 'paweltoken', 'password': 'pawel', 'userID': 2}
usersDict['piotr'] = {'token': 'piotrtoken', 'password': 'piotr', 'userID': 3}

tasksDict = {}


@app.route('/login', methods=['POST'])
def login():
    requestData = None
    responseData = None
    status = 400
    requestDataRead = False

    try:
        requestData = json.loads(request.data)
        requestDataRead = True
    except:
        responseData = {'error': 'bad request'}

    if requestDataRead:
        if 'login' in requestData and 'password' in requestData:
            if usersDict[requestData['login']]['password'] == requestData['password']:
                responseData = {
                    'message': "OK",
                    'token': usersDict[requestData['login']]['token'],
                    }
                status = 200
            else:
                responseData = {'error', 'Nie poprawny login lub haslo'}
        else:
            responseData = {'error': 'Brak loginu lub hasla'}

    responseJsonData = json.dumps(responseData)
    responseHeaders = {'Content-Type': 'application/json'}
    response = Response(responseJsonData,
                        status=status,
                        mimetype = "application/json",
                        headers=responseHeaders)
    return response



if __name__ == '__main__':
    app.run(port=5000, debug=True)