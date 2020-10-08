import hashlib
import random

import requests
from urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


class MT5WebAPIClient:
    def __init__(self, address, agent='MT5WebAPIClient', api_version=2280, cert=None, cert_key=None,
                 cert_validate=None):
        self._agent = agent
        self._api_version = api_version
        self._address = address
        self._session = requests.Session()
        if cert is not None:
            self._session.cert = (cert, cert_key) if cert_key is not None else cert
        if cert_validate is not None:
            self._session.verify = cert_validate

    def authorize(self, login, password, type='manager'):
        response = self.get('auth_start',
                            params={'version': self._api_version, 'agent': self._agent, 'login': login, 'type': type})
        if response.status_code != 200:
            raise Exception('failed at authority start', response.text)
        body = response.json()
        if body['retcode'] != '0 Done':
            raise Exception('failed at authority start', response.text)

        server_rand = body['srv_rand']
        server_password_rand = self._get_password_rand(password, server_rand)

        client_rand = self._get_rand_value()
        client_password_rand = self._get_password_rand(password, client_rand)

        response = self.get('auth_answer', params={'srv_rand_answer': server_password_rand, 'cli_rand': client_rand})
        if response.status_code != 200:
            raise Exception('failed at authority answer', response.text)
        body = response.json()
        if body['retcode'] != '0 Done':
            raise Exception('failed at authority answer', response.text)

        if body['cli_rand_answer'] != client_password_rand:
            raise Exception('failed at authority answer, unexpected client password answer', response.text,
                            client_password_rand)

    def get(self, command, params=None):
        return self._session.get(self._address + '/' + str(command), params=params)

    def post(self, command, params=None, data=None, json=None):
        return self._session.post(self._address + '/' + str(command), params=params, data=data, json=json)

    @staticmethod
    def _get_rand_value():
        return ''.join(random.choice('0123456789abcdef') for _ in range(32))

    @staticmethod
    def _get_password_rand(password, rand_value):
        password_hash = hashlib.md5(hashlib.md5(password.encode('utf-16-le')).digest() + b'WebAPI').digest()
        return hashlib.md5(password_hash + bytes.fromhex(rand_value)).hexdigest()
