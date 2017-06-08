import random


def grades():
    random_num = random.randint(60,100)
    if (100 >= random_num > 90):
        print "Score:", random_num , "Your grade is A"
    elif 89 <= random_num > 80:
        print "Score:", random_num , "Your grade is A"
    elif 79 <= random_num > 70:
        print "Score:", random_num , "Your grade is A"
    elif 69 <= random_num > 60:
        print "Score:", random_num , "Your grade is A"
    else:
        print "End of the program.  Bye!"
    return


grades()



