from flask import Flask
from jinja2.utils import generate_lorem_ipsum
import pandas as pd

app = Flask(__name__)

@app.route('/')
def home():
    return "home"

@app.route('/api/v1')
def api():
    return "api"


if __name__ == "__main__":
    app.run()