def default_screen():
    print_gallows(wrong, mistakes)
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
    print("WRONG!!!!!")
    guess = input("Guess another letter:      ")
        

def lose_game():
    print(" MAN ")
    print(" IS ")
    print(" DEAD ")
    print(" !!!!!!! ")
    print(" The word was : %s" %gword)
    while True:
        poop = "smelly"

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
        #checkindex gives charposition of correct guess
        check_index()
        try:
            beenGuessed.append(charPos[0])
        except(IndexError):
            default_screen()
            wrong_guess()
            
        update_board()
        default_screen()
    
    else:
        wrong += 1
        gstate = "wrong"
        default_screen()
        


def print_gallows(wrong, mistakes):
    global pieces, gstate
    #mistakes decides how many incorrect guesses trigger a new hangman piece
    #mistakes = 2
    
    #if gstate == "correct" or gstate == "start":
    if wrong == 0 or gstate == "correct":
        for i in range(len(gallows)):
            print(gallows[i])
        for i in range(7 - pieces):
            print("|")
        
    if gstate == "wrong" and wrong % mistakes == 0 or wrong == 1 and gstate != "correct":
        gallows.append(man[int(wrong/mistakes)])
        pieces += 1
        for i in range(len(gallows)):
            print(gallows[i])
        for i in range(7 - pieces):
            print("|")
    if pieces == 4:
        lose_game()
        while True:
            poop = "smelly"


 #main game
def hangman(word):
    global wrong, gword, beenGuessed, man, gallows, pieces
    wrong = 0
    #store word in a global variable
    gword = word
    beenGuessed = []
    gallows = ["",
              "__________         ",
              ]
    man = [   #"|        |         ",
              "|        |         ",
              "|        O         ",
              "|       /|\        ",
              "|       / \        ",
              "|                  "
              ]
    pieces = 0


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
difficulty = input("how many wrong guesses does player 2 get? (multiples of 4)   ")
difficulty = int(difficulty)
if difficulty == 1:
    mistakes = difficulty
else:
    mistakes = int(difficulty / 4)

for i in range(30):
    
    print("#")
hangman(choice)












