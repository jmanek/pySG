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


