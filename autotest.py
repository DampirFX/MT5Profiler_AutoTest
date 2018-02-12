import requests
import json
import Myparser
from datetime import datetime


filename = datetime.now().strftime("%Y%m%d")
f = open(filename + '.log', 'a+')
f.write(datetime.now().strftime("%H:%M:%S") + '   Start testing\n')
const_url = 'http://172.16.1.42:9967ChangeProfile?ProfileName=America'
const_headers = {'Content-type': 'application/json',  # Определение типа данных
                 'Accept': 'text/plain',
                 'Content-Encoding': 'utf-8'}
###################################################################
#
f.write(datetime.now().strftime("%H:%M:%S") + '   Test 1\n')
print('\nTest №1')
st = ''
url = const_url
headers = const_headers
#data = {}
answer = requests.get(url, headers=headers)
st = answer.text
FinishResult = Myparser.parsers(st)
if FinishResult[0] == 'Done':
    if FinishResult[1] == 0:
        if FinishResult[2][0]["Description"] == 'Done' and FinishResult[2][0]["Server"] == 60 and FinishResult[2][0]["Status"] == 0:
            print('result - OK')
            f.write(datetime.now().strftime("%H:%M:%S") + '   result - OK\n')
        else:
            print('result - failed')
            f.write(datetime.now().strftime("%H:%M:%S") + '   result - failed\n')
    else:
        print('result - failed: wrong status')
        f.write(datetime.now().strftime("%H:%M:%S") + '   result - failed: wrong status\n')
else:
    print('result - failed: wrong response')
    f.write(datetime.now().strftime("%H:%M:%S") + '   result - failed: wrong response\n')
###################################################################
f.write(datetime.now().strftime("%H:%M:%S") + '   Finish testing\n')
f.close()