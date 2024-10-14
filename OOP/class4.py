class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def draw(self):
        print(f"Point = ({self.x}, {self.y})")

point = Point(4, 2)
point.draw()


