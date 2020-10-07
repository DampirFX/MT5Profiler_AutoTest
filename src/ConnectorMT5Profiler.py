import requests
import json


class Connection(object):
    def __init__(self):
        self.url = 'http://mt5sharedservices.mt.qa-env.com:9977/'
        self.session = requests.Session()
        self.session.headers.update = ({'Content-type': 'application/json', 'Accept': 'text/plain', 'Content-Encoding': 'utf-8'})

    def _query_response(self):
        # if self.response.status_code not in (200,201,202):
        #     self.response.raise_for_status()
        #     print(f"The connection to {self.url} is failed")

        return json.loads(self.response.content.decode('utf8'))

    def ReloadProfile_true_url(self):
        self.response = self.session.get(self.url + 'ReloadProfiles')
        return self._query_response()

    def ReloadProfile_false_url(self):
        self.response = self.session.get(self.url + 'ReloadProfilesfalseurl')
        return self._query_response()

    def Change_Profile_true_url(self,data):
        self.response = self.session.post(self.url + 'ChangeProfile',data=json.dumps(data))
        return self._query_response()

    def Change_Profile_false_url(self,data):
        self.response = self.session.post(self.url + 'ChangeProfilefalseurl',data=json.dumps(data))
        return self._query_response()

    def Change_Profile_wrong_json(self,data):
        self.response = self.session.post(self.url + 'ChangeProfile',data=data)
        return self._query_response()