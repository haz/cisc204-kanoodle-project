
from bauhaus import Encoding, proposition, constraint

from shapes import SHAPES
from boards import BOARDS
from viz import visualize
from utils import get_coordinates

import pprint, sys, time

USAGE = "\n\tUsage: python3 run.py <board number>\n"

# Encoding that will store all of your constraints
E = Encoding()


#############
# Constants #
#############
DIM = 5

colMap = {
    'r': 'red',
    'b': 'blue',
    'g': 'green',
    'y': 'yellow',
    'o': 'orange',
    'p': 'pink',
}

####################################
#
#   Propositions
#
####################################

# Proposition to determine which configuration is used for a coloured piece
@proposition(E)
class PieceConfig:
    def __init__(self, col, config_num) -> None:
        self.col = col
        self.config_num = config_num
    
    def __repr__(self) -> str:
        return f"PieceConfig({self.col}, {self.config_num})"


pieceConfigs = {c: [] for c in colMap.values()}

for col in pieceConfigs:
    for i in range(len(SHAPES[col])):
        prop = PieceConfig(col, i)
        pieceConfigs[col].append(prop)



# Proposition to place a piece on the board
@proposition(E)
class PlacePiece:
    def __init__(self, col, config_num, x, y) -> None:
        self.col = col
        self.config_num = config_num
        self.x = x
        self.y = y
    
    def __repr__(self) -> str:
        return f"PlacePiece({self.col}, {self.config_num}, {self.x}, {self.y})"


pieceLocations = {c: [{} for _ in range(len(SHAPES[c]))] for c in pieceConfigs}

piecesAtLocation = {}

pieceLocationsByCol = {
    col: [] for col in pieceLocations
}

for col in pieceLocations:
    for i in range(len(SHAPES[col])):
        for x in range(DIM):
            for y in range(DIM):

                prop = PlacePiece(col, i, x, y)

                pieceLocations[col][i][(x,y)] = prop
                pieceLocationsByCol[col].append(prop)

                if (x,y) not in piecesAtLocation:
                    piecesAtLocation[(x,y)] = []
                piecesAtLocation[(x,y)].append(prop)


@proposition(E)
class PlaceColour:
    def __init__(self, col, x, y) -> None:
        self.col = col
        self.x = x
        self.y = y
    
    def __repr__(self) -> str:
        return f"PlaceColour({self.col}, {self.x}, {self.y})"

coloursAtLocation = {}
for x in range(DIM):
    for y in range(DIM):
        coloursAtLocation[(x,y)] = {}
        for col in pieceLocations:
            prop = PlaceColour(col, x, y)
            coloursAtLocation[(x,y)][col] = prop


####################################
#
#   Constraints
#
####################################


# Only one configuration for a colour
for col in pieceConfigs:
    constraint.add_exactly_one(E, *(pieceConfigs[col]))

# Don't allow pieces go out of bounds
for x in range(DIM):
    for y in range(DIM):
        for pieceLoc in piecesAtLocation[(x,y)]:
            disable = False
            for (x1, y1) in get_coordinates(pieceLoc):
                if x1 < 0 or x1 >= DIM or y1 < 0 or y1 >= DIM:
                    disable = True
                    break
            if disable:
                E.add_constraint(~pieceLoc)

# At most one piece can be placed at a location
for x in range(DIM):
    for y in range(DIM):
        constraint.add_at_most_one(E, *(piecesAtLocation[(x,y)]))

# Can only place a piece in one place
for col in pieceLocationsByCol:
    constraint.add_exactly_one(E, *(pieceLocationsByCol[col]))

# If a piece is picked for a location, then the appropriate configuration must be chosen
for col in pieceLocationsByCol:
    for var in pieceLocationsByCol[col]:
        cVar = pieceConfigs[col][var.config_num]
        E.add_constraint(var >> cVar)



# Every location can take on at most one colour
for x in range(DIM):
    for y in range(DIM):
        colAtXY = []
        for col in coloursAtLocation[(x,y)]:
            colAtXY.append(coloursAtLocation[(x,y)][col])
        constraint.add_at_most_one(E, *colAtXY)

# If a piece is placed, then it forces the colours under it
for col in pieceLocationsByCol:
    for var in pieceLocationsByCol[col]:
        for (x,y) in get_coordinates(var):
            if x < DIM and y < DIM:
                E.add_constraint(var >> coloursAtLocation[(x,y)][col])


def add_board_configuration(ind):
    assert ind in BOARDS, "Invalid board number."

    board = BOARDS[ind]

    for x in range(DIM):
        for y in range(DIM):
            if board[x][y] != '_':
                # go from the colour character to the colour string
                col = colMap[board[x][y]]
                E.add_constraint(coloursAtLocation[(x,y)][col])


###################################################################



# Build an example full theory for your setting and return it.
#
#  There should be at least 10 variables, and a sufficiently large formula to describe it (>50 operators).
#  This restriction is fairly minimal, and if there is any concern, reach out to the teaching staff to clarify
#  what the expectations are.
def example_theory(board_num):

    # Add the board constraints
    add_board_configuration(board_num)

    T = E.compile()
    return T


if __name__ == "__main__":

    if len(sys.argv) != 2:
        print(USAGE)
        sys.exit(1)

    board_num = int(sys.argv[1])
    print("\nOk, solving board number %d" % board_num)

    T = example_theory(board_num)
    
    # After compilation (and only after), you can check some of the properties
    # of your model:
    t = time.time()
    sol = T.solve()
    print("Done in %.2f seconds" % (time.time() - t))

    if sol:

        print("\nSatisfiable: True\n")
        visualize(sol, DIM, pieceConfigs, pieceLocations, coloursAtLocation, BOARDS[board_num])

        # Save this solution to file
        with open('solution.txt', 'w') as f:
            f.write(str(sol))
    else:
        print("\nSatisfiable: False\n")

