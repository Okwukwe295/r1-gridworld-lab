class GridWorld:

    def __init__(self):
        self.rows = 7
        self.cols = 7 

        self.start_state = (6, 0)
        self.goal_state = (0, 0)

        self.obstacles = {(2,0), (2,1), (2,2), (2,3), (2,4), (2,5)}

        self.actions = {
            'up': (-1, 0),
            'down': (1, 0),
            'left': (0, -1),
            'right': (0, 1)
        }

        self.state = self.start_state

    def reset(self):
        self.state = self.start_state
        return self.state

    def is_valid_state(self, state):
        row, col = state
        return 0 <= row < self.rows and 0 <= col < self.cols and state not in self.obstacles

    def step(self, action):
        if action not in self.actions:
            raise ValueError(f"Invalid action: {action}")

        row_change, col_change = self.actions[action]
        new_state = (self.state[0] + row_change, self.state[1] + col_change)

        is_valid = self.is_valid_state(new_state)

        if is_valid:
            self.state = new_state
        else:
            new_state = self.state  # Stay in the same state if the move is invalid

        reward = 20 if new_state == self.goal_state else -1

        if new_state == self.goal_state:
            done = True
        else:
            done = False

        return new_state, reward, done