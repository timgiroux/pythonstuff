from turtle import *

fibo_nr = [1,1,2,3,5,8,13,21,34,55]

def draw_square(side_length):
    for i in range(4):
        forward(side_length)
        right(90)

nr_squares=len(fibo_nr)

factor = 3
penup()
goto(50,50)
pendown()
for i in range(nr_squares):
    draw_square(factor*fibo_nr[i])
    penup()
    forward(factor*fibo_nr[i])
    right(90)
    forward(factor*fibo_nr[i])
    pendown()

penup()
goto(50,50)
setheading(0)
pencolor('red')
pensize(3)
pendown()

for i in range(nr_squares):
    circle(-factor*fibo_nr[i],90)


