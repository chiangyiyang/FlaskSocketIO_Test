#!/usr/bin/python
# -*- coding: UTF-8 -*-


from flask import Flask, render_template
from flask_socketio import SocketIO

import thread_test as tt

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!123456'
socketio = SocketIO(app)

@app.route("/")
def hello():
    return "Hello World! 456"

@app.route("/ws")
def hellows():
    return render_template('index.html')


@socketio.on('my event')
def handle_my_custom_event(json):
    print('received json: ' + str(json))

@socketio.on('car event')
def handle_car_event(json):
    print('received car cmd: ' + str(json))

if __name__ == '__main__':
    socketio.run(app)
