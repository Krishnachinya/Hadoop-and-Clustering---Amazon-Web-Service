import memcache
import mysql.connector
from flask import Flask, redirect, url_for, request,render_template
import timeit
import hashlib
import random
import numpy as np
import matplotlib.pyplot as plt
from numpy import genfromtxt
from sklearn.cluster import KMeans
import csv
import sklearn.metrics as sm
import collections
import pygal
import boto3
from docutils.writers.s5_html import themes_dir_path
from flask import Flask ,redirect, url_for, request,render_template
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

Uploadpath = "/home/ubuntu/Upload"
Downloadpath = "/home/ubuntu/Download"

@app.route('/')
def upload():
    return render_template("Upload.html")


@app.route('/uploader', methods=['POST','GET'])
def uploader():
    if request.method == 'POST':
        file = request.files['file']

        filename = secure_filename(file.filename)
        file.save(os.path.join(Uploadpath, filename))
    return "File Uploaded to EC2 successfully"



start_time = timeit.default_timer()
my_data = genfromtxt('data1.csv', delimiter=',')
kmeans = KMeans(n_clusters=5)
kmeans.fit(my_data)

centriods = kmeans.cluster_centers_
labels = kmeans.labels_
finish_time = timeit.default_timer() - start_time

print "Time Taken is %s"%(str(finish_time))
print (centriods)
print (labels)

print "Centeriod is %s %s"%(centriods[:, 0], centriods[:, 1])

for i in range(len(my_data)):
    print "%s %s"%(my_data[i][0],my_data[i][1])


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)
