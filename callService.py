import requests
from requests.exceptions import HTTPError
from retry import retry

class CallService:

    @retry(HTTPError, tries=10)
    def call(self, body):
        response = requests.get("http://localhost:5000/{0}".format(body))
        response.raise_for_status()
        return response.text.strip()