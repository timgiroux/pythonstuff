def default_screen():
    print_gallows()
    print(boardstring)
    ask_guess()

def update_board():
    global guess, board, boardstring, charPos
    if len(charPos) > 1:        
        board[charPos[1]] = guess    
        boardstring = "".join(board)
    else:
        #change board
        board[charPos[0]] = guess        
        boardstring = "".join(board)


def check_index():
     #character position
    global charPos
    charPos = []
    
    for i in range(wordlength):
        if guess == rletters[i]:
            charPos.append(i)

    if charPos[0] in beenGuessed:
        charPos.pop()

def correct_guess():
    global guess
    if len(beenGuessed) == len(rletters):
        win_game()
    else:
        print("Correct! '%s' is in the word." %guess)
        guess = input("Guess another letter:       ")

def wrong_guess():
    global guess
    if wrong == 4:
       lose_game()
    else:
        print("WRONG!!!!!")
        guess = input("Guess another letter:      ")
        

def lose_game():
    print_gallows()
    print(" MAN ")
    print(" IS ")
    print(" DEAD ")
    print(" !!!!!!! ")
    print(" The word was : %s" %word)
    while True:
        poop = smelly

def win_game():
    print(" YOU ")
    print(" SAVED ")
    print(" MAN ")
    print(" !!!!!! ")
    print(" you win : ) ")
    while True:
        win = True

def ask_guess():
    global wrong, guess, gstate, boardstring, word
    
    if gstate == "none":
        gstate = "start"
        guess = input("Guess a letter:      ")
        
    if gstate == "correct":
        correct_guess()
    if gstate == "wrong":
        wrong_guess()
    if gstate == "LOSE":
        lose_game()
        

    if guess in rletters:
        gstate = "correct"
        check_index()
        beenGuessed.append(charPos[0])
        update_board()
        default_screen()
        

        
    else:
        wrong += 1
        gstate = "wrong"
        if wrong == 4:
            gstate == "LOSE"
            default_screen()
        else:
            default_screen()
            #print_gallows()
            #print(boardstring)
            #ask_guess()

        


def print_gallows():
    #7 total 

    #none wrong
    if wrong == 0:
        for i in range(8):
            print(gallows[i])
    #i wrong
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
    global wrong, gword, beenGuessed, man, gallows
    wrong = 0
    #store word in a global variable
    gword = word
    beenGuessed = []
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

    default_screen()

    
    
    
#start game

choice = input("player one please enter your word: ")
for i in range(30):
    
    print("#")
hangman(choice)












