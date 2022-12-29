from exer2 import ImportData, ReadJson
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score
from sklearn.neighbors  import KNeighborsClassifier
from sklearn.model_selection import cross_val_score
import warnings
warnings.filterwarnings("ignore")

df = pd.read_csv("D:/tudo/Mestrado/IAA/Final/AprendizagemAutomatica/PF/src/data/exer5Data.csv")
df9 = pd.read_csv("D:/tudo/Mestrado/IAA/Final/AprendizagemAutomatica/PF/src/data/exer9Data.csv")

X_train, X_test, y_train, y_test = train_test_split(df.iloc[:, :-1], df.iloc[:,-1], test_size=0.3, random_state=1)
knn= KNeighborsClassifier(n_neighbors=100)

accuracies=cross_val_score(estimator=knn,X=X_train,y=y_train,cv=2)

print(accuracies)
print("average accuracy :",np.mean(accuracies))
knn.fit(X_train,y_train)
print("test accuracy :",knn.score(X_test,y_test))
print("train accuracy :",knn.score(X_train,y_train))