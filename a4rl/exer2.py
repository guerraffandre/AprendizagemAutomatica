import random
from Funcs import GetFuncValue, DiffErro, Stdev, ReadFile, Classify, Evaluate
from iris import Iris

setosa = []
versicolor = []
virginica = []
dataSet = []
avgFirstColumns = 0

numRuns = 10
k = [3, 4, 7, 11, 20, 30]

ReadFile(setosa, versicolor, virginica, dataSet, avgFirstColumns)

for j in k:
    Evaluate(j, j, dataSet, numRuns) 

