import math
import random
from iris import Iris
import os

def Variance(data, ddof=0):
    n = len(data)
    mean = sum(data) / n
    return sum((x - mean) ** 2 for x in data) / (n - ddof)


def Stdev(data):
    var = Variance(data)
    std_dev = math.sqrt(var)
    return std_dev

def GetFuncValue(value):
    if value > 0:
        return 1
    elif value <= 0:
        return 0
        
def DiffErro(res, resExpected):
    count1 = 4
    for i in range(4):
        if res[i] == resExpected[i]:
            count1 -= 1
    return count1 / 4

def ReadFile(setosa, versicolor, virginica, dataSet, avgFirstColumns):
    f = open(os.getcwd() + "\\a4rl\iris.data", "r")
    w = 1
    for x in f:
        if x.__contains__("setosa"):
            s = x.replace(",Iris-setosa\n","")
            i = Iris()
            i.id = w
            i.sepalLength = float(s.split(",")[0])
            avgFirstColumns += i.sepalLength
            i.sepalWidth = float(s.split(",")[1])
            i.petalLength = float(s.split(",")[2])
            i.petalWidth = float(s.split(",")[3])
            i.className = "setosa"
            setosa.append(i)
            
        elif x.__contains__("virginica"):
            s = x.replace(",Iris-virginica\n","")
            i = Iris()
            i.id = w
            i.sepalLength = float(s.split(",")[0])
            avgFirstColumns += i.sepalLength
            i.sepalWidth = float(s.split(",")[1])
            i.petalLength = float(s.split(",")[2])
            i.petalWidth = float(s.split(",")[3])
            i.className = "virginica"
            virginica.append(i)
            
        elif x.__contains__("versicolor"):        
            s = x.replace(",Iris-versicolor\n","")
            i = Iris()
            i.id = w
            i.sepalLength = float(s.split(",")[0])
            avgFirstColumns += i.sepalLength
            i.sepalWidth = float(s.split(",")[1])
            i.petalLength = float(s.split(",")[2])
            i.petalWidth = float(s.split(",")[3])
            i.className = "versicolor"
            versicolor.append(i)    
            
        w += 1  
        
    dataSet.extend(setosa)
    dataSet.extend(versicolor)
    dataSet.extend(virginica)
    return avgFirstColumns
    
def K_FoldValidation(K, k, Items):
    correct = 0
    random.shuffle(Items)
    trainingSet = []
    testSet = []
    for s in range(len(Items)):
        if s < round(len(Items) * 0.7):
            trainingSet.append(Items[s])
        else:
            testSet.append(Items[s])

    for item in testSet:
        itemClass = item.className   
        className = Classify(item, k, trainingSet)
        if className == itemClass:
            correct += 1
    
    accuracy = correct / float(len(Items))
    return accuracy, correct

def Evaluate(K, k, items, numRuns):
    accuracy = 0
    correct = 0
    for i in range(numRuns):
        random.shuffle(items)
        accuracyAux, correctAux = K_FoldValidation(K, k, items)
        accuracy += accuracyAux
        correct += correctAux

    print("k: "+ str(k) +"\naccuracy: " + str(accuracy / float(numRuns)) + " \navg correct predictions: " 
          + str(correct / len(items)) + "\ncorrect predictions: " + str(correct))
 
def Classify(itemX, k, dataSet):
    neighbors = [] 
    for item in dataSet:
        distance = EuclideanDistance(itemX, item)
        neighbors = UpdateNeighbors(neighbors, item, distance, k)
        
    className = CalculateNeighborsClass(neighbors, k)
    return className

def EuclideanDistance(x, y):
    s = 0  
    s += math.pow(x.sepalLength - y.sepalLength, 2)
    s += math.pow(x.petalLength - y.petalLength, 2)
    s += math.pow(x.sepalWidth - y.sepalWidth, 2)
    s += math.pow(x.petalWidth - y.petalWidth, 2)
    return math.sqrt(s)

def UpdateNeighbors(neighbors, item, distance, k):     
    if neighbors is None:
        neighbors = []
    if len(neighbors) < k:
        item.distance = distance
        neighbors.append(item)
        neighbors.sort(key=lambda x: x.distance, reverse=False)   
    else:
        if neighbors[-1].distance > distance:            
            item.distance = distance
            neighbors[-1] = item
            neighbors.sort(key=lambda x: x.distance, reverse=False)   
    return neighbors


def CalculateNeighborsClass(neighbors, k):
    countsetosa = 0
    countversicolor = 0
    countvirginica = 0
    for i in range(round(k)):         
        if neighbors[i].className == "versicolor":
            countversicolor += 1
        elif neighbors[i].className == "setosa":
            countsetosa += 1
        elif neighbors[i].className == "virginica":
            countvirginica += 1
            
    if countsetosa > countversicolor:
        if countsetosa > countvirginica:
            return "setosa"
        else:
            return countvirginica
    elif countversicolor > countvirginica:
        return "versicolor"
    else:
        return "virginica"