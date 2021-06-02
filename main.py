from flask import Flask, g 
import pymysql
from os import environ
import logging, logging.handlers
from api import comment_api 

app = Flask(__name__)

app.secret_key = b"1722a28089f91b73fff8708c26800a5e"

app.register_blueprint(comment_api, url_prefix="/api/comment")

def connect_db():
    host = environ.get("MYSQL_HOST")
    user = environ.get("MYSQL_USER", "root")
    passwd = environ.get("MYSQL_PWD")
    
    return pymysql.connect(
        host = host,
        port = 3306,
        user = user,
        passwd = passwd,
        database = "wall"
        )

@app.before_request
def before_request():
    if not hasattr(g, 'db'):
        g.db = connect_db()

@app.teardown_appcontext
def teardown_appcontext(error):
    if hasattr(g, 'db'):
        g.db.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

