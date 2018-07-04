import random

okay = input("Enter any string to be randomized: ")

okay = list(okay)

new = []

amountLeft = len(okay)

while len(new) != len(okay):
    randy = random.randint(0, len(okay) - 1)
    print(randy)
    if okay[randy] in new:
        continue
    else:
        amountLeft -= 1
        new.append(okay[randy])
        print(new)
        
print(new)
