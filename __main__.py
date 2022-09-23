from flask import Flask
from flask_table import Table, Col

class ItemTable(Table):
    startkm = Col('Anfangskilometerstand')
    endkm = Col('Endkilometerstand')
    enddestination = Col('Fahrtziel')
    driver = Col('Fahrer')
    licenseplate = Col('Kennzeichen')

items = ItemModel.query.all()
table = ItemTable(items)
app = Flask(__name__)

@app.route("/")
def render_html(table):
    return table