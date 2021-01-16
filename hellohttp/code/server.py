import datetime
from flask import Flask
from .handler import handle_echo
app = Flask("My hello world server")


@app.route('/')
def hello_world():
    now = datetime.datetime.now()
    return f'Hello, World {now}'


@app.route('/echo/<word>')
def echo(word):
    return handle_echo(word)
