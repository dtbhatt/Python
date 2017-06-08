l = ['magical unicorns',19,'hello',98.98,'world']

myString = ""
my_sum= 0
decisionInt = 0
decisionStr = 0
decisionFloat = 0

for i in l:
    if isinstance(i,str):
        myString += i + ""
        decisionStr += 1
    elif isinstance(i,int):
        my_sum += i
        decisionInt += 1
    else isinstance(i,float):
        my_sum += i
        decisionFloat += 1
    
if (decisionStr > 0 and decisionInt == 0):
    print "The array you enetered is a string type"
elif (decisionInt > 0 and decisionStr == 0):
    print "This array you entered is of int type"
else (decisionInt > 0 and decisionStr > 0 or decisionFloat > 0):
    print "The array you entered is of mixed type"

print myString,my_sum



