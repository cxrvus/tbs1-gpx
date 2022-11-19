import flask
render_template = flask.render_template
app = flask.Flask(__name__)

@app.route('/')
def render_html():
    return render_template('index.html')