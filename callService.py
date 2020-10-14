import requests

def call():
    response = requests.get('https://5000-eefd3e68-8302-4d0f-9f83-d35f34653766.ws-us02.gitpod.io/')
    response.raise_for_status()
    return response.text