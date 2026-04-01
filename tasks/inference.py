from environment import IncidentEnv
from grader import compute_score

env = IncidentEnv()

obs = env.reset()
done = False

total_reward = 0
steps = 0

while not done:
    print("Incident:", obs)

    if obs["cpu"] > 90:
        action = "scale_up"
    elif obs["errors"] == "high":
        action = "restart"
    else:
        action = "notify_team"

    result = env.step(action)

    obs = result["observation"]
    reward = result["reward"]
    done = result["done"]

    total_reward += reward
    steps += 1

score = compute_score(total_reward, steps)

print("Total Reward:", total_reward)
print("Steps:", steps)
print("Final Score:", score)
