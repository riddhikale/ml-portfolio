"""
Dynamic Programming solves the MDP exactly (no simulation needed) because we
know the environment's rules - transitions and rewards - in advance.
 
Policy Evaluation: repeatedly apply the Bellman expectation equation
    V(s) = sum_a pi(a|s) * [R(s,a) + gamma * V(s')]
until V stops changing (converges).
 
Policy Improvement: for each state, switch to whichever action looks best
according to the current V - "greedy" with respect to V.
 
Policy Iteration: alternate evaluation and improvement until the policy
itself stops changing - this is GUARANTEED to converge to the optimal policy.
"""