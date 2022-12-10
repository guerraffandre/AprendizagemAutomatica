import numpy as np
import pandas as pd
import math
import os

# loading required data
arrTitle = ["Sepal_Length", "Sepal_Width", "Petal_Length", "Petal_Width", "Species"]
iris = pd.read_csv(os.getcwd() + "\\a4rl\iris.data", sep=",", names=arrTitle)

# filling empty values and array creation of features
iris['Sepal_Length'] = iris['Sepal_Length'].fillna(iris['Sepal_Length'].mean())
iris['Sepal_Width'] = iris['Sepal_Width'].fillna(iris['Sepal_Width'].mean())
iris['Petal_Length'] = iris['Petal_Length'].fillna(iris['Petal_Length'].mean())
iris['Petal_Width'] = iris['Petal_Width'].fillna(iris['Petal_Width'].mean())

S_length = np.array(iris.Sepal_Length)
S_width = np.array(iris.Sepal_Width)
P_length = np.array(iris.Petal_Length)
P_width = np.array(iris.Petal_Width)


# this function calculates entropy of provided data set
def calculate_entropy(values):
    one = 0
    two = 0
    size = len(values)

    # distinguishing values in two group comparing with mean of each array
    for i in values:
        if (i <= np.mean(values)):
            one += 1
        else:
            two += 1

    entropy = -(((one / size) * math.log((one / size), 2)) + ((two / size) * math.log((two / size), 2)))
    return entropy


# defining dictionary to store values of entroy based on features
myDict = {"Sepal Length": calculate_entropy(S_length), "Sepal Width": calculate_entropy(S_width),
          "Petal Length": calculate_entropy(P_length), "Petal Width": calculate_entropy(P_width)}

# finding and displaying root of decision tree based on entropy
# lower the entropy higher the information gain

temp = min(myDict.values())
key = None
for keys in myDict:
    if myDict[keys] == temp:
        print("Root of Decision Tree : ", str(keys))
        key = keys
        break

print("Entropy of ", key, " = ", myDict[key])