"""
A minimal GridWorld to represent an MDP concretely:
- States: each cell on the grid
- Actions: up, down, left, right
- Transition: deterministic - taking an action moves you to the adjacent cell
- Reward: -1 per step (encourages shortest path), +10 at goal, -10 at trap
- Terminal states: goal and trap end the episode
 
Grid layout (4x4):
  S . . .
  . # . .
  . . # T
  . . . G
 
S = start, G = goal, T = trap, # = wall (blocked cell)
"""

GRID_SIZE = 4
START = (0, 0)
GOAL = (3, 3)
TRAP = (2, 3)
WALLS = {(1, 1), (2, 2)}
 
ACTIONS = ["up", "down", "left", "right"]
ACTION_DELTAS = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

class GridWorld:
    def __init__(self):
        self.state = START
 
    def reset(self):
        self.state = START
        return self.state
 
    def is_terminal(self, state):
        return state == GOAL or state == TRAP
 
    def step(self, action):
        """Applies an action, returns (next_state, reward, done) - the core MDP transition."""
        if self.is_terminal(self.state):
            raise ValueError("Episode already ended - call reset() first")
 
        dr, dc = ACTION_DELTAS[action]
        r, c = self.state
        new_r, new_c = r + dr, c + dc
 
        # stay in place if move goes off-grid or into a wall
        if not (0 <= new_r < GRID_SIZE and 0 <= new_c < GRID_SIZE) or (new_r, new_c) in WALLS:
            new_r, new_c = r, c
 
        next_state = (new_r, new_c)
        self.state = next_state
 
        if next_state == GOAL:
            reward, done = 10, True
        elif next_state == TRAP:
            reward, done = -10, True
        else:
            reward, done = -1, False
 
        return next_state, reward, done