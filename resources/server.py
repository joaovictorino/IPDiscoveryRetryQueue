from flask import Flask
app = Flask(__name__)
import random
import requests


@app.route("/")
def index():
    if random.choice([True, False]):
        r = requests.get("http://ipinfo.io/ip")
        return r.text
    else:
        raise Exception("Erro no request!")

if __name__ == "__main__":
    app.run()