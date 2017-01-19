# -*- coding: utf-8 -*-
from flask import Flask, request, json, Response

app = Flask(__name__)

# OPTIONAL TO ADD LATER
# getTimeAndData to single task when client send request

usersDict = {}
usersDict['rafal'] = {'token': 'rafaltoken', 'password': 'rafal', 'userID': 1, 'tasks': {}}
# usersDict['pawel'] = {'token': 'paweltoken', 'password': 'pawel', 'userID': 2}
# usersDict['piotr'] = {'token': 'piotrtoken', 'password': 'piotr', 'userID': 3}

tasksDict = {}
tasksDict[1] = {"title": "Projekt z programowania internetowego",
                "details": "Projekt, w którym piszemy własną usługę sieciową + 2 rodzaje klientów",
                "timeToDo": "30.01.2016",
                "tag": ["school"],
                "done": 0,
                "id": 1
                }
tasksDict[2] = {"title": "Sprzątnięćie kuchni",
                "details": "Dokładne wyczyszczenie kuchenki i mikrofali",
                "timeToDo": "15.02.2016",
                "tag": ["home"],
                "done": 0,
                "id": 2
                }
tasksDict[3] = {"title": "Specyfikacja dla klienta",
                "details": "Napisanie szczegółowej specyfikacji dla klienta dotyczącej aplikacji",
                "timeToDo": "25.09.2016",
                "tag": ["work"],
                "done": 0,
                "id": 3
                }


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
        responseData = {'error': 'nie moglem odczytac danych z requestu, ktory wyslal klient'}

    if requestDataRead:
        if 'login' in requestData and 'password' in requestData:
            if requestData['login'] in usersDict:
                if usersDict[requestData['login']]['password'] == requestData['password']:
                    responseData = {
                        'info': "OK",
                        'token': usersDict[requestData['login']]['token'],
                        'userID': usersDict[requestData['login']]['userID']
                    }
                    status = 200
                else:
                    responseData = {'error': 'Niepoprawny login lub haslo'}
            else:
                responseData = {'error': 'Brak uzytkownika o podanym loginie w bazie danych'}
        else:
            responseData = {'error': 'Brak loginu lub hasla'}

    responseJsonData = json.dumps(responseData)
    responseHeaders = {'Content-Type': 'application/json'}
    response = Response(responseJsonData,
                        status=status,
                        mimetype="application/json",
                        headers=responseHeaders)
    return response


@app.route("/notdone", methods=['GET'])
def notdone():
    requestData = None
    requestDataRead = False
    responseJsonData = None
    status = 400
    responseData = None

    try:
        requestData = json.loads(request.data)
        requestDataRead = True
    except:
        responseData = {"error": "bad token give to request"}

    if requestDataRead:
        # TODO add searching login based on given in request token

        if requestData['token'] == usersDict['rafal']['token']:

            # TODO dodac funkcje, ktora liczy niewykonane zadania
            responseData = {"undone": 3}
            status = 200
        else:
            responseData = {
                "error": "couldn't match login to requested token(probably there isn't any user with requested token)"}
    else:
        responseData = {"error": "bad syntax of request(bad oken has been given"}

    responseJsonData = json.dumps(responseData)
    responseHeaders = {'Content-Type': 'application/json'}
    response = Response(responseJsonData,
                        status=status,
                        mimetype="application/json",
                        headers=responseHeaders)

    return response


# def countUndoneTask():


if __name__ == '__main__':
    app.run(port=5000, debug=True)
