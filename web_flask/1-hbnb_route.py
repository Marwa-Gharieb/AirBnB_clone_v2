#!/usr/bin/python3
""""flask starts a web application"""
from flask import Flask

app = Flask(__name__)

@app.route("/", )
def saying_hello():
    return "Hello HBNB!"
    
if __name__=="__main__":
    app.run(host="0.0.0.0")