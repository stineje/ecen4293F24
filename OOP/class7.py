class Point:
    default_origin = "(0,0)"

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def draw(self):
        print(f"Point = ({self.x}, {self.y})")

Point.default_origin = "(1,1)"
point = Point(4, 2)
print(point)
