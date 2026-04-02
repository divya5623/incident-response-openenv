from environment import IncidentEnvironment

if __name__ == "__main__":
    env = IncidentEnvironment()
    print("[START]")
    for episode in range(1, 6):
        state = env.reset()
        done = False
        step_count = 0
        print(f"Episode {episode}")
        while not done:
            # Simple rule-based agent: always pick best_action from incident
            action = env.current_incident["best_action"]
            state, reward, done, _ = env.step(action)
            print(f"Step {step_count+1} - Action: {action} - Reward: {reward}")
            step_count += 1
    print("[END]")
