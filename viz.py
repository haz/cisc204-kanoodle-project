
from tabulate import tabulate
from shapes import SHAPES
from utils import get_coordinates


# Transpose a 2d list
def transpose(lst):
    return list(map(list, zip(*lst)))

def vis_shape(shape):
    return '\n\t' + '\n\t'.join([''.join(s) for s in transpose(shape)]) + '\n'

def visualize(sol, dim, configs, locations, colouring):
    
    # Empty board
    board = []
    for i in range(dim):
        board.append([])
        for j in range(dim):
            board[i].append('')
    
    # Print the chosen configurations
    for col in configs:
        print(f'\n\t[{col}]')
        for c in configs[col]:
            if sol[c]:
                print(vis_shape(SHAPES[col][c.config_num]))
    
    # Populate the board
    for col in locations:
        for i in range(len(locations[col])):
            for (x,y) in locations[col][i]:

                var = locations[col][i][(x,y)]
                if sol[var]:
                    # Capital at the location
                    # board[x][y] += f'[{col[0]}]'

                    # Print the others too
                    for (x1,y1) in get_coordinates(var):
                        board[x1][y1] += col[0].upper()

    for (x,y) in colouring:
        for col in colouring[(x,y)]:
            if sol[colouring[(x,y)][col]]:
                board[x][y] += f'({col[0]})'

    print(tabulate(transpose(board), tablefmt="fancy_grid"))
    print()
