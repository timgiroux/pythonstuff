


def check_index():

    #position of guessed character in word
    global charPos
    charPos = []
    

    
    for i in range(wordlength):
        if guess == rletters[i]:
            charPos.append(i)

    if charPos[0] in beenGuessed:
        charPos.pop()
    


def ask_guess():
    global wrong
    
    global guess

    global gstate

    global boardstring

    global word

    
    if gstate == "none":
        guess = input("Guess a letter:      ")
        
        
    if gstate == "correct":
    
        if len(beenGuessed) == len(rletters):
            print(" YOU ")
            print(" SAVED ")
            print(" MAN ")
            print(" !!!!!! ")
            print(" you win : ) ")
            while True:
                win = True
        print("Correct! '%s' is in the word." %guess)
        guess = input("Guess another letter:       ")


    if gstate == "wrong":
        if wrong == 4:
            print(" MAN ")
            print(" IS ")
            print(" DEAD ")
            print(" !!!!!!! ")
            print(" you lose : ( ")
            while True:
                lose = True
        else:
            print("WRONG!!!!!")
            guess = input("Guess another letter:      ")

        
    if gstate == "LOSE":
        print_gallows()
        print(" MANS ")
        print(" IS ")
        print(" DEAD ")
        print(" !!!!!!! ")
        
        

    if guess in rletters:
        gstate = "correct"
        check_index()
        beenGuessed.append(charPos[0])


        if len(charPos) > 1:
                
            board[charPos[1]] = guess
            
            boardstring = "".join(board)
        else:
            #change board
            board[charPos[0]] = guess
            
            boardstring = "".join(board)


        
        print_gallows()
        print(boardstring)
        ask_guess()
        
    else:
        wrong += 1
        gstate = "wrong"

        if wrong == 4:
            gstate == "LOSE"
            




        
        print_gallows()
        print(boardstring)
        ask_guess()

        


def print_gallows():
    #7 total

    #none wrong
    if wrong == 0:
        for i in range(8):
            print(gallows[i])

    else:
        print(gallows[0])
        print(gallows[1])
        print(gallows[2])
        for wrongs in range(wrong):
            print(man[wrongs])
        therest = 4 + wrongs
        for i in range(therest, 8):
            print(gallows[i])


 #main game
def hangman(word):
    global wrong
    wrong = 0
    #store word in a global variable
    global gword
    gword = word


    global beenGuessed
    beenGuessed = []


    global man
    global gallows
    gallows = ["",
              "__________         ",
              "|                  ",
              "|                  ",
              "|                  ",
              "|                  ",
              "|                  ",
              "|                  "
              ]
    man = [
              "|        |         ",
              "|        O         ",
              "|       /|\        ",
              "|       / \        ",
              "|                  "
              ]


    global rletters
    rletters = list(word)
    global wordlength
    wordlength = len(word)

    

    #create board list
    global board, boardstring
    board = []
    for i in range(wordlength):
        board.append(" _ ")
        


    #create board string
    boardstring = "".join(board)
    


    #before first guess
    global gstate
    gstate = "none"

    print_gallows()
    print(boardstring)
    ask_guess()

    
    
    
    
        

#start game
choice = input("player one please enter your word: ")
hangman(choice)












