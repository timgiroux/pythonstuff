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


    #if 1 wrong, print 1 man,
    #if 2 wrong, print 1 man,
    #if 3 wrong, print 2 man, etc
    
    # updated print for handman
    hungman = []

    #mistakes per "body part"
    mistakes = 2
    nextmistakes = mistakes * 2
    
    if wrong == 0:
        for i in range(8):
            print(gallows[i])

    elif wrong in range(mistakes):
        print(gallows[0])
        print(gallows[1])
        print(gallows[2])
        print(man[0])
        print(gallows[4])
        print(gallows[5])
        print(gallows[6])
        print(gallows[7])

    elif wrong in range(mistakes, nextmistakes):
        print(gallows[0])
        print(gallows[1])
        print(gallows[2])
        print(man[0])
        print(man[1])
        print(gallows[5])
        print(gallows[6])
        print(gallows[7])
    nextmistakes = nextmistakes + mistakes
    mistakes = mistakes + mistakes

for i in range(8):
    print_gallows(i)

