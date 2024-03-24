<br />
<div align="center" id="readme-top">
  
  <h1 align="center">Leaderboard Submission Guide</h1>
  <h3 align="center">Deep Reinforcement Learning Class 2024 Programming Homework 2 | National Tsing Hua University</h3>

Due: 2022/04/09 (Tue.) 23:59

  <p align="center" >



[<img src="https://raw.githubusercontent.com/Talendar/flappy-bird-gym/main/imgs/blue_bird_playing.gif" height=450>]

</div>



## Problem Description

### Overview & Installation

Flappy Bird for OpenAI Gym ("<Student_ID>\_hw2_<train|test>.py"), please referring to [flappy_bird_gym](https://github.com/Talendar/flappy-bird-gym). This is a set of OpenAI Gym environments for the Flappy Bird game.

There are two types of environment in the package, the "FlappyBird-rgb-v0" environment, yields RGB-arrays (images) representing the game's screen. The "FlappyBird-v0" environment, on the other hand, yields simple numerical information about the game's state as observations. 

## Leaderboard Submission

We provide leaderboard for you to compare with your classmate, the ranking of which will be a significant reference of your overall score base on the your relative ranking position.

To submit your code to leaderboard, you will need to first fork this repo and clone it to your local environment:

```
git clone <Your forked repo>
```

Now replace `112062892_hw2_*` files in the repo with your own version of them. The following packages were installed by default in repo cloud environment:

- Python 3.8
- flappy-bird-gym 
- torch (CPU)

If you wish to add more dependencies inorder to run your code, please add them into `requirements.txt`, each raw for one dependency.

Once you are happy with it, commit & push them to your forked repo:

```
git commit -m "submission"
git push
```

Pushing to the repo will trigger the following procedure:

1. Creating virtual env & installing dependencies
2. Check your submission
3. Run your code and return a score if checking succeed
4. Push the socre to the leaderboard