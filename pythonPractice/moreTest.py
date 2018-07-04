import turtle

my_turtle = turtle.Turtle()

move = 1
turn = 5
for i in range (10000):
    my_turtle.forward(move)
    my_turtle.right(turn)

  
    turn = turn * 0.999
    move = move * 1.001
