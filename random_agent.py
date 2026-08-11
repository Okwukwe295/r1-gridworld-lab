import numpy as np
from gridworld import GridWorld

def randomAgent(env, max_steps=50):

    state = env.reset()
    tot_reward = 0
    trajectory = [state]  # Initialize trajectory with the starting state

    for step_ in range(1, max_steps+ 1):
        action = np.random.choice(list(env.actions.keys())) # Randomly select an action from the available actions
        next_state, reward, done = env.step(action)
        tot_reward += reward
        trajectory.append(next_state)  # Add the next state to the trajectory

        state = next_state
        if done:
            return step_, tot_reward, True, trajectory

    return max_steps, tot_reward, False, trajectory


env = GridWorld()
episodes_num = 20
results = []

sample_trajectory = None

#Experiment
for i in range(episodes_num):
    steps, total_reward, goal_reached, trajectory = randomAgent(env, max_steps=50)

    results.append({"steps": steps, "total_reward": total_reward, "goal_reached": goal_reached})

    if i == 0:  # Store the trajectory of the first episode for visualization
        sample_trajectory = trajectory

print(results)

'''20 experiments conducted, in them, i recorded steps taken, total calculated reward, whether or not goal was reached
   Directions 0,1,2,3 were picked strictly random'''
