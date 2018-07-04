import math

class Orange:
    def __init__(self, w, c):
        self.weight = w
        self.color = c
        self.mold = 0
        print("Created!")

    def rot (self, days, temp):
        self.mold = days * temp


or1 = Orange(10, "brown")

or1.rot(7, 115)
#print(or1.mold)


class Rectangle():
    def __init__(self, w, l):
        self.width = w
        self.len = l

    def area(self):
        return self.width * self.len

    def changesize(self, w, l):
        self.width = w
        self.len = l

#w = input("Width of your rectangle: ")
#w = int(w)
#l = input("length of your rectangle: ")
#l = int(l)
#rectangle = Rectangle(w, l)
#print("your rectangle has an area of %s" %rectangle.area())


class Apple():
    def __init__(self, color, weight, species, clean):
        self.color = color
        self.weight = weight
        self.species = species
        self.clean = clean
        if self.clean == False:
            self.wash()

        

    def wash(self):
        if self.clean == False:
            self.clean = True
            print(self.clean)

    def eat(self):
        for i in range(10):
            self.weight -= 3
            print("the apple weighs %s lbs" %self.weight)
        print("yummy!")
            

apple = Apple("red", 15, "granny smith", False)

#apple.eat()


class Circle():
    def __init__(self, r, color):
        self.radius = r
        self.color = color
        
    def area(self):
        a = self.radius * self.radius * math.pi
        print(a)

circle = Circle(33, "red")

circle.area()































