#!/usr/bin/env python3

import gymnasium as gym
import gym_2048
import random

def agent_function(state: gym_2048.Gym2048State):
    """
    state: A gym_2048.Gym2048State object. The current state of the environment.
    
    returns: An integer representing the direction to move.
    """
    action = random.choice(gym_2048.Gym2048Model.ACTIONS(state))
    return action

def main():
    # render_mode = None
    render_mode = "ansi"
    # render_mode = "rgb_array"
    # render_mode = "human"

    env = gym.make('gym_2048/Gym2048-v0', render_mode=render_mode)
    observation, info = env.reset()
    state = gym_2048.Gym2048State()
    state.observation = observation
    
    terminated = truncated = False
    if render_mode == "ansi":
        print("Current state:")
        print(env.render())

    DS = gym_2048.Gym2048DIRECTIONS
    while not (terminated or truncated):
        action = agent_function(state)
        if render_mode == "ansi":
            action_name = ""
            match action:
                case DS.UP:
                    action_name = "up"
                case DS.DOWN:
                    action_name = "down"
                case DS.LEFT:
                    action_name = "left"
                case DS.RIGHT:
                    action_name = "right"

            print()
            print(f"Action: moving {action_name}.")
        observation, reward, terminated, truncated, info = env.step(action)
        state.observation = observation
        if render_mode == "ansi":
            print("Current state:")
            print(env.render())

    env.close()
    return

if __name__ == "__main__":
    main()
    

