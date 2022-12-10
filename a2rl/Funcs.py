from random import randrange
from Colors import Colors

def BuildPatterns(howManyPatterns):
    aux = []
    aux.append(1)
    w = 2
    for j in range(howManyPatterns):
        aux.append(w)
        w += 2
    return aux
    
def GetRandomColor(howManyColors):
    r =  randrange(1,howManyColors + 1)
    match r:
        case 1: return Colors.RED
        case 2: return Colors.BLUE
        case 3: return Colors.BROWN
        case 4: return Colors.GREEN
        case 5: return Colors.WHITE
        case 6: return Colors.BLACK
        case 7: return Colors.PURPLE
        case 8: return Colors.ORANGE
            
def CreateRandomPatern(howManyColors, cols):
    r = []
    for i in range(cols):
        r.append(GetRandomColor(howManyColors))
    return r

def CreateStartPatern(cols):
    r = []
    for i in range(cols):
        r.append(Colors.NO_COLOR)
    return r

def ValuePatern(solution, patern, cols):
    value = cols
    for i in range(cols):
        if patern[i] != solution[i]:
            value -= 1
    return value    

def ValuePaternInverse(solution, patern, cols):
    value = 0
    for i in range(cols):
        if patern[i] == solution[i]:
            value += 1
    return value        

def FlipOneBit(pattern, sizePattern, howManyColors):
    aux = pattern[:]
    aux[randrange(0, sizePattern)] = GetRandomColor(howManyColors)
    return aux

def CrossOver(best30Paterns, sizePattern):
    colors1 = best30Paterns[randrange(0, len(best30Paterns) - 1 )].colors[:]
    colors2 = best30Paterns[randrange(0, len(best30Paterns) - 1 )].colors[:]
    colors1[randrange(0, sizePattern)] = colors2[randrange(0, sizePattern)]
    return colors1
    
def GetRatting(array):
    somaRunsF = 0
    somaRunsCountF = 0
    for rts in array:    
        somaRun = 0
        somaRunCount = 0
        for rt in rts:
            somaRun += rt
            somaRunCount += 1
        
        somaRunsF += somaRun / somaRunCount
        somaRunsCountF += 1
    return somaRunsF / somaRunsCountF