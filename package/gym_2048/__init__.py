from gymnasium.envs.registration import register

from gym_2048.envs.gym_2048_env import Gym2048Env
from gym_2048.envs.gym_2048_model import Gym2048Model
from gym_2048.envs.gym_2048_model import Gym2048State
from gym_2048.envs.gym_2048_model import Gym2048DIRECTIONS

register(
    # gym_2048 is this folder name
    # -v0 is because this first version
    # Gym2048 is the pretty name for gym.make
    id="gym_2048/Gym2048-v0",
    
    # gym_2048.envs is the path gym_2048/envs
    # Gym2048Env is the class name
    entry_point="gym_2048.envs:Gym2048Env",
)