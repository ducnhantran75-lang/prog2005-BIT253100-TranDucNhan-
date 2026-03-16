class vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"({self.x}, {self.y}"

v1 = vector(2, 3)
v2 = vector(1, 4)
