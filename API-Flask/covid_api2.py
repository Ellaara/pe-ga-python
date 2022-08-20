from crypt import methods
from select import select
import pandas as pd
from flask import Flask, render_template, requests, redirect, url_for

import json

app = Flask(__name__)

@app.route('/', methods=['GET'])
def show_history():

    url = "https://covid-193.p.rapidapi.com/history?country=search"
    querystring ={"limit": "country", "page": "0", "per_page": "10"}

    headers = {
	    "X-RapidAPI-Key": "e9f92e15c1msh626754d27e3bdeep11c432jsn503c7e8afd67",
	    "X-RapidAPI-Host": "covid-193.p.rapidapi.com"
    }
    response = requests.request("GET", url, headers=headers, params = querystring)

    data = response.json()

    return render_template('countries.html')

@app.route("/covid")
def get_statistics():
    url = 'https://covid-193.p.rapidapi.com/statistics'
    headers = {
        "X-RapidAPI-Key": "a88e006cccmshd995b917aac7424p1d5d44jsne39acecf3898",
        "X-RapidAPI-Host": "covid-193.p.rapidapi.com"
    }
    response = requests.request("GET", url, headers=headers)
    print(response.json())
    data = response.json()
    

    covid_data = []
    
    for cases in data:
        cases = {
            "new_cases" : covid_data["cases.new"],
            "active_cases": covid_data["cases.active"],
            "cases_recovered": covid_data["cases.recovered"],
        }
        
        covid_data.append(cases)
    print(covid_data)
    return {"cases": covid_data}


if __name__ == '__main__':
    app.run(debug=True)