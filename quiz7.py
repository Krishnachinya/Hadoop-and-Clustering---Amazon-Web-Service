from flask import Flask, redirect, url_for, request,render_template
import timeit
import hashlib
import random
import os

app = Flask(__name__)


@app.route('/')
def upload():
    return render_template("Display.html")



if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)
