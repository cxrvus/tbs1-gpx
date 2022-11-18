# from flask import Flask
import flask
render_template = flask.render_template
import os
app = flask.Flask(__name__)


# script = '\n'.join(open('templates/index.js','r'))

@app.route('/')
def render_html():
    return render_template('index.html')