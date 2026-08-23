"""
Return = total reward an agent accumulates from a given point onward.
Discounted return = same idea, but future rewards are worth less than
immediate ones, controlled by gamma (0 <= gamma <= 1).
 
G_t = r_t + gamma*r_(t+1) + gamma^2*r_(t+2) + ...
 
gamma close to 0 -> agent is "short-sighted", only cares about immediate reward
gamma close to 1 -> agent is "far-sighted", cares almost equally about distant rewards
"""
 
 
def compute_return(rewards, gamma):
    """rewards: list of rewards received at each timestep, in order."""
    G = 0
    for t, r in enumerate(rewards):
        G += (gamma ** t) * r
    return G

if __name__ == "__main__":
    # same path from 01_gridworld_mdp.py: 5 steps of -1, then +10 at the goal
    rewards = [-1, -1, -1, -1, -1, 10]
 
    print("Same episode, different discount factors:\n")
    for gamma in [0.0, 0.5, 0.9, 0.99, 1.0]:
        G = compute_return(rewards, gamma)
        print(f"gamma = {gamma:<5} -> Return G = {G:.3f}")
 
    print("\n--- Why this matters: comparing two paths to the goal ---")
    # Path A: reaches goal quickly (3 steps then +10)
    path_a = [-1, -1, -1, 10]
    # Path B: reaches the SAME goal but takes a much longer route (8 steps then +10)
    path_b = [-1, -1, -1, -1, -1, -1, -1, -1, 10]
 
    for gamma in [0.5, 0.9, 0.99]:
        ga = compute_return(path_a, gamma)
        gb = compute_return(path_b, gamma)
        print(f"gamma={gamma}: Path A (short) = {ga:.3f}, Path B (long) = {gb:.3f} "
              f"-> {'A preferred' if ga > gb else 'B preferred'}")