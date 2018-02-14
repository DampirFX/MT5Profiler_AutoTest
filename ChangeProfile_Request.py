import requests
import json
import My_Parser


def trueurl(data):
    st = ''
    url = 'http://172.16.1.42:9967ChangeProfile'       #MT5 - .42:9966  MT4 - .135:9967
    headers = {'Content-type': 'application/json',    # Определение типа данных
               'Accept': 'text/plain',
               'Content-Encoding': 'utf-8'}
    answer = requests.post(url, data=json.dumps(data), headers=headers)
    st = answer.text
    FinishResult = My_Parser.parsers(st)
    #print(st)
    return FinishResult
def falseurl(data):
    url = 'http://172.16.1.42:9967ChangeProfile'       #MT5 - .42:9966  MT4 - .135:9967
    headers = {'Content-type': 'application/json',    # Определение типа данных
               'Accept': 'text/plain',
               'Content-Encoding': 'utf-8'}
    answer = requests.post(url, data=json.dumps(data), headers=headers)
    st = answer.text
    FinishResult = My_Parser.parsers(st)
    return FinishResult