import gymnasium
from gymnasium import spaces
from gym_2048.envs.gym_2048_model import Gym2048Model
from gym_2048.envs.gym_2048_model import Gym2048State
from gym_2048.envs.gym_2048_model import Gym2048DIRECTIONS
import time
import numpy as np

class Gym2048Env(gymnasium.Env):

    metadata = {
        "render_modes": ["human", "ansi"],
        "render_fps": 1,
    }

    def __init__(self, render_mode=None):
        self.render_mode = render_mode
        # TODO fix this
        self.action_space = spaces.Discrete(4)
        self.observation_space = spaces.Box(0, 2048, shape=(16,), dtype=np.int16)

        return

    def reset(self, seed=None, options=None):
        super().reset(seed=seed)
        self.state = Gym2048State(seed=seed)

        observation = self.state.observation
        info = {}
        return observation, info

    def step(self, action):
        state = self.state
        state1 = Gym2048Model.RESULT(state, action)
        state1.spawn_random()
        self.state = state1
        
        observation = self.state.observation
        reward = Gym2048Model.STEP_COST(state, action, state1)
        terminated = Gym2048Model.GOAL_TEST(state1)
        info = {}

        # display support
        if self.render_mode == "human":
            self.render()
        return observation, reward, terminated, False, info

    def render(self):
        if self.render_mode is None:
            assert self.spec is not None
            gymnasium.logger.warn(
                "You are calling render method without specifying any render mode. "
                "You can specify the render_mode at initialization, "
                f'e.g. gym.make("{self.spec.id}", render_mode="rgb_array")'
            )
            return

        if self.render_mode == "ansi":
            return self._render_text()
        else:
            return self._render_gui(self.render_mode)

    def _render_text(self):
        return str(self.state)

    def _render_gui(self, mode):
        out = str(self.state)
        print(out)
        time.sleep(1 / self.metadata["render_fps"])
        return out
    
    def close(self):
        pass
    


    
