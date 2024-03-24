
import os
import importlib
import torch
import gym
import sys
import numpy as np
import inspect

def check_promblem_agent(foldername: str) -> bool:
    sarsa_filename = f"{foldername}_hw1_2_taxi_sarsa.pth"
    qlearning_filename = f"{foldername}_hw1_2_taxi_qlearning.pth"

    for filename in [sarsa_filename, qlearning_filename]:
        print(f"Checking {filename}")

        # check whether the file exists or not
        if not os.path.exists(f"{foldername}/{filename}"):
            print(filename + " does not exist")
            return False
        
        try:
            agent = torch.load(f"{foldername}/{filename}")
        except:
            print("Load agent " + foldername + " failed")
            return False
        
        env = gym.make("Taxi-v3")
        state, _ = env.reset()
        
        try:
            action = torch.argmax(agent[state]).item()
        except:
            print("Agent " + foldername + " does not successfully return action")
            return False

        try:
            _, _, _, _, _ = env.step(action)
        except:
            print("Agent " + foldername + " does not successfully take action")
            return False
        
        env.close()
    
    return True


def check_file_integrity(foldernames):

    checking_list = []
    for file in foldernames:
        if not os.path.isdir(file) and "_hw2" in file:
            checking_list.append(file.split("_")[2])
 
    elements = ["data.py","test.py","report.pdf","train.py"]
    
    for name in elements:
        if name not in checking_list:
            print(f"\033[91m 112062892_hw2_{name} IS MISSING\033[0m")
            return False
    
    return True
        


def check_agent(foldernames):

    test_file = None
    for file in foldernames:
        if "hw2_test.py" in file:
            test_file = file

    module_name = test_file.replace('/', '.').replace('.py', '')
    spec = importlib.util.spec_from_file_location(module_name, test_file)
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    try:
        spec.loader.exec_module(module)
        Agent = getattr(module, 'Agent')
        return Agent
    except AttributeError as e:
        return None

        
def check_agent_act(Agent):

    if hasattr(Agent, 'act') and callable(getattr(Agent, 'act')):

        # cheking data form
        act_signature = inspect.signature(Agent.act)
        params = list(act_signature.parameters.keys())
        if len(params) == 2 and params[1] == 'observation':
            print(f"\033[92mAgent Act Function Checking: PASS +5\033[0m")
        else:
            print(f"\033[91mAgent ACT FUNCTION HAS WRONG PARAMETER LIST!\033[0m")
            return False
    else:
        print(f"\033[91mAgent MISSING ACT FUNCTION!\033[0m")
        return False


    return True

def check_data_form(Agent):

    observation_space = gym.spaces.Box(0, 255, [288,512, 3])
    test_obs = observation_space.sample()
    agent = Agent() 
    try:
        action = agent.act(test_obs)

        if action != 0 and action != 1:
            print(f"\033[91mAgent ACT FUNCTION RETURNS ACTION IN WRONG FORM\033[0m")
            return False
    except Exception as e:
        print(e)
        print(f"\033[91mAgent ACT FUNCTION CANNOT HANDLE CORRECT OBSERVATION FORM\033[0m")
        return False
    
    print(f"\033[92mData Form Checking: PASS +5\033[0m")
    return True


# main function
def main():

    score = 0

    foldernames = os.listdir()
    
    # checking
    if check_file_integrity(foldernames):
        print(f"\033[92mFile Checking: PASS +5\033[0m")
        score += 5
    else:
        return

    
    Agent = check_agent(foldernames)
    if Agent == None:
        print(f"\033[91mAgent Class IS MISSING IN TEST FILE\033[0m")
    else:
        print(f"\033[92mAgent Class Checking: PASS +5\033[0m")
        score += 5

    if check_agent_act(Agent):
        score += 5

    if check_data_form(Agent):
        score += 5

    # showing score
        
    print(f"\033[93mScore: {score}/20\033[0m")
    
 
          

if __name__ == "__main__":
    main()