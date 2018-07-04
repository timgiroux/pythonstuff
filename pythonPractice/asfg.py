import turtle
turt = turtle.Turtle()

def check_dir():
    global direction
    direction = input("move the turtle")

def motion():
    if direction == "w":
        turt.forward(100)
    elif direction == "a":
        turt.left(90)
        turt.forward(100)
    elif direction == "d":
        turt.right(90)
        turt.forward(100)
    elif direction == "quit":
        exit()
    else:
        print("oops")

for i in range(100):

    check_dir()
    motion()
