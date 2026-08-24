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

class GridWorld:
    def reset(self):
        self.state = START
        return self.state
 
    def is_terminal(self, s):
        return s == GOAL or s == TRAP
 
    def step(self, action):
        dr, dc = ACTION_DELTAS[action]
        r, c = self.state
        nr, nc = r + dr, c + dc
        if not (0 <= nr < GRID_SIZE and 0 <= nc < GRID_SIZE) or (nr, nc) in WALLS:
            nr, nc = r, c
        self.state = (nr, nc)
        if self.state == GOAL:
            return self.state, 10, True
        elif self.state == TRAP:
            return self.state, -10, True
        else:
            return self.state, -1, False
 
 
def random_policy(state):
    return random.choice(ACTIONS)
 
 
def run_episode(env, policy, start_state=None, first_action=None, max_steps=100):
    """Runs one episode, returns list of (state, action, reward) tuples."""
    state = env.reset()
    if start_state is not None:
        env.state = start_state
        state = start_state
 
    trajectory = []
    for step in range(max_steps):
        if env.is_terminal(state):
            break
        action = first_action if (step == 0 and first_action) else policy(state)
        next_state, reward, done = env.step(action)
        trajectory.append((state, action, reward))
        state = next_state
        if done:
            break
    return trajectory
 
 
def compute_returns(trajectory, gamma):
    """Given [(s,a,r), ...], compute the discounted return from each timestep onward."""
    returns = []
    G = 0
    for (s, a, r) in reversed(trajectory):
        G = r + gamma * G
        returns.append(G)
    return list(reversed(returns))
 
 
def estimate_V(env, policy, n_episodes=2000, gamma=GAMMA):
    state_returns = defaultdict(list)
    for _ in range(n_episodes):
        traj = run_episode(env, policy)
        returns = compute_returns(traj, gamma)
        for (s, a, r), G in zip(traj, returns):
            state_returns[s].append(G)
    return {s: sum(vals) / len(vals) for s, vals in state_returns.items()}
 
 
def estimate_Q(env, policy, state, action, n_episodes=500, gamma=GAMMA):
    """Estimate Q(state, action): take `action` from `state`, then follow policy."""
    total = 0
    for _ in range(n_episodes):
        traj = run_episode(env, policy, start_state=state, first_action=action)
        returns = compute_returns(traj, gamma)
        total += returns[0] if returns else 0
    return total / n_episodes
 
 
if __name__ == "__main__":
    env = GridWorld()
 
    print("Estimating V(s) under a random policy (2000 episodes)...\n")
    V = estimate_V(env, random_policy)
    for r in range(GRID_SIZE):
        row = []
        for c in range(GRID_SIZE):
            s = (r, c)
            if s in WALLS:
                row.append("  WALL ")
            elif s == GOAL:
                row.append("  GOAL ")
            elif s == TRAP:
                row.append("  TRAP ")
            else:
                row.append(f"{V.get(s, 0):7.2f}")
        print(" ".join(row))
 
    print("\nEstimating Q(s,a) for the start state (0,0), each action:")
    for action in ACTIONS:
        q = estimate_Q(env, random_policy, START, action)
        print(f"  Q({START}, {action:6s}) = {q:.3f}")
 