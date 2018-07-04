import turtle
import os
import math
import random

#screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Space Invaders")

#register shapes
turtle.register_shape("invader.gif")

#draw border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300, -300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
    border_pen.forward(600)
    border_pen.left(90)
border_pen.hideturtle()

#set score to 0
score = 0
kills = 0

#draw score
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-290, 280)
scorestring = "Score: %s" %score
score_pen.write(scorestring, False, align="left", font=("Arial", "14", "normal"))
score_pen.hideturtle()

#create player turtle
player = turtle.Turtle()
player.color("blue")
player.shape("triangle")
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)

playerspeed = 15




enemynum = 5
enemies = []

#add enemies to list
for i in range(enemynum):
    #create the enemy
    enemies.append(turtle.Turtle())
        
for enemy in enemies:
    enemy.color("red")
    enemy.shape("invader.gif")
    enemy.penup()
    enemy.speed(0)
    x = random.randint(-200, 200)
    y = random.randint(100, 250)
    enemy.setposition(x, y)


def new_wave():
    enemies.append(turtle.Turtle())
    
        
    for enemy in enemies:
        enemy.color("red")
        enemy.shape("circle")
        enemy.penup()
        enemy.speed(0)
        x = random.randint(-200, 200)
        y = random.randint(100, 250)
        enemy.setposition(x, y)

#enemy despawn
def enemy_despawn():
    while len(enemies) > 0:
        enemies.pop()
    


enemyspeed = 2


bulletnum = 10
bullets = []

for i in range(bulletnum):
    bullets.append(turtle.Turtle())

for bullet in bullets:
    #create bullet
    bullet.color("white")
    bullet.shape("triangle")
    bullet.penup()
    bullet.speed(0)
    bullet.setheading(90)
    bullet.shapesize(0.5, 0.5)
  #  bullet.hideturtle()
    bullet.setposition(-500, -500)

bulletspeed = 30

#define bullet state

#ready
#firing
#bulletstate = "ready"




#move left and right
def move_left():
    x = player.xcor()
    x -= playerspeed
    if x < -280:
        x = -280
    player.setx(x)
    
def move_right():
    x = player.xcor()
    x += playerspeed
    if x > 280:
        x = 280
    player.setx(x)

#fire bullet
def fire_bullet():
    #declare bulletstate as gobal if it needs changed
   # global bulletstate
    
    
    #move the bullet to just above the player
    x = player.xcor()
    y = player.ycor() + 10
    bullet.setposition(x, y)
    bullet.showturtle()

#check distance
def isCollision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    if distance < 15:
        return True
    else:
        return False


#create keyboard bindings
turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")
turtle.onkey(fire_bullet, "space")



#main game loop
while True:

    

    for enemy in enemies:

        #move the enemy
        x = enemy.xcor()
        x += enemyspeed
        enemy.setx(x)

        #check border
        if enemy.xcor() > 280 or enemy.xcor() < -280:
            #move all enemies down
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            #change direction
            enemyspeed *= -1
            
        
            #bullet hit detect
        if isCollision(bullet, enemy):
            bullet.hideturtle()
            bullet.sety(300)
            enemy.hideturtle()
            enemy.sety(-800)

            
            #update score
            score += 50
            kills += 1
            scorestring = "Score: %s" %score 
            score_pen.clear()
            score_pen.write(scorestring, False, align="left", font=("Arial", "14", "normal"))


            #check end of wave
            if kills in range(5, 10):
                for enemy in enemies:
                    enemy.hideturtle()
                    enemy.sety(-800)

                #start new wave
                score += (4 - kills) + 250
                score_pen.clear()
                score_pen.write(scorestring, False, align="left", font=("Arial", "14", "normal"))
                enemyspeed += 2

                enemynum += 1
                new_wave()
                
                kills = 0
                
              
            
           

        #player death
        if isCollision(enemy, player):
            player.hideturtle()
            print("GAME OVER")
            break


    #move the bullet
    
    y = bullet.ycor()
    y += bulletspeed
    bullet.sety(y)

    #check if bullet at top
    if bullet.ycor() > 275:
        bullet.hideturtle()
        




