class Vector2:

    def __init__(self, *args):
        if len(args) == 2:
            self.x = float(args[0])
            self.y = float(args[1])
        else:
            self.x = 0
            self.y = 0
    def __str__(self):
        return '{0}, {1}'.format(self.x, self.y)
    def __repr__(self):
        return '{0}, {1}'.format(self.x, self.y)


