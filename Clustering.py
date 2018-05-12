import numpy as np
import matplotlib.pyplot as plt
from numpy import genfromtxt
from sklearn.cluster import KMeans
import csv
import sklearn.metrics as sm
import collections


my_data = genfromtxt('iris.csv', delimiter=',')

kmeans = KMeans(n_clusters=3)
kmeans.fit(my_data)

centriods = kmeans.cluster_centers_
labels = kmeans.labels_

print (centriods)
print (labels)

counter=collections.Counter(labels)



colors = ["g.","r.","b.","p."]

for i in range(len(my_data)):
    # print "%s %s"%(my_data[i][0],my_data[i][1])
    plt.plot(my_data[i][0],my_data[i][1],colors[labels[i]],markersize=10)

plt.scatter(centriods[:,0],centriods[:,1],marker="x",s=150,linewidths=5,zorder = 10)
plt.show()


plt.rcdefaults()
fig, ax = plt.subplots()

# Example data
label_header = ('A', 'B','C')
y_pos = np.arange(len(label_header))

ax.bar(y_pos, counter.values(), align='center',
        color='green')
ax.set_xticks(y_pos)
ax.set_xticklabels(label_header)
# ax.invert_yaxis()  # labels read top-to-bottom
ax.set_ylabel('Cluster Size')
ax.set_xlabel('Cluster Name')
# plt.savefig("A.jpg")
plt.show()


colors = ["#E13F29", "#D69A80", "#D63B59"]

fig1, ax1 = plt.subplots()
explode = (0, 0.1, 0)
ax1.pie(counter.values(), explode=explode, labels=y_pos, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()


