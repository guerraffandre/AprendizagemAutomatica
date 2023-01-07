from Funcs import ImportData, ReadJson
import time
import random
from datetime import date, datetime
import numpy as np
import matplotlib.pyplot as plt
from models.DataToShow import DataToShow
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import os
import csv
import warnings
warnings.filterwarnings("ignore")


df = pd.read_csv(os.getcwd()  + "\src\data\Data1100.csv")

correlations = df.corr()
sns.heatmap(correlations, xticklabels=correlations.columns, yticklabels=correlations.columns)
plt.show()
        
