from Pattern import Pattern
import time
import matplotlib.pyplot as plt
from Funcs import CrossOver, CreateRandomPatern, ValuePatern, ValuePaternInverse, BuildPatterns, GetRatting

howManyPatterns = 18# howManyPatterns = 9 => 1, 2, 4, ..., 18, ..., 36
patterns = BuildPatterns(howManyPatterns)
howManyPatternsPopulation = 100 # 100
bestPercentage = 0.3 # best value patterns percentage to the next generation
newPercentage = 0.7 # percenatage how many new patterns created based on howManyPatternsPopulation
howManyColors = 4 #MAX is 8
runs = 30 # sets the max size of the patern to 
maxRunTimeSecs = 3600

patern = []
runTimes = []
countTentativasRuns = []
stOverall = time.time() 
for sizePattern in patterns:
    runtimesForEachPattern = []
    countTentativasRunsForEachPattern = []
    
    for run in range(runs):
        patern.clear()
        solution = CreateRandomPatern(howManyColors, sizePattern)            
        for j in range(howManyPatternsPopulation):
            p = Pattern()
            p.colors = CreateRandomPatern(howManyColors, sizePattern)
            p.valueInverse = ValuePaternInverse(solution, p.colors, sizePattern)
            p.value = ValuePatern(solution, p.colors, sizePattern)
            patern.append(p)
            
        countTentativas = 0
        st = time.time()
        while solution != patern[0].colors:
            patern.sort(key=lambda x: x.value, reverse=True)     
            countTentativas += 1   
            best30Paterns = []
            new70Paterns = []
            
            for p in range(round(howManyPatternsPopulation * bestPercentage)):
                best30Paterns.append(patern[p])
                
            for p in range(round(howManyPatternsPopulation * newPercentage)):
                p = Pattern()
                p.colors = CrossOver(best30Paterns, sizePattern)
                p.valueInverse = ValuePaternInverse(solution, p.colors, sizePattern)
                p.value = ValuePatern(solution, p.colors, sizePattern)
                new70Paterns.append(p)
            
            patern.clear()
            patern.extend(best30Paterns)
            patern.extend(new70Paterns)
                
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
