class Dog():
    def __init__(self, name, breed, owner):
        self.name = name
        self.breed = breed
        self.owner = owner

class Person():
    def __init__(self, name):
        self.name = name

tim = Person("Tim Giroux")
nina = Dog("Nina", "Yorkie", tim)

#print(nina.owner.name)

class Rectangle():
    recs = []
    
    def __init__(self, w, l, name):
        self.width = w
        self.len = l
        self.area = w * l
        self.name = name
        self.recs.append((self.width, self.len))

    def __repr__(self):
        return self.name

#for i in range(4):
 #   i = Rectangle(i * 10 + 5, i * 3 + 30)

poopy = Rectangle(50, 10, "fart")
print(poopy)

#print(Rectangle.recs)
