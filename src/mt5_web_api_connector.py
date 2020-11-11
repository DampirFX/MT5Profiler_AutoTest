from .mt5_web_api_client import MT5WebAPIClient
import json
import os


class MT5Connector(object):
    def __init__(self):
        with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'credentials.json'), "r") as read_file:
            self.data_set = json.load(read_file)
            self.address = f'https://{self.data_set["IP_MT5"]}:{self.data_set["PORT_MT5"]}'
            self.client = MT5WebAPIClient(address=self.address, cert_validate=False)
            self.client.authorize(self.data_set["LOGIN_MT5"], self.data_set["WEB_API_PASSWORD_MT5"])

    def get_symbols(self):
        response = self.client.get('symbol_list')

        if response.status_code != 200:
            raise RuntimeError(f'{self.address} returned status code {response.status_code}')

        response_json = response.json()
        if response_json['retcode'] != '0 Done':
            raise RuntimeError(
                f'{self.data_set["IP_MT5"]}/symbol_list returned json with status code {response_json["retcode"]}')

        result = response_json['answer']
        return result


    def get_symbol_settings(self,symbol:str):

        response = self.client.get('symbol_get',{'symbol': symbol})

        if response.status_code != 200:
            raise RuntimeError(f'{self.address} returned status code {response.status_code}')

        response_json = response.json()
        if response_json['retcode'] != '0 Done':
            raise RuntimeError(
                f'{self.data_set["IP_MT5"]}/get_symbol_settings returned json with status code {response_json["retcode"]}')

        result = response_json['answer']

        return result