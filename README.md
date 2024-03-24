<br />
<div align="center" id="readme-top">
  
  <h1 align="center">Programming Homework 2</h1>
  <h3 align="center">Deep Reinforcement Learning Class 2024 | National Tsing Hua University</h3>

Due: 2022/04/09 (Tue.) 23:59

  <p align="center" >



[<img src="https://raw.githubusercontent.com/Talendar/flappy-bird-gym/main/imgs/blue_bird_playing.gif" height=450>]

</div>



## Problem Description

### Overview & Installation

Flappy Bird for OpenAI Gym ("<Student_ID>\_hw2_<train|test>.py"), please referring to [flappy_bird_gym](https://github.com/Talendar/flappy-bird-gym). This is a set of OpenAI Gym environments for the Flappy Bird game.

There are two types of environment in the package, the "FlappyBird-rgb-v0" environment, yields RGB-arrays (images) representing the game's screen. The "FlappyBird-v0" environment, on the other hand, yields simple numerical information about the game's state as observations. 

In this assignment, you are required to use **FlappyBird-rgb-v0** environment.

It is recommanded to use virtual environment like conda to manage your code base. Flappy Bird for OpenAI Gym supports a wide range of python versions (from 3.6-3.9), install `flappy-bird-gym` directly by:

```
pip install flappy-bird-gym
```

Note that if in case you encounter some error when installing gym==0.18 and thus failed to install flappy-bird-gym, try run the following first then install again:

```
pip install setuptools==65.5.0 pip==21
pip install wheel==0.38.0
```

### Environment Spaces

**Action Space** - gym.spaces.Discrete(2) | (Zero `0` means "do nothing" and one `1` means "flap")

**Observation Space** - gym.spaces.Box(0, 255, [288,512,3]) | Numpy array of shape `(288,512,3)`

**Reward** - `reward = 1` for all timesteps.

### Programming Requirements

1. Implement and train your agent in **FlappyBird-rgb-v0** environment.
2. You are required to use DQN as your core algorithm, but other improvements are allowed (optional).
3. You must write all your training and testing code by yourself.
4. You may store your learned model in an external file “./<Student_ID>_hw2_data”, and access it with your program (during testing).
5. You should implement a class called `Agent` with the member function `act(observation)` function in your testing code. See `random_agent.py` for an example.
6. If your program outputs invalid moves, you lose and the game ends immediately.
7. Time limit for each move is 1 second, and the memory limit is 4 GB. (Note that the 1-second duration may vary depending on different processors. If you use a DQN-based agent and it doesn’t perform additional calculations during inference, you don’t need to worry about the time limit.)
8. You are allowed to use the following Python package:
- numpy, scipy, gym, pandas, tensorflow, pytorch and the packages mentioned in the environment’s repo.
- You are allowed to use Python default installed packages.
(e.g., sys, time, pickle, random, etc.)
- If you need to use other packages, state your reasons and post on hackmd.
- You are not allowed to use any read-made RL algorithms like stablebaseline3.

### Other Requirements

Write a report to:

1. Elaborate on how you design your agent. What advanced techniques of DQN do you use? The report is graded directly. So, make sure you have included enough details and figures to help TAs grade your report.

2. TAs will not refer to your code when grading your report, so make sure you have taken a screenshot of the important code snippets.


## Problem Submission

For each problem, please use Python to implement with a single source file.

Your files must be named as:
- “<Student_ID>_hw2_train.py”
- “<Student_ID>_hw2_test.py”
- “<Student_ID>_hw2_data”
- “<Student_ID>_hw2_report.pdf”

and please make sure that all characters of the filename are in lower case. For example, if your student id is 110062579, the name of your program file should be 110062579_hw2_train.py and so on.

0 points will be given to **Plagiarism**. NEVER SHOW YOUR CODE to others and you must write your code by yourself. If the codes are similar to other people and you can’t explain your code properly, you will be identified as plagiarism.

0 points will be given if you violate the rules above.
If you use modularized / OOP code and want to use multiple files to keep your code structured, please upload it along with the 3 files above.


## Grading Policy

1. The project accounts for 15 points (tentative) of your total grade.

2. You must submit both your source code and report. Remember the submission rules mentioned
above, or you will be punished on your grade. Late submission rules are specified in the Lecture
1 Slides.

3. 