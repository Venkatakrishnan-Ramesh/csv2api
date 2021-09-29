from flask import Flask, jsonify, request
import pandas as pd

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <h1>Hey There 👋</h1>
    <p>head over to <a href="/api/v1?url=sample">Endpoint</a> to view a sample of the API and replace sample with a raw CSV link to get your production ready Backend, already configured for you</p>
    """

@app.route('/api/v1')
def api():
    url = ''

    if 'url' in request.args:
        url = request.args['url']
    else :
        return jsonify(
            message = "url not found"
        )
    
    if (url == 'sample'):
        df = pd.read_csv('https://raw.githubusercontent.com/dev-Roshan-lab/csv2api/main/sample.csv?token=APHBO3A3CRITP2ZMRKMOIBDBLV2D4')
        data = df.to_dict('records')
        return jsonify(data)
    else:
        df = pd.read_csv(url)
        data = df.to_dict('records')
        return jsonify(data)


if __name__ == "__main__":
    app.run()
