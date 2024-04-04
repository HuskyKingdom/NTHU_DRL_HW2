from .ddqn import MarioDDQN

try:
    from .agent import MarioAgent
    from .preprocess import MarioPreprocessor
    from .replay_memory import ReplayMemory

    __all__ = ["MarioAgent", "MarioDDQN", "MarioPreprocessor", "ReplayMemory"]
except ModuleNotFoundError as e:
    __all__ = ["MarioDDQN"]
    print(e)
