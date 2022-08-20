from flask import Flask, render_template, url_for
import requests
import json
import urllib.request

app = Flask(__name__)

@app.route('/')
def index():
    url = "https://covid-193.p.rapidapi.com/history?country=search"
    querystring = {'Type Country': 'Here'}
    headers = {
        "X-RapidAPI-Key": "e9f92e15c1msh626754d27e3bdeep11c432jsn503c7e8afd67",
        "X-RapidAPI-Host": "covid-193.p.rapidapi.com"
        }
    response = requests.request("GET", url, headers=headers, params=querystring)
    data = response.read()
    dict = json.loads(data)
    print(dict)
    return render_template('index.html', covid=dict['results'])


@app.route('/covid_info')
def show_info():
    url = "https://covid-193.p.rapidapi.com/history?country=search"
    response = urllib.request.urlopen(url)
    data = response.read()
    dict = json.loads(data)
    data = []
    for data in dict["results"]:
        data = {
            "country": data["country"],
            "history": data["history"]
            }
    data.append(data)
    return {"results": data}