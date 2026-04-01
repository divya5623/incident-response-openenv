def compute_score(total_reward, steps):
    efficiency = max(0, (3 - steps)) * 0.2
    return total_reward + efficiency
