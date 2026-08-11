from gridworld import GridWorld


_env_for_states = GridWorld()
v_star = {
    (r, c): 0
    for r in range(_env_for_states.rows)
    for c in range(_env_for_states.cols)
    if (r, c) not in _env_for_states.obstacles
}


# Greedy action selection

def predict_next_state(env, state, action):
    """Mirrors GridWorld.step()'s transition logic, without mutating env."""
    row_change, col_change = env.actions[action]
    candidate = (state[0] + row_change, state[1] + col_change)

    if env.is_valid_state(candidate):
        next_state = candidate
    else:
        next_state = state  

    reward = 20 if next_state == env.goal_state else -1
    return next_state, reward


def select_greedy_action(env, state, v_star):
    """pi*(s) = argmax_a [ r(s,a) + v*(s') ], per the one-step lookahead
    result from the slides: given the true v*, no deeper search is needed."""
    best_action, best_value = None, float('-inf')

    for action in env.actions:
        next_state, reward = predict_next_state(env, state, action)
        value = reward + v_star.get(next_state, 0)
        if value > best_value:
            best_value = value
            best_action = action

    return best_action



def greedyAgent(env, v_star, max_steps=100):
    state = env.reset()
    tot_reward = 0
    trajectory = [state]  

    for step_ in range(1, max_steps + 1):
        action = select_greedy_action(env, state, v_star)
        next_state, reward, done = env.step(action)  
        tot_reward += reward
        trajectory.append(next_state)

        state = next_state
        if done:
            return step_, tot_reward, True, trajectory

    return max_steps, tot_reward, False, trajectory


env = GridWorld()
episodes_num = 20
results = []

sample_trajectory = None

# Experiment
for i in range(episodes_num):
    steps, total_reward, goal_reached, trajectory = greedyAgent(env, v_star, max_steps=100)

    results.append({"steps": steps, "total_reward": total_reward, "goal_reached": goal_reached})

    if i == 0:  # Store the trajectory of the first episode for visualization
        sample_trajectory = trajectory

print(results)

'''20 experiments conducted, in them, i recorded steps taken, total calculated reward,
   and whether or not the goal was reached. Actions were chosen greedily using v*,
   via one-step lookahead: pi*(s) = argmax_a [ r(s,a) + v*(s') ]'''