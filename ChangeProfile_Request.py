import requests
import json

class Connection(object):
    def _query_response(self):
        # if self.response.status_code not in (200,201,202):
        #     self.response.raise_for_status()
        #     print(f"The connection to {self.url} is failed")

        return json.loads(self.response.content.decode('utf8'))

    def __init__(self):
        self.url = 'http://mt5sharedservices.mt.qa-env.com:9977'
        self.session = requests.Session()
        self.headers = {'Content-type': 'application/json','Accept': 'text/plain','Content-Encoding': 'utf-8'}

    def Change_Profile_true_url(self,data):
        st = ''
        self.response = self.session.post(self.url + 'ChangeProfile',data=json.dumps(data), headers=self.headers)
        return self._query_response()

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