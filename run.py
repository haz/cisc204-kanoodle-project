
from itertools import groupby
from bauhaus import Encoding, proposition, constraint, print_theory
from bauhaus.utils import count_solutions, likelihood

import pprint

# Encoding that will store all of your constraints
E = Encoding()

# Proposition to determine which configuration is used for a coloured piece
@proposition(E)
class PieceConfig:
    def __init__(self, col, config_num) -> None:
        self.col = col
        self.config_num = config_num
    
    def __repr__(self) -> str:
        return f"PieceConfig({self.col}, {self.config_num})"


pieceConfigs = {
    'red': [],
    'green': [],
    'blue': []
}

for col in pieceConfigs:
    for i in range(8):
        pieceConfigs[col].append(PieceConfig(col, i))

for col in pieceConfigs:
    constraint.add_exactly_one(E, *(pieceConfigs[col]))



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


pieceLocations = {
    'red': {i: {} for i in range(8)},
    'green': {i: {} for i in range(8)},
    'blue': {i: {} for i in range(8)}
}

for col in pieceLocations:
    for i in range(8):
        for x in range(4):
            for y in range(4):
                pieceLocations[col][i][(x,y)] = PlacePiece(col, i, x, y)


# specifically restrict that mega-sized red piece
for i in range(len(pieceLocations['red'])):
    for x in range(4):
        for y in range(4):
            if x > 2 or y > 2:
                E.add_constraint(~pieceLocations['red'][i][(x,y)])


# Build an example full theory for your setting and return it.
#
#  There should be at least 10 variables, and a sufficiently large formula to describe it (>50 operators).
#  This restriction is fairly minimal, and if there is any concern, reach out to the teaching staff to clarify
#  what the expectations are.
def example_theory():
    T = E.compile()
    return T


if __name__ == "__main__":

    T = example_theory()
    
    # After compilation (and only after), you can check some of the properties
    # of your model:
    print("\nSatisfiable: %s" % T.satisfiable())
    print("# Solutions: %d" % count_solutions(T))
    # print("   Solution: %s" % T.solve())

    sol = T.solve()

    # Save this solution to file
    with open('solution.txt', 'w') as f:
        f.write(str(sol))

    # pprint.pprint(sol)
    # print_theory(sol)
    # E.introspect(sol, var_level=False)

    # for col in pieceConfigs:
    #     # Print just the index for the true proposition
    #     idx = -1
    #     for i in range(len(pieceConfigs[col])):
    #         if sol[pieceConfigs[col][i]]:
    #             idx = i
    #     print(f"{col} piece is config {idx}")
    
