
from shapes import process

configs = []

# configs.append ("""
# rrbbg
# rbbgg
# rppgg
# ppyoo
# pyyyo
# """)

configs.append ("""
r_r
___
b_b
""")

BOARDS = {i+1: process(configs[i]) for i in range(len(configs))}
