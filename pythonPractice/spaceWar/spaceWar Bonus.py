import os
import random
import turtle
import time
#import subprocess

#quickfart = "/Users/tlg/Documents/spaceWar/quickfart.wav"
def space_war(enemyShape):
    level = 1

    turtle.fd(0)
    turtle.speed(0)
    turtle.bgcolor("black")
    turtle.title("SpaceWar")
    #turtle.bgpic("space.gif")
    turtle.ht()
    turtle.setundobuffer(1)

    turtle.tracer(0)

    turtle.register_shape("dad.gif")

    


    class Sprite(turtle.Turtle):
        def __init__(self, spriteshape, color, startx, starty):
            turtle.Turtle.__init__(self, shape = spriteshape)
            self.speed(0)
            self.penup()
            self.color(color)
            self.fd(0)
            self.goto(startx, starty)
            self.speed = 1

        def move(self):
            self.fd(self.speed)
            
            #boundary detection
            if self.xcor() > 290:
                self.setx(290)
                self.rt(60)
            if self.xcor() < -290:
                self.setx(-290)
                self.rt(60)
            if self.ycor() > 290:
                self.sety(290)
                self.rt(60)
            if self.ycor() <  -290:
                self.sety(-290)
                self.rt(60)

        #check sprite collision
        def is_collision(self, other):
            if (self.xcor() >= (other.xcor() - 20)) and \
               (self.xcor() <= (other.xcor() + 20)) and \
               (self.ycor() >= (other.ycor() - 20)) and \
               (self.ycor() <= (other.ycor() + 20)):
                return True
            else:
                return False

            

    class Player(Sprite):
        def __init__(self, spriteshape, color, startx, starty):
            Sprite.__init__(self, spriteshape, color, startx, starty)
            self.shapesize(stretch_wid=0.6, stretch_len=1.1, outline=None)
            self.speed = 4
            self.lives = 3


        def turn_left(self):
            self.lt(20)
            
        def turn_right(self):
            self.rt(20)

        def accelerate(self):
            self.speed += 1

        def decelerate(self):
            self.speed -= 1

    class Enemy(Sprite):
        def __init__(self, spriteshape, color, startx, starty):
            Sprite.__init__(self, spriteshape, color, startx, starty)
            self.speed = 6
            self.setheading(random.randint(0, 360))

    class Ally(Sprite):
        def __init__(self, spriteshape, color, startx, starty):
            Sprite.__init__(self, spriteshape, color, startx, starty)
            self.speed = 8
            self.setheading(random.randint(0, 360))

            def move(self):
                self.fd(self.speed)
                
                #boundary detection
                if self.xcor() > 290:
                    self.setx(290)
                    self.lt(60)
                if self.xcor() < -290:
                    self.setx(-290)
                    self.lt(60)
                if self.ycor() > 290:
                    self.sety(290)
                    self.lt(60)
                if self.ycor() <  -290:
                    self.sety(-290)
                    self.lt(60)
            
    class Missile(Sprite):
        def __init__(self, spriteshape, color, startx, starty):
            Sprite.__init__(self, spriteshape, color, startx, starty)
            self.shapesize(stretch_wid = 0.2, stretch_len = 0.4, outline=None)
            self.speed = 20
            self.status = "ready"
            #self.goto(-1000, 1000)
            

        def fire(self):
            if self.status == "ready":
                #subprocess.call(["afplay", "/Users/tlg/Documents/spaceWar/quickfart.wav"])
                #os.system(" afplay /Users/tlg/Documents/spaceWar/quickfart.wav$")
                self.goto(player.xcor(), player.ycor())
                self.setheading(player.heading())
                self.status = "firing"

        def move(self):
            if self.status == "ready":
                self.goto(1000, -1000)
            
            
            if self.status == "firing":
                self.fd(self.speed)

            #border check
            
            if self.xcor() > 290 or self.xcor() < -290 or\
               self.ycor() > 290 or self.ycor() <  -290:
                #self.goto(-1000, 1000)
                self.status = "ready"

    class Particle(Sprite):
        def __init__(self, spriteshape, color, startx, starty):
            Sprite.__init__(self, spriteshape, color, startx, starty)
            self.shapesize(stretch_wid = 0.1, stretch_len = 0.1, outline=None)
            self.goto(-1000,-1000)
            self.frame = 0

        def explode(self, startx, starty):
            self.goto(startx, starty)
            self.setheading(random.randint(0, 360))
            self.frame = 1

        def move(self):
            if self.frame > 0:
                self.fd(10)
                self.frame += 1
            if self.frame > 50:
                self.frame = 0
                self.goto(-1000, -1000)
            if self.xcor() > 290 or self.xcor() < -290 or\
               self.ycor() > 290 or self.ycor() <  -290:
                #self.goto(-1000, 1000)
                self.lt(random.randint(0, 270))

    class Trail(Sprite):
        def __init__(self, spriteshape, color, startx, starty):
            Sprite.__init__(self, spriteshape, color, startx, starty)
            self.shapesize(stretch_wid = 0.1, stretch_len = 0.1, outline=None)
            self.goto(-1000,-1000)
            self.state = "find"
            self.frame = 0
            

        def follow(self, other):
            if self.state == "find":
                self.state = "freeze"
                self.setheading(player.heading() - 178 + random.randint(0, 4))
                x = other.xcor()
                y = other.ycor()
                self.goto(x, y)
                
                
                
            if self.state == "freeze":
                self.fd(random.randint(1, 10))
                #self.fd(10)
                self.frame += 1
                if self.frame > 10:
                    self.state = "find"
                    self.frame = 0
                    self.goto(-1000, -1000)
            
            
                
    class Game():
        def __init__(self):
            self.level = 1
            self.score = 0
            self.state = "playing"
            self.pen = turtle.Turtle()
            self.lives = 3

        def draw_border(self):
            #draw border
            self.pen.speed(0)
            self.pen.color("white")
            self.pen.pensize(3)
            self.pen.penup()
            self.pen.goto(-300, 300)
            self.pen.pendown()
            for side in range(4):
                self.pen.fd(600)
                self.pen.rt(90)
            self.pen.penup()
            self.pen.ht()
            self.pen.pendown()

        def show_status(self):
            
            if self.score >= 300:
                if enemyShape == "circle":
                    self.level = 2
                elif enemyShape == "dad.gif":
                    self.level = 1
            self.pen.undo()
            if enemyShape == "circle":
                msg = "Score: %s  Level: %s" %(self.score, self.level)
            elif enemyShape == "dad.gif":
                msg = "Score: %s  Level: %s" %(self.score, "DAD MODE ENABLED !!!!! ")
            self.pen.penup()
            self.pen.goto(-300, 310)
            self.pen.write(msg, font=("Arial", 16, "normal"))



    #create game object
    game = Game()

    #draw the game border
    game.draw_border()

    #show game status
    game.show_status()


    #create my sprites
    player = Player("triangle", "white", 0, 0)

    #enemy = Enemy("circle", "red", 100, 100)

    missile = Missile("triangle", "yellow", 1000, -1000)

    # ally = Ally("square", "blue", 0, 0)
    trails = []
    for trail in range(20):
        trails.append(Trail("circle", "grey", -1000, -1000))

    allies = []
    for i in range(6):
        allies.append(Ally("square", "blue", -100, -100))

    enemies = []
    if game.level == 1:
        for i in range(6):
            enemies.append(Enemy(enemyShape, "red", 100, 100))
                
    particles = []
    for i in range(20):
        particles.append(Particle("circle", "orange", 0, 0))


    #keyboard bindings
    turtle.onkey(player.turn_left, "Left")
    turtle.onkey(player.turn_right, "Right")
    turtle.onkey(player.accelerate, "Up")
    turtle.onkey(player.decelerate, "Down")
    turtle.onkey(missile.fire, "space")
    turtle.listen()


    #main game loop
    while True:
        if game.level == 1:
            gamespeed = 0.05
        if game.level == 2:
            
            game.pen.undo()
            for enemy in enemies:
                enemy.ht()
            for ally in allies:
                ally.ht()
            player.ht()
            missile.ht()
            for particle in particles:
                particle.ht()
            for trail in trails:
                trail.ht()


            
            space_war("dad.gif")
        turtle.update()
        time.sleep(gamespeed)

       # enemy.move()
        player.move()
        missile.move()
        # ally.move()

        for trail in trails:
            trail.follow(player)
            
            
        
        for particle in particles:
            particle.move()
        
        for ally in allies:
            ally.move()
            if missile.is_collision(ally):
                x = random.randint(-250, 250)
                y = random.randint(-250, 250)
                ally.goto(x, y)
                missile.status = "ready"
                ally.setheading(random.randint(0, 360))
                #decrease score
                game.score -= 50
                game.show_status()
                
        for enemy in enemies:
            enemy.move()
            
            #check for collision
            if player.is_collision(enemy):
                
                x = random.randint(-250, 250)
                y = random.randint(-250, 250)
                player.goto(x, y)
                player.setheading(random.randint(0, 360))
                game.score -= 100
                game.show_status()

            if missile.is_collision(enemy):
                x = random.randint(-250, 250)
                y = random.randint(-250, 250)
                enemy.goto(x, y)
                missile.status = "ready"
                enemy.setheading(random.randint(0, 360))
                #increase score
                game.score += 100
                game.show_status()

                for particle in particles:
                    particle.explode(missile.xcor(), missile.ycor())
                    
                    
                         

space_war("circle")













