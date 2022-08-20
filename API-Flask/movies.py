import json
from flask import Flask, render_template
import requests
import json

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    url = "https://movie-details1.p.rapidapi.com/imdb_api/movie"
    querystring = {"id":"tt0111161"}
    headers = {
	"X-RapidAPI-Key": "e9f92e15c1msh626754d27e3bdeep11c432jsn503c7e8afd67",
	"X-RapidAPI-Host": "movie-details1.p.rapidapi.com"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    data = response.read()
    dict = json.loads(data)
    print(dict)
    #return render_template('index.html', covid=dict['results'])