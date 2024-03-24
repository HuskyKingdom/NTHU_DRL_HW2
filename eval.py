from xml.etree import ElementTree as ET
import importlib.util
import sys
import os

# retrive submission meta info
xml_file_path = 'meta.xml'

tree = ET.parse(xml_file_path)
root = tree.getroot()

sub_name = ""

for book in root.findall('info'):
    sub_name =  book.find('name').text

# initializing agent
agent_path = sub_name + "_hw2_test.py"
module_name = agent_path.replace('/', '.').replace('.py', '')
spec = importlib.util.spec_from_file_location(module_name, agent_path)
module = importlib.util.module_from_spec(spec)
sys.modules[module_name] = module
spec.loader.exec_module(module)
Agent = getattr(module, 'Agent')

os.environ["SDL_AUDIODRIVER"] = "dummy"

# evaluating
import time
import flappy_bird_gym
from tqdm import tqdm

total_reward = 0
total_time = 0
env = flappy_bird_gym.make("FlappyBird-rgb-v0")
obs = env.reset()

for episode in tqdm(range(100), desc="Evaluating"):
    obs = env.reset()
    start_time = time.time()
    episode_reward = 0
    
    while True:
        action = Agent.act(obs) 

        obs, reward, done, info = env.step(action)
        episode_reward += reward

        if done:
            break

    end_time = time.time()
    total_reward += episode_reward
    total_time += (end_time - start_time)

env.close()

score = total_reward / total_time
print(f"Final Score: {score}")