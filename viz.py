
from tabulate import tabulate
from colored import fg, bg, attr
from shapes import SHAPES
from utils import get_coordinates



FGMAP = {
    'orange': 'black',
    'pink': 'black',
    'blue': 'white',
    'green': 'black',
    'yellow': 'black',
    'red': 'white'
}

BGMAP = {
    'orange': 'orange_1',
    'pink': 'pink_1',
    'blue': 'blue',
    'green': 'light_green',
    'yellow': 'light_yellow',
    'red': 'red'
}


# Transpose a 2d list
def transpose(lst):
    return list(map(list, zip(*lst)))

def vis_shape(shape):
    return '\n\t' + '\n\t'.join([''.join(s) for s in transpose(shape)]) + '\n'

def visualize(sol, dim, configs, locations, colouring, board_config):
    
    # Empty board
    board = []
    for i in range(dim):
        board.append([])
        for j in range(dim):
            board[i].append('')
    
    # Print the chosen configurations
    # for col in configs:
    #     print(f'\n\t[{col}]')
    #     for c in configs[col]:
    #         if sol[c]:
    #             print(vis_shape(SHAPES[col][c.config_num]))
    
    # Populate the board
    for (x,y) in colouring:
        board[x][y] = board_config[x][y].replace('_', ' ')

    for col in locations:
        for i in range(len(locations[col])):
            for (x,y) in locations[col][i]:

                var = locations[col][i][(x,y)]
                if sol[var]:

                    # Print the others too
                    for (x1,y1) in get_coordinates(var):
                        if sol[colouring[(x1,y1)][col]]:
                            board[x1][y1] = fg(FGMAP[col]) + bg(BGMAP[col]) + board[x1][y1] + attr('reset')

    print(tabulate(transpose(board), tablefmt="fancy_grid"))
    print()
