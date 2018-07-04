gallows = ["",
              "__________         ",
              "|                  ",
              ]
#deleted last "|"
man = [       "|        |         ",
              "|        O         ",
              "|       /|\        ",
              "|       / \        ",
              ]

pieces = 0

def print_gallows(wrong):
    global pieces
    #mistakes decides how many incorrect guesses trigger a new hangman piece
    mistakes = 2
    
    if wrong % mistakes == 0:
        gallows.append(man[int(wrong/mistakes)])
        pieces += 1
    for i in range(len(gallows)):
        print(gallows[i])
    for i in range(2):
        print("|")
    if pieces == 4:
        print("YOU LOSE")
        while True:
            poop = "smelly"
        
        

for i in range(16):
    print_gallows(i)

