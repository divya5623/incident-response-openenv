from environment import IncidentEnv

env = IncidentEnv()

obs = env.reset()

print(obs)

if obs["cpu"] > 90:
    action = "scale_up"
else:
    action = "restart"

result = env.step(action)

print(result)
