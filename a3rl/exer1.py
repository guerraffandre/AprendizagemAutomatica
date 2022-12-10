from turtle import color
import matplotlib . pyplot as plt
import numpy as np
import random
import math

runs = 10
alfa = 0.0005  #0.00001
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
    for i in range(howManyPoints*2):
        if math.dist([setCX[i], setCY[i]], [setRX[0], setRY[0]]) < math.dist([setCX[i], setCY[i]], [setRX[1], setRY[1]]):
            setRX[0] = (1 - alfa) * setRX[0] + alfa * setCX[i]
            setRY[0] = (1 - alfa) * setRY[0] + alfa * setCY[i]            
            if run == 0:
                setRXFirstPassage.append(setRX[0])
                setRYFirstPassage.append(setRY[0])
            #print("closer to p1")
        else:
            setRX[1] = (1 - alfa) * setRX[1] + alfa * setCX[i]
            setRY[1] = (1 - alfa) * setRY[1] + alfa * setCY[i]
            if run == 0:
                setRXFirstPassage.append(setRX[1])
                setRYFirstPassage.append(setRY[1])
            #print("closer to p2")
            
    
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
            
        