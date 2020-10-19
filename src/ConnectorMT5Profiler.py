import requests
import json
import os


class Connection_To_MT5Profiler(object):
    def __init__(self):
        with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'credentials.json'), "r") as read_file:
            self.data_set = json.load(read_file)
        self.session = requests.Session()
        self.session.headers.update = ({'Content-type': 'application/json', 'Accept': 'text/plain', 'Content-Encoding': 'utf-8'})

    def _query_response(self):
        # if self.response.status_code not in (200,201,202):
        #     self.response.raise_for_status()
        #     print(f"The connection to {self.url} is failed")

        return json.loads(self.response.content.decode('utf8'))

    def ReloadProfile_true_url(self):
        self.response = self.session.get(self.data_set["uri"] + 'ReloadProfiles')
        return self._query_response()

    def ReloadProfile_false_url(self):
        self.response = self.session.get(self.data_set["uri"] + 'ReloadProfilesfalseurl')
        return self._query_response()

    def Change_Profile_true_url(self,data):
        self.response = self.session.post(self.data_set["uri"] + 'ChangeProfile', data=json.dumps(data))
        return self._query_response()

    def Change_Profile_false_url(self,data):
        self.response = self.session.post(self.data_set["uri"] + 'ChangeProfilefalseurl', data=json.dumps(data))
        return self._query_response()

    def Change_Profile_wrong_json(self,data):
        self.response = self.session.post(self.data_set["uri"] + 'ChangeProfile', data=data)
        return self._query_response()

    def Change_Server_Settings(self,data):
        self.response = self.session.post(self.data_set["uri"] + 'ChangeServerSettings', data=json.dumps(data))
        return self._query_response()