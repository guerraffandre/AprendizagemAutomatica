from Funcs import ImportData, ReadJson
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
from sklearn.ensemble import AdaBoostClassifier
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn import metrics
import pandas as pd
import warnings
warnings.filterwarnings('ignore')
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import AdaBoostClassifier
import pickle


### Adaboost
df = pd.read_csv(os.getcwd()  + "\src\data\Data2000Exer6.csv")
#split dataset in features and target variable
feature_cols = ['aNumFeridosgravesa30dias','aNumFeridosligeirosa30dia','aNumMortosa30dias','aFactoresAtmosféricos','aNatureza','aCaracterísticasTecnicas1','aCondAderência','aEstadoConservação','aTraçado1','aTraçado2','aTraçado3','aTraçado4','pAcessóriosPassageiro','cvSexo','cvIdade']
X = df[feature_cols] # Features
y = df.cvSexo # Target variables => 'aNumFeridosgravesa30dias,aNumFeridosligeirosa30dia','aNumMortosa30dias',
# Split dataset into training set and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3) # 70% training and 30% test
# Create adaboost classifer object
abc = AdaBoostClassifier(n_estimators=1, learning_rate=2)
# Train Adaboost Classifer
model = abc.fit(X_train, y_train)
#Predict the response for test dataset
y_pred = model.predict(X_test)
# Model Accuracy, how often is the classifier correct?
print("Accuracy:",metrics.accuracy_score(y_test, y_pred))

