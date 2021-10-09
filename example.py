
from bauhaus import Encoding, proposition, utils, print_theory


E = Encoding()

@proposition(E)
class V:
    def __init__(self, n) -> None:
        self.n = n
    def __repr__(self):
        return 'v' + str(self.n)

v1 = V(1)
v2 = V(2)
v3 = V(3)

E.add_constraint(v1 >> v2)
E.add_constraint(~(v2 & v3))

T = E.compile()
sol = T.solve()

E.introspect()
input()

print(sol)
input()

print("Theory with true literals:")
E.pprint(T, sol)
input()

print("Theory with true variables:")
E.pprint(T, sol, var_level=True)
input()

print_theory(sol)
input()

print("             Total Solutions: %d" % utils.count_solutions(T))
input()

print("Total Solutions w/ [v3, ~v2]: %d" % utils.count_solutions(T, [v3, ~v2]))
input()

print(" Likelihood of v1 being true: %f" % utils.likelihood(T, v1))
input()

print("Done!")
