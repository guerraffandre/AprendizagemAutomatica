from turtle import color
import matplotlib . pyplot as plt
import numpy as np
import math
from sklearn.cluster import AgglomerativeClustering
from scipy.cluster import hierarchy
import seaborn as sns
import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage

alfa = 0.5  #0.00001
howManyPoints = 100

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

data = list(zip(setCX, setCY))
linkage_data = linkage(data, method='ward', metric='euclidean')
dendrogram(linkage_data)
plt.show()

distance = 10000
positionClosestX1 = 0
positionClosestY1 = 0
positionClosestX2 = 0
positionClosestY2 = 0
auxI = 0
auxJ = 0
px = []
py = []

while len(setCX) > 1:    
    distance = 10000                
    for i in range(len(setCX)-1):    
        for j in range(len(setCX)-1):        
            if math.dist([setCX[j], setCY[j]], [setCX[i], setCY[i]]) < distance and setCX[j] != setCX[i] and setCY[j] != setCY[i]:
                distance = math.dist([setCX[j], setCY[j]], [setCX[i], setCY[i]])
                positionClosestX1 = setCX[j]
                positionClosestY1 = setCY[j]
                positionClosestX2 = setCX[i]
                positionClosestY2 = setCY[i]
                auxI = i
                auxJ = j
                
    setCX = np.delete(setCX, i)
    setCY = np.delete(setCY, i)
    setCX = np.delete(setCX, j)
    setCY = np.delete(setCY, j)
    setCX = np.append(setCX, [(positionClosestX1 + positionClosestX2) / 2])
    setCY = np.append(setCY, [(positionClosestY1 + positionClosestY2) / 2])
    px.append((positionClosestX1 + positionClosestX2) / 2)
    py.append((positionClosestY1 + positionClosestY2) / 2)
    
    