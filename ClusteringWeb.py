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


app = Flask(__name__)

@app.route('/')
def upload():
    #cursor = connection.cursor()
    return render_template("Display.html")

@app.route('/Kmeans',methods=['POST'])
def Kmeans():
    if request.method == 'POST':
        type = "";
        K_value = request.form['kvalue']
        m_cache = int(request.form['one'])
        col1 = request.form['col1']
        col2 = request.form['col2']
        csvdata = genfromtxt('data1.csv', delimiter=',')
        kmeans = KMeans(n_clusters=int(K_value))
        kmeans.fit(csvdata[:,[1,2]])
        centriods = kmeans.cluster_centers_
        labels = kmeans.labels_
        #
        # print (centriods)
        # print (labels)
        counter = collections.Counter(labels)
        if m_cache == 1:
            colors = ["g.", "r.", "b.", "c.","y."]
            print (centriods)
            print (labels)

            for i in range(len(csvdata)):
                print "%s %s" % (csvdata[i][0], csvdata[i][1])
                plt.plot(csvdata[i][0], csvdata[i][1], colors[labels[i]], markersize=10)
            plt.scatter(centriods[:, 0], centriods[:, 1], marker="x", s=150, linewidths=5, zorder=10)
            plt.savefig('static/scatterplot.png')
            type = "scatter"
            # plt.show()
        elif m_cache == 2:
            plt.rcdefaults()
            fig, ax = plt.subplots()
            label_header = ('A', 'B', 'C','D','E')
            y_label = np.arange(len(label_header))
            ax.bar(y_label, counter.values(), align='center',
                   color='green')
            ax.set_xticks(y_label)
            ax.set_xticklabels(label_header)
            # ax.invert_yaxis()  # labels read top-to-bottom
            ax.set_ylabel('Cluster Size')
            ax.set_xlabel('Cluster Name')
            plt.savefig('static/bar.png')
            type = "bar"
            # plt.savefig("A.jpg")
            # plt.show()
        else:
            colors = ["#E13F29", "#D69A80", "#D63B59","#D69A80", "#D63B59"]
            fig1, ax1 = plt.subplots()
            explode = (0, 0.1, 0)
            label_header = ('A', 'B', 'C')
            y_label = np.arange(len(label_header))
            ax1.pie(counter.values(), explode=explode, labels=y_label, autopct='%1.1f%%',
                    shadow=True, startangle=90)
            ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
            plt.savefig('static/pie.png')
            type = "pie"

    if type == "scatter":
        return render_template("Graph.html",imagename = 'scatterplot.png')
    elif type == "bar":
        return render_template("Graph.html",imagename = 'bar.png')
    else:
        return render_template("Graph.html", imagename = 'pie.png')

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)