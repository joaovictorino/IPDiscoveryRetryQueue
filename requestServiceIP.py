import requests
from requests.exceptions import HTTPError
from retry import retry


class RequestServiceIP():

    @retry(HTTPError, tries=3)
    def call(self, body):
        response = requests.get(f'http://localhost:5000/{body}')
        response.raise_for_status()
        return response.text