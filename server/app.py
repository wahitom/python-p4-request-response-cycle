#!/usr/bin/env python3
import os

from flask import Flask, request, current_app, g

app = Flask(__name__)

@app.before_request
def app_path():
    g.path = os.path.abspath(os.getcwd()) # this returns the current working directory as a string 
    # current working directory is the directory from which the script is run 

@app.route('/')
def index():
    host = request.headers.get('Host')
    appname = current_app.name
    return f'''<h1>The host for this page is {host}</h1>
               <h2>The name of this application is {appname}</h2
               <h2>The path of this app is on the user's device us {g.path}</h2>'''

    # use make_response() for a more object-oriented approach to responses 

    status_code = 200
    headers = {}

    return make_response(response_body, status_code, headers)

if __name__ == '__main__':
    app.run(port=5555)
