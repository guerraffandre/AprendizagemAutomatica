import math
from random import randrange
from Actions import Action
from Position import Position

def Variance(data, ddof=0):
    n = len(data)
    mean = sum(data) / n
    return sum((x - mean) ** 2 for x in data) / (n - ddof)


def Stdev(data):
    var = Variance(data)
    std_dev = math.sqrt(var)
    return std_dev

def BuildMatrix(matrix, cols, rows, reward):
    j = 1
    for i in range(rows):
        for w in range(cols):
            if i > 0 and i < 11 and w > 0 and w < 11:
                p = Position()
                p.state = j
                p.reward = 0.0
                p.parede = False
                matrix[i][w] = p
            else:
                p = Position()
                p.state = j
                p.reward = 0.0
                p.parede = True
                matrix[i][w] = p
            j += 1
    matrix[10][10].reward = reward

def PrintMatrix(matrix,cols,rows):
    for i in range(cols):
        print("#####################################")
        for j in range(rows):
            print("state: " + str(matrix[i][j].state) + " reward: " + str(matrix[i][j].reward) + " parede: " + str(matrix[i][j].parede))

def PrintMatrixNoWalls(matrix,cols,rows):
    for i in range(cols):
        print("#####################################")
        for j in range(rows):
            if matrix[i][j].parede == False:
                print("state: " + str(matrix[i][j].state) + " reward: " + str(matrix[i][j].reward) + " parede: " + str(matrix[i][j].parede))
            
            
def RandomAction():
    r = randrange(1,5)
    if r == 1:
        return Action.UP
    elif r == 2:
        return Action.DOWN
    elif r == 3:
        return Action.LEFT
    elif r == 4:
        return Action.RIGHT

def StateTransition(currentState, action):
    nextState = 0
    if action == Action.UP:
        nextState = currentState - 12
    elif action == Action.DOWN:
        nextState = currentState + 12
    elif action == Action.RIGHT:
        nextState = currentState + 1
    elif action == Action.LEFT:
        nextState = currentState - 1
    return nextState

def IsParede(matrix, nextState):
    return SearchStateInMatrix(matrix, nextState).parede
    
def SearchStateInMatrix(matrix, state):
    for row in matrix:
        for element in row:
            if element.state == state:
                return element
    return False

def UpdateReward(matrix, currentState, nextState, alfaVar, gamaVar):
    currentStateValue = SearchStateInMatrix(matrix, currentState).reward
    nextStateValue = SearchStateInMatrix(matrix, nextState).reward
    bestValueNextStepCanDo = GetBestValueAction(matrix, nextState)
    if nextStateValue > 0.0:
        #SearchStateInMatrix(matrix, currentState).reward = ( (1 - alfaVar) * currentStateValue ) + alfaVar * ( nextStateValue + ( gamaVar * bestValueNextStepCanDo ) )
        #SearchStateInMatrix(matrix, currentState).reward = ( currentStateValue + (alfaVar * ( 1 + ( gamaVar * bestValueNextStepCanDo ) ) ) - currentStateValue )
        SearchStateInMatrix(matrix, currentState).reward = (1 - alfaVar) * currentStateValue + alfaVar * (nextStateValue + gamaVar * bestValueNextStepCanDo)
    
def GetBestValueAction(matrix, currentState):
    upStateReward = SearchStateInMatrix(matrix, StateTransition(currentState, Action.UP)).reward
    downStateReward = SearchStateInMatrix(matrix, StateTransition(currentState, Action.DOWN)).reward
    leftStateReward = SearchStateInMatrix(matrix, StateTransition(currentState, Action.LEFT)).reward
    rightStateReward = SearchStateInMatrix(matrix, StateTransition(currentState, Action.RIGHT)).reward
    
    return max(upStateReward, downStateReward, leftStateReward, rightStateReward)
    
def GetBestStepAction(matrix, currentState):
    upState = SearchStateInMatrix(matrix, StateTransition(currentState, Action.UP))
    downState = SearchStateInMatrix(matrix, StateTransition(currentState, Action.DOWN))
    leftState = SearchStateInMatrix(matrix, StateTransition(currentState, Action.LEFT))
    rightState = SearchStateInMatrix(matrix, StateTransition(currentState, Action.RIGHT))
    
    if upState.reward == downState.reward == leftState.reward == rightState.reward:
        return StateTransition(currentState, RandomAction())
        
    aux = max(upState.reward, downState.reward, leftState.reward, rightState.reward)
    if upState.parede == False and upState.reward == aux:
        return upState.state
    elif downState.parede == False and downState.reward == aux:
        return downState.state
    elif leftState.parede == False and leftState.reward == aux:
        return leftState.state
    elif rightState.parede == False and rightState.reward == aux:
        return rightState.state
    
def GetMatrixOnlyRewards(matrix,cols,rows):
    matrixAux = [[0 for _ in range(cols)] for _ in range(rows)]
    for i in range(rows):
        for w in range(cols):
           matrixAux[i][w] = matrix[i][w].reward
    return matrixAux
    
def Test1000(initState, finalState, steps, FAIL_FUN, matrix, mainTestStepsCount,reward):
    currentState = initState
    rewards = []
    countSteps = 0
    while currentState != finalState:        
        if countSteps >= steps:
            countSteps = FAIL_FUN
            break
        
        nextState = GetBestStepAction(matrix, currentState)
        if IsParede(matrix, nextState) == False:
            reward = SearchStateInMatrix(matrix, currentState).reward
            try:                
                rewards.append(steps / reward)
            except ZeroDivisionError:
                rewards.append(0)
            currentState = nextState
            countSteps += 1
            
    #print("Avarage reward per "+str(steps)+" steps at " +str(mainTestStepsCount)+ " => " + str( rewards ) )
    return rewards

def BuildInsideWalls(matrix, rows, cols):
    for i in range(rows-2):
        matrix[i][4].parede = True
        matrix[i][4].reward = -0.0000005
    aux = cols - 1
    for i in range(rows-2):
        matrix[aux][7].parede = True
        matrix[aux][7].reward = -0.0000005
        aux -= 1