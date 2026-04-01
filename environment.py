import json
import random

class IncidentEnv:

    def __init__(self):
        with open("tasks/incidents.json") as f:
            self.tasks = json.load(f)
        self.current = None
        self.steps = 0

    def reset(self):
        self.current = random.choice(self.tasks).copy()
        self.steps = 0
        return self.current

    def step(self, action):
        self.steps += 1

        correct = self.current["correct_action"]

        # dynamic state update
        if action == "scale_up":
            self.current["cpu"] = max(10, self.current["cpu"] - 30)
        if action == "restart":
            self.current["errors"] = "low"

        # reward logic
        if action == correct:
            reward = 1.0
        elif action in ["scale_up", "restart", "rollback"]:
            reward = 0.3
        else:
            reward = -0.2

        done = action == correct or self.steps >= 3

        return {
            "observation": self.current,
            "reward": reward,
            "done": done
        }
