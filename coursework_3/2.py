class Rectangle:
    # constructor body
    # with the given x, y, w, h
    def __init__(self, x, y, w, h):
        self._x = x
        self._y = y
        self._width = w
        self._height = h

    # return the field values
    def getx(self):
        return self._x

    def gety(self):
        return self._y

    def get_width(self):
        return self._width

    def get_height(self):
        return self._height

    def __str__(self):
        return '{(%d, %d), %dx%d}' % (self.getx(), self.gety(), self.get_width(), self.get_height())

    # define a merge function
    def merge(self, rect):
        x = min(self.getx(), rect.getx())  # find the x coordinate
        y = max(self.gety(), rect.gety())  # find the y coordinate
        # calculate the width and the height
        to_x = max(self.getx() + self.get_width(), rect.getx() + rect.get_width())
        to_y = min(self.gety() - self.get_height(), rect.gety() - rect.get_height())
        w = to_x - x
        h = y - to_y
        return Rectangle(x, y, w, h)


# test part
rect1 = Rectangle(5, 12, 4, 6)
rect2 = Rectangle(6, 8, 5, 7)
rect3 = Rectangle(14, 9, 3, 3)
rect4 = Rectangle(10, 3, 5, 8)
print(rect1.merge(rect2))
print(rect4.merge(rect3))
