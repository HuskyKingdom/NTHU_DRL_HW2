import gym


class RandomAgent(object):
    """Agent that acts randomly."""
    def __init__(self):
        self.action_space = gym.spaces.Discrete(2)

    def act(self, observation):
        return self.action_space.sample()
