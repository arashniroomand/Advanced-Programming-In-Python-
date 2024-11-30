class point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other):
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5

    def zone(self):
        if self.x > 0 and self.y > 0:
            return 1
        elif self.x < 0 and self.y > 0:
            return 2
        elif self.x < 0 and self.y < 0:
            return 3
        elif self.x > 0 and self.y < 0:
            return 4


class Circle:

    def __init__(self, r, c):
        self.r = r
        self.c = c

    def area(self):
        return 3.14 * (self.r ** 2)

    def distance(self, other):
        return self.c.distance(other.c)