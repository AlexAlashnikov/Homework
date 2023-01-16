from flask import Blueprint, render_template, request, abort
import requests
from datetime import datetime
from .valid import Validator, Validation 


app1 = Blueprint('app1', __name__)

@app1.route('/')
def index():
    return render_template('index.html')

@app1.route('/quote')
def quote():
    number = request.args.get('number', 1)
    url = 'https://api.kanye.rest'
    res = [requests.get(url).json()['quote'] for i in range(int(number))]
    return f"Quote Kanye: {res}"


@app1.route('/register', methods=["POST", "GET"])
def register():
    if request.method == 'POST':
        username, password, email = request.form['username'], request.form['password'], request.form['email']
        validator = Validator(username, password, email)
        try:
            if validator.validation():
                abort(405)
        except Validation:
            abort(406)
    return render_template('reg.html')


@app1.errorhandler(405)
def valid_accept(error):
    return '<h1>Вы успешно зарегистрировались</h1>'

@app1.errorhandler(406)
def valid_error(error):
    return f"Validation Error"

@app1.route('/time')
def time():
    return f"Time {(datetime.now().time().replace(microsecond=0, tzinfo=None))}"

