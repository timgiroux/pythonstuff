#create bullet
def shoot_bullet():
    
    playerx = player.xcor()
    
    bullet = turtle.Turtle()
    bullet.setposition(playerx, -250)
    bullet.color("white")
    bullet.shape("circle")
    bullet.penup()
    bullet.speed(0)
    
    bullet.setheading(90)

    #bullet move
    bulletx = bullet.xcor()
    bullety = bullet.ycor()
    bulletspeed = 5

    while bullety < 300:
        bullety += bulletspeed
        bullet.sety(bullety)
        if bullety == 300:
            bullet.reset()

    
    #bullet hit
    if bullety == 250:
        enemy.reset()
        bullet.reset()
        print("hit")            
