from environment import IncidentEnv

env = IncidentEnv()

obs = env.reset()
done = False

while not done:
    print("Incident:", obs)

    if obs["cpu"] > 90:
        action = "scale_up"
    elif obs["errors"] == "high":
        action = "restart"
    else:
        action = "notify_team"

    print("Action:", action)

    result = env.step(action)
    obs = result["observation"]
    done = result["done"]

    print("Reward:", result["reward"])

print("Episode finished")
