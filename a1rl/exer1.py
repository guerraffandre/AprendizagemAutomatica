from random import randrange
from Funcs import Stdev, PrintMatrix, StateTransition, RandomAction, IsParede, BuildMatrix
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import time
from Actions import Action
from Position import Position

reward = 1000
FAIL_FUN = "FAIL RUN"
alfaVar = 0.7
lambdaVar = 0.99
#final state
finalState = 131
#initial state
initialState =40
currentState = initialState
#size matrix/gameboard
rows = 12
cols = 12

runs = 30
steps = 1000

matrix = [[0 for _ in range(cols)] for _ in range(rows)]

BuildMatrix(matrix,cols,rows, reward)

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
        
        nextState = StateTransition(currentState, RandomAction())
        if IsParede(matrix, nextState) == False:
            currentState = nextState
            countSteps += 1
            
    et = time.time()
    runTimePerRun.append(et - st)
    numStepsPerRun.append(countSteps)

#print(numStepsPerRun)
#print(runTimePerRun)

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

numberStepsPerRunMRPT = []
for i in numStepsPerRunClean:
    numberStepsPerRunMRPT.append(100/i)
        
#print(str(numStepsPerRunClean))
#print(str(numRunsReachEnd))

print("average reward per step in "+str(steps)+" steps => "+ str((numRunsReachEnd*100)/runs) + "%")
print("standard deviation steps => " + str(Stdev(numStepsPerRunClean)))

print("average time of runs "+str(steps)+" steps => "+ str(somaTimeOfRun/numRunsReachEnd))
print("standard deviation time => " + str(Stdev(runTimePerRun)))

print("Average number actions per run => " + str(somaStepsOfRuns/numRunsReachEnd))
print("standard deviation time => " + str(Stdev(runTimePerRun)))

fig, axs = plt.subplots(1,3)
axs[0].boxplot(numberStepsPerRunMRPT)
axs[0].set_title('Mean reward per step')
axs[1].boxplot(numStepsPerRunClean)
axs[1].set_title('Mean number of steps')
axs[2].boxplot(runTimePerRun)
axs[2].set_title('Mean execution time (s)')

plt.show()