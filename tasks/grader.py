import json

def grade(episodes_results):
    total_score = 0
    for result in episodes_results:
        total_score += result.get("reward", 0)
    avg_score = total_score / len(episodes_results)
    return avg_score

if __name__ == "__main__":
    # Example usage
    with open("tasks/sample_results.json") as f:
        results = json.load(f)
    score = grade(results)
    print(f"Final Score: {score}")
