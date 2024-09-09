import math


def tank_volume(R, d):
    """
    compute the liquid volume in a cylindrical tank
    with conical base
    tank dimensions are
    R:  radius
    2R: height of cylindrical part
    R:  height of conical part
    input:
        R:  tank radius
        d:  liquid depth
    output:
        V:  liquid volume
    """
    if d > 3*R:
        V = 'Overtop'
    else:
        if d <= R:
            V = math.pi*R**2*d/3
        else:
            V = math.pi*R**3/3 + math.pi*R**2*(d-R)
    return V


# Get Radius, depth from user input
radius = float(input('Enter value for radius: '))
depth = float(input('Enter value for liquid depth: '))
volume = tank_volume(radius, depth)
if volume == 'Overtop':
    print(volume)
else:
    print('liquid volume = {0:6.3f}'.format(volume))
