import json
import random

class IncidentEnv:

    def __init__(self):
        with open("tasks/incidents.json") as f:
            self.tasks = json.load(f)

    def reset(self):
        self.current = random.choice(self.tasks)
        return self.current

    def step(self, action):
        correct = self.current["correct_action"]

        if action == correct:
            reward = 1.0
        else:
            reward = -0.5

        done = True

        return {
            "observation": self.current,
            "reward": reward,
            "done": done
        }
