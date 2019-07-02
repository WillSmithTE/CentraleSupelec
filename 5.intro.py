import torch
import numpy as np
import gym
env = gym.make('CartPole-v0')
env = env.unwrapped
s = env.reset()
while True:
	env.render()
