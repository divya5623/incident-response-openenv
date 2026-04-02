# AI Incident Response OpenEnv

An AI-powered environment that simulates real-world production incidents and automatically selects the best mitigation action.

This project demonstrates how intelligent agents can assist in automated incident response and reduce downtime in modern systems.

---

## 🚀 Overview

Modern production systems frequently encounter incidents such as:
- CPU spikes
- Memory leaks
- Service crashes
- Deployment failures
- High error rates

Manual resolution is slow and error-prone. This project introduces an AI-driven environment that simulates incidents and recommends mitigation strategies automatically.

---

## 🧠 Architecture

Incident Generator → AI Agent → Decision Engine → Mitigation Action → System Recovery

---

## ⚙️ Features

- Simulates real-world production incidents  
- AI-based mitigation selection  
- Modular and extensible environment  
- Supports multiple incident scenarios  
- Beginner-friendly structure  
- Lightweight and fast  

---

## 📌 Example Scenario

Input: CPU spike detected  
AI Decision: Restart service  
Result: Service recovered in 3 seconds  

---

## 📂 Project Structure


incident-response-openenv/
│
├── env/
├── agent/
├── scenarios/
├── main.py
├── README.md
└── requirements.txt


---

## ▶️ How to Run

```bash
git clone https://github.com/divya5623/incident-response-openenv
cd incident-response-openenv
python main.py
📊 Sample Output
Incident: Memory leak
Agent Decision: Scale pods
Status: Resolved
Recovery Time: 2.3s
🎯 Use Cases
AI-powered DevOps automation
Incident response training
Reliability engineering experiments
Research on autonomous agents
Production system simulations
🔮 Future Improvements
Reinforcement learning agent
Multi-agent coordination
Dashboard visualization
Integration with monitoring tools
Real-time alert ingestion
🛠️ Tech Stack
Python
AI decision logic
Simulation environment
Modular architecture
🤝 Contribution

Contributions are welcome! Feel free to open issues or submit pull requests.

⭐ Motivation

The goal of this project is to explore intelligent automation in incident response and help developers build more resilient systems.

👩‍💻 Author

Divya Shettar
AI & ML Enthusiast
GitHub: https://github.com/divya5623

📜 License

This project is open-source and available under the MIT License.


---

# ✅ How to use
1. Go to your GitHub repo  
2. Open **README.md**  
3. Click **Edit (✏️)**  
4. **Delete everything**  
5. **Paste this code**  
6. Click **Commit changes**  

Done! 🎉  

Your repo will now look **professional + hackathon ready + Meta-level** 💪# AI Incident Response OpenEnv

## Overview
This project implements an OpenEnv environment that simulates real-world production incidents.  
An AI agent analyzes incidents and selects the best mitigation action.

The objective is to build intelligent agents capable of automated incident response.

---

## Problem Statement
Modern production systems frequently encounter incidents such as:
- CPU spikes
- Service crashes
- Deployment failures
- High error rates

Manual resolution is slow and error-prone.  
This environment enables AI-driven automated mitigation.

---

## Available Actions
The agent can choose one of the following actions:

- scale_up
- restart
- rollback
- notify_team

---

## Multi-Step Environment
- Each episode allows **up to 3 actions**
- Episode ends when:
  - Correct action is taken
  - OR maximum steps reached

This simulates real-world decision making.

---

## Reward Logic

| Action Type | Reward |
|-------------|--------|
| Correct action | +1.0 |
| Partial correct | +0.3 |
| Wrong action | -0.2 |

This encourages efficient and accurate decisions.

---

## Project Structure
.
├── environment.py
├── inference.py
├── tasks/
│ └── incidents.json
├── grader.py
├── Dockerfile
└── README.md

---

## Example Incident
{
"cpu": 95,
"errors": "high",
"correct_action": "scale_up"
}

---

## Goal
Design an AI agent that:
- Detects incident patterns
- Chooses optimal mitigation
- Resolves incidents in minimal steps
- Maximizes reward

---

## Hackathon Highlights
- Real-world production problem
- Multi-step decision environment
- Reinforcement learning compatible
- Clean reward design
- Scalable architecture

---

## Expected Outcome
An intelligent AI agent capable of automated production incident response.

## Evaluation Results

Example run output:

Episodes: 5  
Success Rate: 0.8  
Average Steps: 2.0  
Final Score: 1.25

This environment simulates dynamic production failures and evaluates AI decision efficiency using multi-episode reinforcement scoring.
## How to Run

1. Install Python 3
2. Run:
   python inference.py

The script will simulate multiple incidents and print:
- Success Rate
- Average Steps
- Final Score
