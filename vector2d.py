# __nombre__ dunder methods
# dunder double underscore __
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        self.x += other.x
        self.y += other.y
        return Vector(self.x, self.y)
    
    def __mul__(self, k):
        return Vector(k * self.x, k * self.y)

    def __str__(self):
        return f'<Vector({self.x}, {self.y})>'
