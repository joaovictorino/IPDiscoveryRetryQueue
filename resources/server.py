from flask import Flask
app = Flask(__name__)
import random
import requests


@app.route("/")
@app.route("/<value>")
def index(value='ip'):
    if random.choice([True, False]):
        r = requests.get(f'http://ipinfo.io/{value}')
        return r.text
    else:
        raise Exception("Erro no request!")

if __name__ == "__main__":
    app.run()