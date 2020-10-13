import requests
from requests.exceptions import HTTPError
from retry import retry


class RequestServiceIP():

    @retry(HTTPError, tries=3)
    def call(self):
        response = requests.get("http://localhost:5000")
        response.raise_for_status()
        return response.text