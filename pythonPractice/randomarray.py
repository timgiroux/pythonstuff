import random
from random import shuffle

old = input("Enter any string to be randomized: ")

old = list(old)

oldlength = len(old)

new = []

def random_order(old):
    
    while len(new) != oldlength:
        
    #take random index of old list
        randy = random.randint(0, len(old) - 1)
        
    #add char from old list to new list
        new.append(old[randy])
    #remove char from old list
        old.pop(randy)

    #print new
    newstring = "".join(new)
    #for i in range(30):
     #   print("$$$")
    print(newstring)
    
random_order(old)

#lol python has as built in function for this RIP two hours
shuffle(old)
print(old)




