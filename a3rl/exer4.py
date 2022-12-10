from turtle import color
import matplotlib . pyplot as plt
import numpy as np
from sklearn.cluster import AgglomerativeClustering
from scipy.cluster import hierarchy
import seaborn as sns
import math
import csv
import pandas as pd
from sklearn.cluster import DBSCAN
from sklearn import metrics
from sklearn.datasets import make_blobs
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
from random import randrange

import sys
sys.setrecursionlimit(2000)
            
alfaDistance = 5
howManyPoints = 500
howManyPointsTotal = howManyPoints * 2 

mean = [3, 3]
cov = [[1 , 0], [0 , 1]]
setA = np.random.multivariate_normal(mean, cov, howManyPoints).T
mean = [-3, -3]
cov = [[2, 0], [0 , 5]]
setB = np.random.multivariate_normal(mean, cov, howManyPoints).T

setC = np.concatenate((setA, setB), axis = 1)
setC = setC.T
np.random.shuffle(setC)
setC = setC.T

setCX = setC[0]
setCY = setC[1]

klusterFinalX = []
klusterFinalY = []

#while len(setCX) > 0:
#    indexToRemove = []
#    klusterAuxX = []
#    klusterAuxY = []
#    r = randrange(0, len(setCX))
#    pX = setCX[r]
#    pY = setCY[r]
#    for i in range(len(setCX)):
#        if math.dist([pX, pY], [setCX[i], setCY[i]]) <= alfaDistance:
#            howManyPointsTotal -= 1            
#            klusterAuxX.append(setCX[i])
#            klusterAuxY.append(setCY[i])
#            pX = setCX[i]
#            pY = setCY[i]
#            indexToRemove.append(i)
#    setCXaux = setCX
#    setCYaux = setCY
#    for j in range(len(indexToRemove)):
#        setCXaux = np.delete(setCX, indexToRemove[j])
#        setCYaux = np.delete(setCY, indexToRemove[j])
#    
#    setCX = setCXaux
#    setCY = setCYaux
#    
#    klusterFinalX.append(klusterAuxX) 
#    klusterFinalY.append(klusterAuxY) 
    

################## SECOND implementation
labels_true = []
points = []
for i in range(howManyPoints):
    points.append([setCX[i], setCY[i]])
    labels_true.append(0)

X = StandardScaler().fit_transform(points)

db = DBSCAN(eps=0.3, min_samples=10).fit(X)
core_samples_mask = np.zeros_like(db.labels_, dtype=bool)
core_samples_mask[db.core_sample_indices_] = True
labels = db.labels_

# Number of clusters in labels, ignoring noise if present.
n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
n_noise_ = list(labels).count(-1)

print("Estimated number of clusters: %d" % n_clusters_)
print("Estimated number of noise points: %d" % n_noise_)
print("Homogeneity: %0.3f" % metrics.homogeneity_score(labels_true, labels))
print("Completeness: %0.3f" % metrics.completeness_score(labels_true, labels))
print("V-measure: %0.3f" % metrics.v_measure_score(labels_true, labels))
print("Adjusted Rand Index: %0.3f" % metrics.adjusted_rand_score(labels_true, labels))
print(
    "Adjusted Mutual Information: %0.3f"
    % metrics.adjusted_mutual_info_score(labels_true, labels)
)
unique_labels = set(labels)
colors = [plt.cm.Spectral(each) for each in np.linspace(0, 1, len(unique_labels))]
for k, col in zip(unique_labels, colors):
    if k == -1:
        col = [0, 0, 0, 1]
    class_member_mask = labels == k
    xy = X[class_member_mask & core_samples_mask]
    plt.plot(
        xy[:, 0],
        xy[:, 1],
        "o",
        markerfacecolor=tuple(col),
        markeredgecolor="k",
        markersize=14,
    )
    xy = X[class_member_mask & ~core_samples_mask]
    plt.plot(
        xy[:, 0],
        xy[:, 1],
        "o",
        markerfacecolor=tuple(col),
        markeredgecolor="k",
        markersize=6,
    )
plt.title("Estimated number of clusters: %d" % n_clusters_)
plt.show()