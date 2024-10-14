class Point:
    def draw(self):
        print("let's have fun and draw!")

point = Point()
print(type(point))
print(f"Is this an instance of my class: {isinstance(point, Point)}")
print(f"Is this an instance of my class: {isinstance(point, int)}")
