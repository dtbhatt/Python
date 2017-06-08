import random

def coinToss():
    headToss = 0
    tailToss = 0
    
    coinType = ""

    for i in range(1,5001):
        randomToss = random.random()
        randomRound = int(round(randomToss))
        if (randomRound == 0):
            headToss += 1
            coinType = "Head"
        else:
            tailToss += 1
            coinType = "Tail" 
        print "Attmpet #",i,": Throwing a coin...  It's a", coinType,"Got", headToss, "head(s) so far and", tailToss,"tail(s) so far"
    return 


coinToss()