# from flask import Flask
import flask
app = flask.Flask(__name__)


site = """
<html>
<head>
<script>
alert('lolxd')
</script>
</head>
<body>
<div id="my_div" style="height:100px;width:100px;background-color:green"></div>
<button onclick="my_div.style.backgroundColor='blue'">BRUH</button>
</body>
</html>
"""


@app.route('/')
def render_html():
    return site