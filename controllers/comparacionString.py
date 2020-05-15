from app import app
from flask import flash, jsonify, request
import difflib


@app.route('/', methods=['GET'])
def Bienvenida():
    return 'Microservicio Utils Python'


@app.route('/string-comparacion', methods=['POST'])
def compararString():
    _json = request.json
    if _json['string1'] and _json['string2'] and _json['score']:
        _score = round(difflib.SequenceMatcher(
            None, _json['string1'], _json['string2']).ratio()*100, 1)
        print('Score Resultante : {} , Score Minimo : {}'.format(
            _score, _json['score']))
        if _json['score'] <= _score:
            response = {'codRes': '00', 'score': _score}
        else:
            response = {'codRes': '02', 'score': _score}
    else:
        response = {'codRes': '01', 'message': 'Falta de string'}

    return response


@app.route('/array-comparacion', methods=['POST'])
def comparacionArray():
    response = []
    _json = request.json
    array1 = _json['string1'].split(' ')
    array2 = _json['string2'].split(' ')
    for array_list in array1:
        _score = difflib.get_close_matches(
            array_list, array2, n=1, cutoff=_json['score'])
        if(_score):
            response.append(True)
    if len(array1) == len(response):
        return { 'codRes':'00', 'score':'Aprobado'}
    else:
        return { 'codRes':'02', 'score':'Desaprobado'}
