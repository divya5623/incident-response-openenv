from environment import IncidentEnv
from grader import compute_score

env = IncidentEnv()

episodes = 5
total_score = 0
success = 0
total_steps = 0

for episode in range(episodes):
    obs = env.reset()
    done = False

    total_reward = 0
    steps = 0

    while not done:

        # AI-like decision logic
        score_map = {
            "scale_up": obs["cpu"] / 100,
            "restart": 1 if obs["errors"] == "high" else 0,
            "rollback": 0.2,
            "notify_team": 0.1
        }

        action = max(score_map, key=score_map.get)

        result = env.step(action)

        obs = result["observation"]
        reward = result["reward"]
        done = result["done"]

        total_reward += reward
        steps += 1

    score = compute_score(total_reward, steps)

    total_score += score
    total_steps += steps

    if total_reward > 0:
        success += 1

print("Episodes:", episodes)
print("Success Rate:", success / episodes)
print("Average Steps:", total_steps / episodes)
print("Final Score:", total_score / episodes)
