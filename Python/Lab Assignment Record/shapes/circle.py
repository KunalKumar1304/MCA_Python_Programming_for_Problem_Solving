class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


class Circle:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2

