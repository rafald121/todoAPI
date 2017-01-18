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
    data = None
    responseData = None
    status = 400
    dataRead = False


    try:
        data = json.loads(request.data)
        dataRead = True
    except:
        responseData = {'error': 'bad request'}

    if dataRead:
        if 'login' in data and 'password' in data:
            if usersDict[data['login']]['password'] == data['password']:
                responseData = {
                    'message': "OK",
                    'token': usersDict[data['login']]['token'],
                    }
                status = 200
            else:
                responseData = {'error', 'Nie poprawny login lub haslo'}
        else:
            response_data = {'error': 'Brak loginu lub hasla'}

    headers = {'Content-Type': 'application/json'}
    response = Response(json.dumps(responseData),
                        status=status,
                        mimetype = "application/json",
                        headers=headers)
    return response


    # if dataRead:
    #     if 'login' in dataFromClientRequest and 'password' in dataFromClientRequest:
    #         if dataFromClientRequest['login'] in usersDict:
    #             if dataFromClientRequest['password'] == usersDict[dataFromClientRequest['login']]['password']:
    #
    #                 responseData['info'] = 'OK'
    #                 responseData['token'] = usersDict[dataFromClientRequest['login']]['token']
    #                 responseData['userID'] = usersDict[dataFromClientRequest['login']]['userID']
    #
    #                 status = 200
    #
    #             else:
    #                 responseData = {'error': 'podane hasło jest nieprawidłowe'}
    #         else:
    #             responseData = {'error': 'uzytkownik nie istnieje'}
    #     else:
    #         responseData = {'error': 'nie podano loginu lub hasła'}
    # else:
    #     responseData = {'error': 'data from client request was not read'}
    #
    # headers = {'Content-Type': 'application/json'}
    #
    # responseJson = json.dumps(responseData)
    # responseToClient = Response(responseJson, status=status, mimetype="application/json", headers=headers)
    # return responseToClient


if __name__ == '__main__':
    app.run(port=5000, debug=True)