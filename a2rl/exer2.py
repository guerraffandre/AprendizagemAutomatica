import time
import matplotlib.pyplot as plt
from Funcs import CreateRandomPatern, CreateStartPatern, ValuePaternInverse, FlipOneBit, BuildPatterns, GetRatting

howManyPatterns = 18# howManyPatterns = 9 => 1, 2, 4, ..., 18, ..., 36
patterns = BuildPatterns(howManyPatterns)
howManyColors = 4 #MAX is 8
runs = 30 # sets the max size of the patern to reach
runsForFlipOneBit = 1000000 # original is 1000
maxRunTimeSecs = 3600

patern = []
runTimes = []
countTentativasRuns = []
stOverall = time.time() 
for sizePattern in patterns:
    runtimesForEachPattern = []
    countTentativasRunsForEachPattern = []
    
    for run in range(runs):
        
        patern = CreateStartPatern(sizePattern)
        solution = CreateRandomPatern(howManyColors, sizePattern)
        
        countTentativas = 0
        st = time.time()
        for rffon in range(runsForFlipOneBit):
            auxPattern = FlipOneBit(patern, sizePattern, howManyColors)
            
            if ValuePaternInverse(solution, auxPattern, sizePattern) > ValuePaternInverse(solution, patern, sizePattern):
                patern = auxPattern
                
            if solution == patern:
                break
            
            countTentativas += 1
            
        if solution != patern:
             print("Solution not found at pattern size: " + str(sizePattern))
        
        runtimesForEachPattern.append(time.time() - st)
        countTentativasRunsForEachPattern.append(countTentativas)
        
    if time.time() - stOverall > maxRunTimeSecs:
        print(str(maxRunTimeSecs) + " seconds of execution completed on pattern size: " + str(sizePattern) + ". Stopping...")
        break
        
    runTimes.append(runtimesForEachPattern)
    countTentativasRuns.append(countTentativasRunsForEachPattern)
    
#print("tentativas: " + str(countTentativasRuns) + " \ntime: " + str(runTimes))

fig, axs = plt.subplots(1,2)
axs[0].boxplot(runTimes)
axs[0].set_title('tempos')
axs[1].boxplot(countTentativasRuns)
axs[1].set_title('tentativas')
plt.show()

print("######## rating => " + str(GetRatting(runTimes)*500 + GetRatting(countTentativasRuns)))

