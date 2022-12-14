import os
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.tree import DecisionTreeClassifier # Import Decision Tree Classifier
from sklearn.model_selection import train_test_split # Import train_test_split function
from sklearn import metrics #Import scikit-learn metrics module for accuracy calculation
from sklearn.metrics import accuracy_score
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from xgboost import XGBClassifier

col_names = ['aNumFeridosgravesa30dias','aNumFeridosligeirosa30dia','aNumMortosa30dias','aFactoresAtmosféricos','aNatureza','aCaracterísticasTecnicas1','aCondAderência','aEstadoConservação','aTraçado1','aTraçado2','aTraçado3','aTraçado4','pAcessóriosPassageiro','cvSexo','cvIdade']
"""
### Decision Tree
avg = 0
for i in range(30):
    pima = pd.read_csv(os.getcwd()  + "\src\data\Data2000Exer9.csv", header=None, names=col_names)
    pima.head()
    #split dataset in features and target variable
    feature_cols = ['aNumFeridosgravesa30dias','aNumFeridosligeirosa30dia','aNumMortosa30dias','aFactoresAtmosféricos','aNatureza','aCaracterísticasTecnicas1','aCondAderência','aEstadoConservação','aTraçado1','aTraçado2','aTraçado3','aTraçado4','pAcessóriosPassageiro','cvSexo','cvIdade']
    X = pima[feature_cols] # Features
    y = pima.aNumFeridosligeirosa30dia # Target variables => 'aNumFeridosgravesa30dias,aNumFeridosligeirosa30dia','aNumMortosa30dias',
    # Split dataset into training set and test set
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1) # 70% training and 30% test
    # Create Decision Tree classifer object
    clf = DecisionTreeClassifier()
    # Train Decision Tree Classifer
    clf = clf.fit(X_train,y_train)
    #Predict the response for test dataset
    y_pred = clf.predict(X_test)
    # Model Accuracy, how often is the classifier correct?
    avg += metrics.accuracy_score(y_test, y_pred)
    print("Accuracy:",metrics.accuracy_score(y_test, y_pred))
print("Final avg Decision Tree: " + str(avg/30))
"""
"""
### Multi Layer Perceptron (Neural Networks)
avg = 0
for i in range(30):
    # Creating labelEncoder
    le = preprocessing.LabelEncoder()     
    pima = pd.read_csv(os.getcwd()  + "\src\data\Data2000Exer9.csv", header=None, names=col_names)
    pima.head()
    #split dataset in features and target variable
    feature_cols = ['aNumFeridosgravesa30dias','aNumFeridosligeirosa30dia','aNumMortosa30dias','aFactoresAtmosféricos','aNatureza','aCaracterísticasTecnicas1','aCondAderência','aEstadoConservação','aTraçado1','aTraçado2','aTraçado3','aTraçado4','pAcessóriosPassageiro','cvSexo','cvIdade']
    X = pima[feature_cols] # Features
    y = pima.aNumFeridosligeirosa30dia # Target variables => 'aNumFeridosgravesa30dias,aNumFeridosligeirosa30dia','aNumMortosa30dias',
    # Import train_test_split function
    # Split dataset into training set and test set
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=2)  # 70% training and 30% test
    # Import MLPClassifer 
    # Create model object
    clf = MLPClassifier(hidden_layer_sizes=(6,5),
                        random_state=5,
                        verbose=True,
                        learning_rate_init=0.01)
    # Fit data onto the model
    clf.fit(X_train,y_train)
    # Make prediction on test dataset
    ypred=clf.predict(X_test)
    # Import accuracy score 
    # Calcuate accuracy
    avg += accuracy_score(y_test,ypred)
    print("acuracy: " + str(accuracy_score(y_test,ypred)))
print("Final avg Multi Layer Perceptron: " + str(avg/30))
"""

### XGBoost
avg = 0
for i in range(30):
    df = pd.read_csv(os.getcwd()  + "\src\data\Data2000Exer9.csv", header=None, names=col_names)
    df.head()
    feature_cols = ['aNumFeridosgravesa30dias','aNumFeridosligeirosa30dia','aNumMortosa30dias','aFactoresAtmosféricos','aNatureza','aCaracterísticasTecnicas1','aCondAderência','aEstadoConservação','aTraçado1','aTraçado2','aTraçado3','aTraçado4','pAcessóriosPassageiro','cvSexo','cvIdade']
    X = df[feature_cols] # Features
    y = df.aNatureza # Target variables => 'aNumFeridosgravesa30dias,aNumFeridosligeirosa30dia','aNumMortosa30dias',
    # Import train_test_split function
    # Split dataset into training set and test set
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=3)  # 70% training and 30% test
    # fit model no training data
    model = XGBClassifier()
    model.fit(X_train, y_train)
    # make predictions for test data
    y_pred = model.predict(X_test)
    predictions = [round(value) for value in y_pred]
    # evaluate predictions
    avg += accuracy_score(y_test,predictions)
    accuracy = accuracy_score(y_test, predictions)
    print("Accuracy: %.2f%%" % (accuracy * 100.0))
print("Final avg XGBoost: " + str(avg/30))
