class Square():
    square_list = []
    def __init__(self, w, l):
        self.width = w
        self.len = l
        self.square_list.append(self)
        #print(self.square_list)

    def __repr__(self):
        return """ {} by {} """.format(self.width, self.len)


sq1 = Square(10, 10)
sq2 = Square(20, 20)
sq3 = sq2


def check_if_same(obj1, obj2):
    return obj1 is obj2

print(check_if_same(sq1, sq2))

print(check_if_same(sq2, sq3))
