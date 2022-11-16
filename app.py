from flask import Flask
app = Flask(__name__)

@app.route('/')
def render_html():
    return '<p> Hallo </p>'