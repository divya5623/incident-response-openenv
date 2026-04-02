import random

class IncidentEnvironment:
    def __init__(self, seed=42):
        random.seed(seed)
        self.max_steps = 3
        self.current_step = 0
        self.state_data = {}
        self.done = False
        self.current_incident = {}

    def reset(self):
        self.current_step = 0
        self.done = False
        # Randomly select an incident
        self.current_incident = random.choice(self._load_incidents())
        self.state_data = self._get_initial_state(self.current_incident)
        return self.state()

    def step(self, action):
        if self.done:
            raise Exception("Episode is done. Call reset().")

        reward = self._apply_action(action)
        self.current_step += 1
        # Check if episode is done
        if action == self.current_incident["best_action"] or self.current_step >= self.max_steps:
            self.done = True

        return self.state(), reward, self.done, {}

    def state(self):
        return self.state_data

    def _load_incidents(self):
        import json
        with open("tasks/incidents.json") as f:
            return json.load(f)

    def _get_initial_state(self, incident):
        # Example: state has CPU, memory, latency, errors, etc.
        return {
            "cpu": incident.get("cpu", 50),
            "memory": incident.get("memory", 50),
            "latency": incident.get("latency", 100),
            "errors": incident.get("errors", "low"),
            "deploy_status": incident.get("deploy_status", "ok"),
        }

    def _apply_action(self, action):
        # Basic reward logic
        if action == self.current_incident["best_action"]:
            reward = 1.0
        elif action in self.current_incident.get("acceptable_actions", []):
            reward = 0.5
        else:
            reward = -0.2
            # Optional: worsen some state metrics
            self.state_data["cpu"] += random.randint(5, 15)
        return reward
