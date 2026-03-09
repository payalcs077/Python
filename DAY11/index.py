from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello Flask"

@app.route('/login')
def login():
    return "Click here to login"

@app.route('/signup')
def signup():
    return "Click here to signup"

@app.route('/contact')
def contact():
    return "Contact me"

app.run(debug = True)