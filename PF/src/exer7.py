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
#from lwoku import RANDOM_STATE, N_JOBS, VERBOSE, get_prediction
#from grid_search_utils import plot_grid_search, table_grid_search
import pickle

"""
### Adaboost
n_estimators = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 20, 30]
learning_rate = [(0.97 + x / 100) for x in range(0, 8)]


df = pd.read_csv(os.getcwd()  + "\src\data\DataToExer7.csv")  
#split dataset in features and target variable
feature_cols = ['aFactoresAtmosféricos','aNatureza','aCaracterísticasTecnicas1','aCondAderência','aEstadoConservação','aTraçado1','aTraçado2','aTraçado3','aTraçado4','pAcessóriosPassageiro']
X = df[feature_cols] # Features
y = df.aNumFeridosligeirosa30dia # Target variables => 'aNumFeridosgravesa30dias,aNumFeridosligeirosa30dia','aNumMortosa30dias',
# Split dataset into training set and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3) # 70% training and 30% test
# Create adaboost classifer object
abc = AdaBoostClassifier(n_estimators=1,
                         learning_rate=2)
# Train Adaboost Classifer
model = abc.fit(X_train, y_train)
#Predict the response for test dataset
y_pred = model.predict(X_test)
# Model Accuracy, how often is the classifier correct?
print("Accuracy:",metrics.accuracy_score(y_test, y_pred))
"""

df = pd.read_csv(os.getcwd()  + "\src\data\DataToExer7.csv")  
#split dataset in features and target variable
feature_cols = ['aFactoresAtmosféricos','aNatureza','aCaracterísticasTecnicas1','aCondAderência','aEstadoConservação','aTraçado1','aTraçado2','aTraçado3','aTraçado4','pAcessóriosPassageiro']
X = df[feature_cols] # Features
y = df.aNumFeridosligeirosa30dia # Target variables => 'aNumFeridosgravesa30dias,aNumFeridosligeirosa30dia','aNumMortosa30dias',
# Split dataset into training set and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3) # 70% training and 30% test

ab_clf = AdaBoostClassifier(random_state=RANDOM_STATE)
parameters = {
    'n_estimators': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 20, 30]
}
clf = GridSearchCV(ab_clf, parameters, cv=5, verbose=VERBOSE, n_jobs=N_JOBS)
clf.fit(X_train, y_train)
plot_grid_search(clf)
table_grid_search(clf)

parameters = {
    'learning_rate': [(0.97 + x / 100) for x in range(0, 8)]
}
clf = GridSearchCV(ab_clf, parameters, cv=5, verbose=VERBOSE, n_jobs=N_JOBS)
clf.fit(X_train, y_train)
plot_grid_search(clf)
table_grid_search(clf)

parameters = {
    'algorithm': ['SAMME', 'SAMME.R']
}
clf = GridSearchCV(ab_clf, parameters, cv=5, verbose=VERBOSE, n_jobs=N_JOBS)
clf.fit(X_train, y_train)
plot_grid_search(clf)
table_grid_search(clf)

parameters = {
    'n_estimators': [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 20],
    'learning_rate': [(0.97 + x / 100) for x in range(0, 8)],
    'algorithm': ['SAMME', 'SAMME.R']
}
clf = GridSearchCV(ab_clf, parameters, cv=5, verbose=VERBOSE, n_jobs=N_JOBS)
clf.fit(X_train, y_train)
plot_grid_search(clf)
table_grid_search(clf)