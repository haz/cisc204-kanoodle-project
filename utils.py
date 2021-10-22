
from shapes import SHAPES

def get_coordinates(placement):
    x0, y0 = placement.x, placement.y
    coordinates = []
    shape = SHAPES[placement.col][placement.config_num]
    for x in range(len(shape)):
        for y in range(len(shape[x])):
            if shape[x][y] == 'X':
                coordinates.append((x0 + x, y0 + y))
    return coordinates
