import memcache
import mysql.connector
from flask import Flask, redirect, url_for, request,render_template
import timeit
import hashlib
import random

app = Flask(__name__)



@app.route('/')
def upload():
    #cursor = connection.cursor()
    return render_template("test.html")


if __name__ == '__main__':
    app.run()