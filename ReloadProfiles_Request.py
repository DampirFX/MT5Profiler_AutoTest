import requests
import json


def reload_trueurl():
    url = 'http://172.16.1.42:9977/ReloadProfiles'       #MT5 - .42:9968  MT4 - .135:9967
    headers = {'Content-type': 'application/json',    # Определение типа данных
               'Accept': 'text/plain',
               'Content-Encoding': 'utf-8'}
    answer = requests.get(url, headers=headers)
    FinishResult = answer.json()
    return FinishResult

def reload_falseurl():
    url = 'http://172.16.1.42:9977/ReloadProfilestst'       #MT5 - .42:9966  MT4 - .135:9967
    headers = {'Content-type': 'application/json',    # Определение типа данных
               'Accept': 'text/plain',
               'Content-Encoding': 'utf-8'}
    answer = requests.get(url, headers=headers)
    FinishResult = answer.json()
    return FinishResult