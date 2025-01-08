import os
import argparse
from stable_baselines3 import PPO, A2C
from stable_baselines3.common.env_util import make_vec_env

# Parse command-line arguments
parser = argparse.ArgumentParser(description="Load and run a reinforcement learning model.")
parser.add_argument("--env_name", type=str, default="Walker2d-v4", help="Name of the environment.")
parser.add_argument("--model_name", type=str, required=True, help="Path to the model file.")
parser.add_argument("--algo", type=str, required=True, choices=["PPO", "A2C", "DQN"], help="Algorithm name.")
args = parser.parse_args()

# Create the environment
vec_env = make_vec_env(args.env_name, n_envs=1)

# Select the algorithm
if args.algo == "PPO":
    model_class = PPO
elif args.algo == "A2C":
    model_class = A2C
else:
    raise ValueError(f"Unsupported algorithm: {args.algo}")

# Load the model
model = model_class.load(args.model_name, env=vec_env)

# Run the model
obs = vec_env.reset()
while True:
    action, _states = model.predict(obs)
    obs, rewards, dones, info = vec_env.step(action)
    vec_env.render("human")

