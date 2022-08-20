from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'hello world'


#create a new route
#return 'hey there!'
@app.route('/hello')
def say_hello():
    return 'hey there!'

#create a route called classmates
#return a list of your classmates
@app.route('/classmates')
def get_classmates():
    return{"response_code":200, "data":['dan','pavel','enzo','son','priscilla','sanjeev']}


#use a route parameter
@app.route('/<name>')
def say_hello_with_name(name):
    return f'hey there {name}'


#implement a route that returns the classmate that matches an id


# /classmates/<id>
@app.route('/classmates/<id>')
def get_classmate(id):
    #create a list of dictionaries, wuth each name having an id
    names = [{"id":1, "name": "dan"},
        {"id":2, "name": "pavel"},
        {"id":3, "name": "enzo"},
        {"id":4, "name": "son"},
        {"id":5, "name": "priscilla"},
        {"id":6, "name": "sanjeev"}]
    #return the item that matches the id in the route
    for item in names:
        if item['id']==int(id):
            return item
    return {"response_code": 404}
#make sure that the items in the list are proper json (use double quotes)

if __name__ == 'main':
        app.run()