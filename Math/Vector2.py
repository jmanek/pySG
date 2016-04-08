import math

class Vector2:

    def __init__(self, *args):
        if len(args) == 2:
            self.x = float(args[0])
            self.y = float(args[1])
        else:
            self.x = 0
            self.y = 0


    def set(self, x, y):
            self.x = x
            self.y = y

    def normalize(self):
        mag = math.sqrt(self.x*self.x + self.y*self.y)
        return Vector2(self.x/mag, self.y/mag)

    def __neg__(self):
        return Vector2(self.x, -self.y)

    def __add__(self, other):
        return Vector2(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector2(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        if type(other) is Vector2:
            return 'Not implemented'
        else:
            return Vector2(self.x * other, self.y * other)

    def __setitem__(self, key, val):
        if key == 0: self.x = val
        if key == 1: self.y = val

    def __getitem__(self, key):
        if key == 0: return self.x
        if key == 1: return self.y

    def __str__(self):
        return '{0}, {1}'.format(self.x, self.y)
    def __repr__(self):
        return '{0}, {1}'.format(self.x, self.y)


