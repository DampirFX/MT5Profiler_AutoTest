import requests
import json


def trueurl(data):
    st = ''
    url = 'http://mt5sharedservices.mt.qa-env.com:9977/ChangeProfile'       #MT5 - .42:9968  MT4 - .135:9967
    headers = {'Content-type': 'application/json',    # Определение типа данных
               'Accept': 'text/plain',
               'Content-Encoding': 'utf-8'}
    answer = requests.post(url, data=json.dumps(data), headers=headers)
    FinishResult = answer.json()
    return FinishResult

def trueurl_without_json(data):
    st = ''
    url = 'http://mt5sharedservices.mt.qa-env.com:9977/ChangeProfile'       #MT5 - .42:9968  MT4 - .135:9967
    headers = {'Content-type': 'application/json',    # Определение типа данных
               'Accept': 'text/plain',
               'Content-Encoding': 'utf-8'}
    answer = requests.post(url, data=data, headers=headers)
    FinishResult = answer.json()
    return FinishResult

def falseurl(data):
    url = 'http://mt5sharedservices.mt.qa-env.com:9977/ChangeProfiletst'       #MT5 - .42:9966  MT4 - .135:9967
    headers = {'Content-type': 'application/json',    # Определение типа данных
               'Accept': 'text/plain',
               'Content-Encoding': 'utf-8'}
    answer = requests.post(url, data=json.dumps(data), headers=headers)
    FinishResult = answer.json()
    return FinishResult