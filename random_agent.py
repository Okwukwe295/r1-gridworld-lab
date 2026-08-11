import numpy as np

# class GridWorld:
#     '''(7x7) gridworld, with obstacles on (2, 0-5),
#     takes -1 for step and +20 to reach goal'''
#     def __init__(self):
#         self.size = 7 #(7x7), grid size
#         self.start = (6, 0)
#         self.goal = (0, 0)
#         self.obstacle = set((2, col) for col in range(self.size - 1))
#         self.actions = [(-1, 0),(1, 0),(0, -1),(0, 1)]  #[0,1,2,3] => [U, D, L, R]

#         self.reset()  #Restart

#     def reset(self):
#         self.current_state = self.start
#         return self.current_state

#     def step(self, action):
#         # take (state, action) then return (next state, reward)
#         if self.current_state == self.goal:
#             return self.current_state, 0, True

#         dr, dc = self.actions[action]  #Inspect??
#         r, c = self.current_state

#         next_row = r + dr
#         next_col = c + dc

#         if 0 <= next_row < self.size and 0 <= next_col < self.size:     #Boundary
#             if (next_row, next_col) not in self.obstacle:
#                 self.current_state = (next_row, next_col)

#         is_goal = (self.current_state == self.goal)

#         if is_goal:
#             reward = 20
#         else:
#             reward = -1

#         return self.current_state, reward, is_goal


def randomAgent(env, max_steps=50):

    state = env.reset()
    tot_reward = 0

    for step_ in range(1, max_steps+ 1):
        action = np.random.randint(0, 4) #Random action 0 -> 3 corresponding to up, down, left, right
        next_state, reward, done = env.step(action)
        tot_reward += reward
        # print(f"Start State: {state}")

        state = next_state
        if done:
            return step_, tot_reward, True
            # print(f"Step {step_}: Reached Goal {next_state}! Reward: {reward}, Cumulative Reward: {tot_reward}")

    return max_steps, tot_reward, False 
    # if not done:
    #     print(f"Terminated after {max_steps} steps without reaching goal. Final State: {state}, Total Reward: {tot_reward}")


env = GridWorld()
episodes_num = 20
results = np.zeros((episodes_num, 3))

#Experiment
for i in range(20):
    steps, total_reward, goal_reached = randomAgent(env, max_steps=50)
    results[i] = [steps, total_reward, goal_reached]

print(results)

'''20 experiments conducted, in them, i recorded steps taken, total calculated reward, whether or not goal was reached
   Directions 0,1,2,3 were picked strictly random'''
