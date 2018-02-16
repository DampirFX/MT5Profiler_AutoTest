import requests
import json
import My_Parser


def trueurl(data):
    st = ''
    url = 'http://172.16.1.199:9968/ChangeProfile'       #MT5 - .42:9968  MT4 - .135:9967
    headers = {'Content-type': 'application/json',    # Определение типа данных
               'Accept': 'text/plain',
               'Content-Encoding': 'utf-8'}
    answer = requests.post(url, data=json.dumps(data), headers=headers)
    FinishResult = answer.json()
    return FinishResult

def falseurl(data):
    url = 'http://172.16.1.199:9968/ChangeProfiletst'       #MT5 - .42:9966  MT4 - .135:9967
    headers = {'Content-type': 'application/json',    # Определение типа данных
               'Accept': 'text/plain',
               'Content-Encoding': 'utf-8'}
    answer = requests.post(url, data=json.dumps(data), headers=headers)
    FinishResult = answer.json()
    return FinishResult
    return FinishResult