import json
import random

class IncidentEnv:

    def __init__(self):
        with open("tasks/incidents.json") as f:
            self.tasks = json.load(f)
        self.steps = 0
        self.current = None

    def reset(self):
        self.steps = 0
        self.current = random.choice(self.tasks)
        return self.current

    def step(self, action):
        self.steps += 1

        correct = self.current["correct_action"]

        # reward logic
        if action == correct:
            reward = 1.0
        elif action in ["restart", "scale_up", "rollback"]:
            reward = 0.3   # partial correct
        else:
            reward = -0.2  # wrong

        # multi-step episode
        done = self.steps >= 3 or action == correct

        return {
            "observation": self.current,
            "reward": reward,
            "done": done
        }
