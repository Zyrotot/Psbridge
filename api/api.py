import flask
from flask import request
from flask_cors import CORS
from control import *


app = flask.Flask(__name__)
CORS(app)
app.config["DEBUG"] = True


#Redireciona para a Home
@app.route('/', methods=["POST"])
def calcula():
    if request.method == "POST":
        req = request.json
        return achaNumero(req['number'])

#Handler do erro 404
@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404
    
app.run(host='0.0.0.0')