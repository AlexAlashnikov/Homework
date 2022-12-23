from flask import Flask
from datetime import datetime
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return f"""Хотите узнать время, а может цитату Kenny West?
            Для того чтобы узнать текущее время, в адрессной строке добавь /time .
            А для просмотра цитаты добавь /quote ."""

@app.route('/quote')
def quote():
    result = requests.get('https://api.kanye.rest')
    return result.text

@app.route('/time')
def time():
    return f"Time {(datetime.now().time().replace(microsecond=0, tzinfo=None))}"

if __name__ == '__main__':
    app.run(debug=True)
