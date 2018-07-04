gallows = ["",
              "__________         ",
              "|                  ",
              "|                  ",
              "|                  ",
              "|                  ",
              "|                  ",
              "|                  "
              ]
#deleted last "|"
man = [
              "|        |         ",
              "|        O         ",
              "|       /|\        ",
              "|       / \        ",
              ]




def print_gallows(wrong):
    #7 total 

    #none wrong

    #if 1 wrong, print 1 man,
    #if 2 wrong, print 1 man,
    #if 3 wrong, print 2 man, etc
    
    if wrong == 0:
        for i in range(8):
            print(gallows[i])

    #elif wrong % 2 != 0
    #i wrong
    else:
        print(gallows[0])
        print(gallows[1])
        print(gallows[2])
        for wrongs in range(wrong):
            if wrong % 2 == 1:
                print(man[wrongs])
           # else:
            #    print(man[wrongs - 1])
        therest = 4
        for i in range(therest):
            print("|")
        therest -= 1

for i in range(8):
    print_gallows(i)
