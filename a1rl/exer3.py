from random import randrange
from Funcs import Stdev, PrintMatrix, StateTransition, RandomAction, IsParede, BuildMatrix, UpdateReward, PrintMatrixNoWalls, GetMatrixOnlyRewards, Test1000, GetBestStepAction
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
import time
from Actions import Action
from Position import Position

reward = 100
FAIL_FUN = "FAIL RUN"
stepsToStop = [ 100, 200, 500, 600, 700, 800, 900, 1000, 2500, 5000, 7500, 10000, 12500, 15000, 17500, 20000]
alfaVar = 0.7
gamaVar = 0.001
#final state
finalState = 131
#initial state
initialState =40
currentState = initialState
#size matrix/gameboard
rows = 12
cols = 12

runs = 30 # alinea 2b = 40
steps = 20000 # alinea 2b = 300

matrix = [[0 for _ in range(cols)] for _ in range(rows)]

BuildMatrix(matrix,cols,rows,reward)

numStepsPerRun = []
runTimePerRun = []

for r in range(runs):
    currentState = initialState
    countSteps = 0

    st = time.time()
    while currentState != finalState:        
        if countSteps >= steps:
            countSteps = FAIL_FUN
            break
        
        nextState = np.random.choice( [StateTransition(currentState, RandomAction()), GetBestStepAction(matrix, currentState)], p=[0.1, 0.9]) # ALTERAR PROBABILIDADE AQUI
        if IsParede(matrix, nextState) == False:
            UpdateReward(matrix, currentState, nextState, alfaVar, gamaVar)
            currentState = nextState
            countSteps += 1
            
        #if stepsToStop.__contains__(countSteps):
        #        rewards = Test1000(initialState, finalState, 1000, FAIL_FUN, matrix, countSteps, reward)
                #plt.plot(rewards)
                #plt.show() 
             
    #m = GetMatrixOnlyRewards(matrix, cols,rows)
    #ax = sns.heatmap(m, cbar=False)
    #plt.show()

    et = time.time()
    runTimePerRun.append(et - st)
    numStepsPerRun.append(countSteps)

PrintMatrixNoWalls(matrix,cols,rows)

numStepsPerRunClean = []
numRunsReachEnd = 0
somaTimeOfRun = 0
somaStepsOfRuns = 0
j = 0
for i in numStepsPerRun:
    if i != FAIL_FUN:
        numStepsPerRunClean.append(i)
        numRunsReachEnd += 1
        somaTimeOfRun += runTimePerRun[j]
        somaStepsOfRuns += i
    j += 1
    
print("average time of runs "+str(steps)+" steps => "+ str(somaTimeOfRun/numRunsReachEnd))
print("standard deviation time => " + str(Stdev(runTimePerRun)))

m = GetMatrixOnlyRewards(matrix, cols,rows)
ax = sns.heatmap(m)
plt.show()

