import random


def randInt(min=0, max=0):
    if min == 0 and max == 0:
        num = random.random()*100
    if max != 0:
        num = random.random()*max
    if min != 0:
        num = random.random()*50+min
    if min != 0 and max != 0:
        num = random.random()*(max-min)+min
    return num


print(randInt())            # should print a random integer between 0 to 100
print(randInt(max=50)) 	    # should print a random integer between 0 to 50
print(randInt(min=50)) 	    # should print a random integer between 50 to 100
# should print a random integer between 50 and 500
print(randInt(min=50, max=500))
