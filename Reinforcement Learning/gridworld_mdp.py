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