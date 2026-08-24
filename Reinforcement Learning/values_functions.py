"""
V(s)   = expected return starting from state s, following policy pi
Q(s,a) = expected return starting from state s, taking action a, then following pi
 
Both are estimated here via Monte Carlo: run many episodes under a fixed
(random) policy, and average the actual returns observed from each
state (for V) or state-action pair (for Q).
 
This is intentionally the "dumbest" way to estimate these - full brute-force
simulation - so the definitions are concrete before Dynamic Programming
(next topic) shows a smarter way to compute them exactly, without simulation.
"""
 
import random
from collections import defaultdict
 
GRID_SIZE = 4
START = (0, 0)
GOAL = (3, 3)
TRAP = (2, 3)
WALLS = {(1, 1), (2, 2)}
ACTIONS = ["up", "down", "left", "right"]
ACTION_DELTAS = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}
GAMMA = 0.9

