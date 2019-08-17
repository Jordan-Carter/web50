from flask import Flask, render_template, request, session
from flask_session import Session

app = Flask(__name__)

app.config['SESSION_PERMANENT'] = False
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

@app.route("/", methods = ['POST', 'GET'])
def index(): 
    if session.get('items') is None:
        session['items'] = []   
    if request.method == 'POST':
        item = request.form.get('item')
        session['items'].append(item)
        if request.form.get('clearButton'):
            session['items'].clear()

    lorem = True
    header = "Welcome"
    return render_template('index.html', header=header, lorem=lorem, items=session['items'])

@app.route("/<string:name>")
def hello(name):
    name = name.capitalize
    return f"hello {name}"



