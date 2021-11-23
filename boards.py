
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
rrbbg
rbbgg
rppgg
ppyoo
pyyyo
""")

configs.append ("""
g__g_
g_gg_
_g___
__gg_
g__g_
""")

configs.append ("""
_____
_____
_____
_____
_____
""")

configs.append ("""
____b
opp_b
_p__r
_g_yr
ggy__
""")

BOARDS = {i+1: process(configs[i]) for i in range(len(configs))}
