from Funcs import ImportData, ReadJson
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
from sklearn.cluster import KMeans
from sklearn.cluster import KMeans, DBSCAN
from sklearn.neighbors import NearestNeighbors

coluna1 = "cvSexo"
coluna2 = "cvIdade"
df = pd.read_csv(os.getcwd()  + "\src\data\exer5Data.txt")  

