import math


def arctan4(y, x):
    """
    four-quadrant arctangent given Cartesian coordinate x,y values
    """
    if x == 0:
        if y == 0:
            theta = 0
        elif y > 0:
            theta = math.pi/2
        elif y < 0:
            theta = -math.pi/2
    elif x > 0:
        theta = math.atan(y/x)
    if x < 0:
        if y > 0:
            theta = math.atan(y/x)+math.pi
        elif y < 0:
            theta = math.atan(y/x)-math.pi
        else:
            theta = math.pi
    return theta


testx = [2, 2, 0, -3, -2, -1, 0, 0, 2]
testy = [0, 1, 3, 1, 0, -2, 0, -2, 2]
print('     r           theta')
print('           arctan4  math.atan2')
for i in range(9):
    print('  {0:7.4f}  {1:7.4f}   {2:7.4f}'.
          format(math.sqrt(testx[i]**2+testy[i]**2),
                 arctan4(testy[i], testx[i]),
                 math.atan2(testy[i], testx[i])))
