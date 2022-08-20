from flask import Flask, render_template
import requests
import json


app = Flask(__name__)


@app.route('/')
def index():
    url = "https://covid-193.p.rapidapi.com/history?country=search"

    querystring ={'Name of a country'}

    headers = {
	    "X-RapidAPI-Key": "e9f92e15c1msh626754d27e3bdeep11c432jsn503c7e8afd67",
	    "X-RapidAPI-Host": "covid-193.p.rapidapi.com"
    }
    response = requests.request("GET", url, headers=headers, params = querystring)
    data = response.read()
    dict = json.loads(data)
    #print(dict)
    return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True)