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