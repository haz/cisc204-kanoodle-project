

# Strip whitespace from the strings, and break into array of lines
def process(shape):
    shape = shape.strip()
    shape = [l.strip() for l in shape.split("\n")]
    return [[shape[y][x] for y in range(len(shape))] for x in range(len(shape[0]))]


def gen_yellow():
    shapes = []
    # Define yellow up
    shapes.append("""

        -X-
        XXX

    """)
    # Define yellow down
    shapes.append("""

        XXX
        -X-

    """)
    # Define yellow left
    shapes.append("""

        -X
        XX
        -X

    """)
    # Define yellow right
    shapes.append("""

        X-
        XX
        X-

    """)
    return shapes
yellow = [process(s) for s in gen_yellow()]

def gen_orange():
    shapes = []
    # Define orange up
    shapes.append("""

        -X
        XX

    """)
    # Define orange down
    shapes.append("""

        XX
        -X

    """)
    # Define orange left
    shapes.append("""

        X-
        XX

    """)
    # Define orange right
    shapes.append("""

        XX
        X-

    """)
    return shapes
orange = [process(s) for s in gen_orange()]

def gen_blue():
    shapes = []
    # Define blue up1
    shapes.append("""

        -X
        XX
        X-

    """)
    # Define blue up2
    shapes.append("""

        X-
        XX
        -X

    """)
    # Define blue side1
    shapes.append("""

        XX-
        -XX

    """)
    # Define blue side2
    shapes.append("""

        -XX
        XX-

    """)
    return shapes
blue = [process(s) for s in gen_blue()]

def gen_pink():
    shapes = []
    # Define pink1
    shapes.append("""
    
        XX-
        -XX
        --X
        
    """)
    # Define pink2
    shapes.append("""

        --X
        -XX
        XX-

    """)
    # Define pink3
    shapes.append("""

        X--
        XX-
        -XX

    """)
    # Define pink4
    shapes.append("""

        -XX
        XX-
        X--

    """)
    return shapes
pink = [process(s) for s in gen_pink()]

def gen_red():
    shapes = []
    # Define red up 1
    shapes.append("""

        X-
        X-
        XX

    """)
    # Define red up 2
    shapes.append("""

        -X
        -X
        XX

    """)
    # Define red left 1
    shapes.append("""

        XXX
        --X

    """)
    # Define red left 2
    shapes.append("""
    
        --X
        XXX

    """)
    # Define red right 1
    shapes.append("""

        XXX
        X--

    """)
    # Define red right 2
    shapes.append("""

        X--
        XXX

    """)
    # Define red down 1
    shapes.append("""

        XX
        -X
        -X

    """)
    # Define red down 2
    shapes.append("""

        XX
        X-
        X-

    """)
    return shapes
red = [process(s) for s in gen_red()]

def gen_green():
    shapes = []
    # Define green up 1
    shapes.append("""

        X-
        XX
        XX

    """)
    # Define green up 2
    shapes.append("""

        -X
        XX
        XX

    """)
    # Define green left 1
    shapes.append("""

        XXX
        -XX

    """)
    # Define green left 2
    shapes.append("""

        -XX
        XXX

    """)
    # Define green right 1
    shapes.append("""

        XXX
        XX-

    """)
    # Define green right 2
    shapes.append("""

        XX-
        XXX

    """)
    # Define green down 1
    shapes.append("""

        XX
        XX
        -X

    """)
    # Define green down 2
    shapes.append("""

        XX
        XX
        X-

    """)
    return shapes
green = [process(s) for s in gen_green()]


SHAPES = {
    "yellow": yellow,
    "orange": orange,
    "blue": blue,
    "pink": pink,
    "red": red,
    "green": green
}
