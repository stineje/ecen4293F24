class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod
    def zero(cls):
        return cls(0, 0)

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def draw(self):
        print(f"Point = ({self.x}, {self.y})")


point = Point(10, 20)
other = Point(1, 2)
combined = point + other
print(point + other)
combined.draw()
