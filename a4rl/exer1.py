import random
from Funcs import GetFuncValue, DiffErro, Stdev

runs = 30
array = [[0,0],[0,1],[1,0],[1,1]]
dOR = [0,1,1,1]
dAND = [0,0,0,1]
alfa = [0.00010, 0.0010, 0.10, 1, 4]

averagePerAlfa = []
standardDevPerAlfa = []
for w in range(len(alfa)):
    numEpochsPerRun = []
    for j in range(runs):
        wOR0 = random.uniform(0, 0.9)
        wOR1 = random.uniform(0, 0.9)
        wOR2 = random.uniform(0, 0.9)
        twOR0=0
        twOR1=0
        twOR2=0

        wAND0 = random.uniform(0, 0.9)
        wAND1 = random.uniform(0, 0.9)
        wAND2 = random.uniform(0, 0.9)
        twAND0=0
        twAND1=0
        twAND2=0

        eOR = 1
        eAND = 1
        count = 0
        while (eOR > 0.0 or eAND > 0.0):
            resOR = []
            resAND = []
            for i in range(4):
                auxOR = wOR0 + wOR1 * array[i][0] + wOR2 * array[i][1]
                resOR.append(GetFuncValue(auxOR))
                
                auxAND = wAND0 + wAND1 * array[i][0] + wAND2 * array[i][1]
                resAND.append(GetFuncValue(auxAND))        
            
                twOR0 = twOR0 + alfa[w] * (dOR[i] - GetFuncValue(auxOR))
                twOR1 = twOR1 + alfa[w] * array[i][0] * (dOR[i] - GetFuncValue(auxOR))
                twOR2 = twOR2 + alfa[w] * array[i][1] * (dOR[i] - GetFuncValue(auxOR))
                wOR0 = wOR0 + twOR0
                wOR1 = wOR1 + twOR1
                wOR2 = wOR2 + twOR2
                
                twAND0 = twAND0 + alfa[w] * (dAND[i] - GetFuncValue(auxAND))
                twAND1 = twAND1 + alfa[w] * array[i][0] * (dAND[i] - GetFuncValue(auxAND))
                twAND2 = twAND2 + alfa[w] * array[i][1] * (dAND[i] - GetFuncValue(auxAND))
                wAND0 = wAND0 + twAND0
                wAND1 = wAND1 + twAND1
                wAND2 = wAND2 + twAND2
            
            eOR = DiffErro(resOR, dOR)
            eAND = DiffErro(resAND, dAND)
            count += 1
            
        numEpochsPerRun.append(count)

    soma = 0
    for j in numEpochsPerRun:
        soma += j
        
    print("average number epochs: " + str(soma / len(numEpochsPerRun)))
    print("standard deviation => " + str(Stdev(numEpochsPerRun)))
    averagePerAlfa.append(soma / len(numEpochsPerRun))
    standardDevPerAlfa.append(Stdev(numEpochsPerRun))
    
soma = 0
for j in averagePerAlfa:
    soma += j
print("average number per alfa: " + str(soma / len(averagePerAlfa)))
print("standard deviation per alfa => " + str(Stdev(standardDevPerAlfa)))

