import time
import matplotlib.pyplot as plt
from Funcs import CreateRandomPatern, CreateStartPatern, ValuePatern, ValuePaternInverse, BuildPatterns, GetRatting

howManyPatterns = 8# howManyPatterns = 8 => 1, 2, 4, ..., 16
patterns = BuildPatterns(howManyPatterns)
howManyColors = 4 # MAX is 8
runs = 30 # sets the runs for each pattern
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
        while solution != patern:
            patern = CreateRandomPatern(howManyColors, sizePattern)
            countTentativas += 1
            
            #print("ValuePatern: " + str(ValuePatern(solution, patern, sizePattern)))
            #print("ValuePaternInverse: " + str(ValuePaternInverse(solution, patern, sizePattern)))
            
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

