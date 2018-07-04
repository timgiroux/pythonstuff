

class Data:
    def __init__(self):
        self.nums = [1, 2, 3, 4, 5]

    def change_data(self, index, n):
        self.nums[index] = n
        print(self.nums)

numbers = Data()
#newnum = input("what would you like to change the third number to? ")
#newnum = int(newnum)
#numbers.change_data(2, newnum)
#print(numbers.nums())

class Shape():
    def __init__(self, w, l):
        self.width = w
        self.len = l

    def print_size(self):
        print("""{} by {}
              """.format(self.width, self.len))

class Square(Shape):
    def area(self):
        return self.width * self.len

    def print_size(self):
        print("""I am {} by {}
              """.format(self.width, self.len))

myshape = Square(20, 30)
myshape.print_size()
print(myshape.area())
