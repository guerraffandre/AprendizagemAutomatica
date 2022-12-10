from turtle import color
import matplotlib . pyplot as plt
import numpy as np
import random
import math

runs = 30
alfa = 0.5  #0.00001
howManyPoints = 500

mean = [3, 3]
cov = [[1 , 0], [0 , 1]]
setA = np.random.multivariate_normal(mean, cov, howManyPoints).T
mean = [-3, -3]
cov = [[2, 0], [0 , 5]]
setB = np.random.multivariate_normal(mean, cov, howManyPoints).T

setC = np.concatenate((setA, setB), axis = 1)
setC = setC.T
np.random.shuffle(setC)
setC = setC.T

setAX = setA[0]
setAY = setA[1]

setBX = setB[0]
setBY = setB[1]

setCX = setC[0]
setCY = setC[1]  

setRX = []
setRX.append(setC[0][random.randrange(0,howManyPoints-1)])
setRX.append(setC[0][random.randrange(0,howManyPoints-1)])
setRY = []
setRY.append(setC[0][random.randrange(0,howManyPoints-1)])
setRY.append(setC[0][random.randrange(0,howManyPoints-1)])
setR = [setRX, setRY]

#plt.plot(setAX, setAY, 'x', color='c')
#plt.plot(setBX, setBY, 'x', color='y')
#plt.plot(setRX, setRY, 'x', color='r')
#plt.axis("equal")
#plt.show()

setRXFirstPassage = []
setRYFirstPassage = []

setRXEndEachPassageP1 = []
setRYEndEachPassageP1 = []
setRXEndEachPassageP2 = []
setRYEndEachPassageP2 = []

for run in range(runs):    
    dXP1 = 0
    dYP1 = 0
    dXP2 = 0
    dYP2 = 0
    for i in range(howManyPoints*2):
        if math.dist([setCX[i], setCY[i]], [setRX[0], setRY[0]]) < math.dist([setCX[i], setCY[i]], [setRX[1], setRY[1]]):
            dXP1 = dXP1 + (setCX[i] - setRX[0])
            dYP1 = dYP1 + (setCY[i] - setRY[0])
            if run == 0:
                setRXFirstPassage.append(setRX[0])
                setRYFirstPassage.append(setRY[0])
        else:
            dXP2 = dXP2 + (setCX[i] - setRX[1])
            dYP2 = dYP2 + (setCY[i] - setRY[1])
            if run == 0:
                setRXFirstPassage.append(setRX[1])
                setRYFirstPassage.append(setRY[1])
        
    setRX[0] = setRX[0] + (alfa / howManyPoints) * dXP1
    setRY[0] = setRY[0] + (alfa / howManyPoints) * dYP1
    setRX[1] = setRX[1] + (alfa / howManyPoints) * dXP2
    setRY[1] = setRY[1] + (alfa / howManyPoints) * dYP2
    
    setRXEndEachPassageP1.append(setRX[0])
    setRYEndEachPassageP1.append(setRY[0])
    setRXEndEachPassageP2.append(setRX[1])
    setRYEndEachPassageP2.append(setRY[1])
    
    #plt.plot(setAX, setAY, 'x', color='c')
    #plt.plot(setBX, setBY, 'x', color='y')
    #plt.plot(setRX, setRY, 'x', color='r')
    #plt.axis("equal")
    #plt.show()

plt.plot(setAX, setAY, 'x', color='c')
plt.plot(setBX, setBY, 'x', color='y')
plt.plot(setRXFirstPassage, setRYFirstPassage, 'x', color='m')
plt.plot(setRXEndEachPassageP1, setRYEndEachPassageP1, 'x', color='k')
plt.plot(setRXEndEachPassageP2, setRYEndEachPassageP2, 'x', color='k')
plt.axis("equal")
plt.show()

setXCloserToP1SetA = []
setYCloserToP1SetA = []
setXCloserToP1SetB = []
setYCloserToP1SetB = [] 

setXCloserToP2SetA = []
setYCloserToP2SetA = []
setXCloserToP2SetB = []
setYCloserToP2SetB = []
for i in range(howManyPoints):
    #setA
    if math.dist([setRX[0], setRY[0]], [setAX[i], setAY[i]]) < math.dist([setRX[1], setRY[1]], [setAX[i], setAY[i]]):
        setXCloserToP1SetA.append(setAX[i])
        setYCloserToP1SetA.append(setAY[i])
    else:
        setXCloserToP2SetA.append(setAX[i])
        setYCloserToP2SetA.append(setAY[i])
    #setB
    if math.dist([setRX[0], setRY[0]], [setBX[i], setBY[i]]) < math.dist([setRX[1], setRY[1]], [setBX[i], setBY[i]]):
        setXCloserToP1SetB.append(setBX[i])
        setYCloserToP1SetB.append(setBY[i])
    else:
        setXCloserToP2SetB.append(setBX[i])
        setYCloserToP2SetB.append(setBY[i])

plt.plot(setXCloserToP1SetA, setYCloserToP1SetA, 'x', color='c')
plt.plot(setXCloserToP1SetB, setYCloserToP1SetB, 'x', color='y')
plt.plot(setXCloserToP2SetA, setYCloserToP2SetA, 'x', color='m')
plt.plot(setXCloserToP2SetB, setYCloserToP2SetB, 'x', color='k')
plt.plot(setRXEndEachPassageP1, setRYEndEachPassageP1, 'x', color='r')
plt.plot(setRXEndEachPassageP2, setRYEndEachPassageP2, 'x', color='r')
plt.axis("equal")
plt.show()

