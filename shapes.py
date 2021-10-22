
blue = []

# Define blue up
blue.append("""

    ---
    -X-
    XXX

""")
# Define blue down
blue.append("""

    XXX
    -X-
    ---

""")
# Define blue left
blue.append("""

    --X
    -XX
    --X

""")
# Define blue right
blue.append("""

    X--
    XX-
    X--

""")


red = []
# Define red up
red.append("""

    -X
    XX

""")
# Define red down
red.append("""

    XX
    -X

""")
# Define red left
red.append("""

    X-
    XX

""")
# Define red right
red.append("""

    XX
    X-

""")

# Strip whitespace from the strings, and break into array of lines
def process(shape):
    shape = shape.strip()
    shape = [l.strip() for l in shape.split("\n")]
    return [[shape[y][x] for y in range(len(shape))] for x in range(len(shape[0]))]

blue = [process(s) for s in blue]
red = [process(s) for s in red]

SHAPES = {
    "blue": blue,
    "red": red
}
