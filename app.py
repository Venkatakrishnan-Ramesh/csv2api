from flask import Flask, jsonify, request
import pandas as pd

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <h1>Hey There 👋</h1>
    <p>Head over to <a href="/api/v1?url=sample">Sample endpoint</a> to view a sample of the API and replace "sample" with a raw CSV url to get your Already configured, Production ready Backend!</p>
    """

@app.route('/api/v1')
def api():
    url = ''
    query = False

    if 'url' in request.args:
        url = request.args['url']
    else :
        return jsonify(
            message = "url not found"
        )
    if 'query' in request.args:
        query = request.args['query']
    

    if (query != ''):
        print("True")
        df =  pd.read_csv(url)
        df.query(query, inplace = True)
        data = df.to_dict('records')
    else:
        df = pd.read_csv(url)
        data = df.to_dict('records')
        #print(data)
        
    return str(data)


if __name__ == "__main__":
    app.run(debug=True)
