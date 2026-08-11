# 7x7 Gridworld MDP

Reinforcement Learning - COMS4061A/7071A

Members: Okwukwechukwu Mbajiorgu (2430639), 

Implementation of the 7x7 Gridworld MDP from the Markov Decision
Processes lab.

## Environment

- Grid size: 7x7
- Initial state: bottom-left
- Goal state: top-left
- Actions: up, down, left, right
- Actions are deterministic
- Third row from the top contains obstacles except for the right-most cell
- Reward for reaching the goal: +20
- Reward for every other action: -1
- Discount factor: 1 (no discounting)

## Files

- `gridworld.py` - Gridworld MDP
- `random_agent.py` - Random policy
- `greedy_agent.py` - Greedy policy using the optimal value function
- `experiment.py` - Experiments and visualisation