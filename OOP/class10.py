class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod
    def zero(cls):
        return cls(0, 0)

    def __str__(self):
        return f"({self.x}, {self.y})"

    def draw(self):
        print(f"Point = ({self.x}, {self.y})")


point = Point.zero()
print(point)
