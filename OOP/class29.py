from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])
p1 = Point(x=1, y=2)
p2 = Point(x=1, y=2)
print(p1 == p2)
print(f"point 1 is {p1.x} and {p1.y}")
print(f"point 2 is {p2.x} and {p2.y}")
