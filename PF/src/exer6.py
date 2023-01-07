from Funcs import ImportData, ReadJson
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
from sklearn.cluster import KMeans
from sklearn.cluster import KMeans, DBSCAN
from sklearn.neighbors import NearestNeighbors

coluna1 = "aNatureza"
coluna2 = "aTraçado4"
df = pd.read_csv(os.getcwd()  + "\src\data\Data2000Exer6.csv")  

### DBscan
x = df.loc[:, [coluna1, coluna2]].values
neighb = NearestNeighbors(n_neighbors=5) # creating an object of the NearestNeighbors class
nbrs=neighb.fit(x) # fitting the data to the object
distances,indices=nbrs.kneighbors(x) # finding the nearest neighbours
# Sort and plot the distances results
distances = np.sort(distances, axis = 0) # sorting the distances
distances = distances[:, 1] # taking the second column of the sorted distances
# cluster the data into five clusters
dbscan = DBSCAN(eps = 1.1, min_samples = 8).fit(x) # fitting the model
labels = dbscan.labels_ # getting the labels
# Plot the clusters
plt.scatter(x[:, 0], x[:,1], c = labels, cmap= "plasma") # plotting the clusters
plt.xlabel(coluna1) # X-axis label
plt.ylabel(coluna2) # Y-axis label
plt.show() # showing the plot


### K Means
kmeans = KMeans(n_clusters=7).fit(df)
centroids = kmeans.cluster_centers_
print(centroids)
#select the 2 columns to work with
plt.scatter(df['aFactoresAtmosféricos'], df['aNumFeridosligeirosa30dia'], c= kmeans.labels_.astype(float), s=40, alpha=0.1)
plt.scatter(centroids[:, 0], centroids[:, 1], c='red', s=30)
plt.xlabel("aFactoresAtmosféricos") # X-axis label
plt.ylabel("aNumFeridosligeirosa30dia") # Y-axis label
plt.show()


