class Point:
    default_origin = "(0,0)"

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print(f"Point = ({self.x}, {self.y})")

Point.default_origin = "(1,1)"
point = Point(4, 2)
point.draw()
print(point.default_origin)
another = Point(8, 4)
another.draw()
print(another.default_origin)

