from flask import Flask, jsonify, request
import pandas as pd
import csv


app = Flask(__name__)

@app.route('/')
def home():
    return "home"

@app.route('/api/v1')
def api():
    url = ''

    if 'url' in request.args:
        url = request.args['url']
    else :
        return jsonify(
            message = "url not found"
        )
    
    df = pd.read_csv(url)
    data = df.to_dict('records')
    print(data)
    return str(data)


if __name__ == "__main__":
    app.run()
