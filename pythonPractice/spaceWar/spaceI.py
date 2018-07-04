import turtle, random, time

turtle.speed(0)
turtle.bgcolor("black")
turtle.title("SpaceWar")
turtle.ht()
turtle.setundobuffer(1)
turtle.tracer(0)


class Sprite(turtle.Turtle):
    def __init__(self, spriteshape, color, startx, starty):
        turtle.Turtle.__init__(self, shape = spriteshape)
        self.speed(0)
        self.penup()
        self.color(color)
        self.fd(0)
        self.goto(startx, starty)
        self.speed = 1

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
        self.speed = 15
        self.setheading(0)


    def move_right(self):
        self.fd(self.speed)
    def move_left(self):
        self.fd(-self.speed)



class Enemy(Sprite):
    def __init__(self, spriteshape, color, startx, starty):
        Sprite.__init__(self, spriteshape, color, startx, starty)
        self.speed = 2
        
    def move(self):
        self.fd(self.speed)
        if self.xcor() > 290:
            self.setx(290)
            for self in enemies:
                self.speed = self.speed * -1
                y = self.ycor()
                y -= 20
                self.sety(y)
        if self.xcor() < -290:
            self.setx(-290)
            for self in enemies:
                self.speed = self.speed * -1
                y = self.ycor()
                y -= 20
                self.sety(y)

class Bullet(Sprite):
    def __init__(self, spriteshape, color, startx, starty):
        Sprite.__init__(self, spriteshape, color, startx, starty)
        self.speed = 20
        self.shapesize(0.2, 0.5, outline=None)
        self.setheading(90)
        self.bulletstate = "ready"

        
    def move(self):
        if self.bulletstate == "firing":
            self.fd(self.speed)
        if self.bulletstate == "ready":
            self.goto(0, -1000)

    def shoot(self):
        if self.bulletstate == "ready":
            self.bulletstate = "firing"
            x = player.xcor()
            self.goto(x, -290)
        if self.bulletstate == "firing":
            self.fd(self.speed)
            if self.ycor() >= 290:
                self.bulletstate = "ready"
        

        

player = Player("square", "white", 0, -290)

enemynum = 6
enemies = []
for enemy in range(enemynum):
    enemies.append(Enemy("circle", "red", random.randint(-3, 7) * 40, 280))

bulletnum = 3
bullets = []
for bullet in range(bulletnum):
    bullets.append(Bullet("square", "grey", 0, -290))

#keyboard bindings
turtle.onkey(player.move_left, "Left")
turtle.onkey(player.move_right, "Right")
for bullet in bullets:
    turtle.onkey(bullet.shoot, "Up")
turtle.listen()

while True:
    turtle.update()
    time.sleep(0.03)

    for enemy in enemies:
        enemy.move()

    for bullet in bullets:
        bullet.move()










        
