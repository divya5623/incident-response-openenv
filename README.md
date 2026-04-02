# AI Incident Response OpenEnv

An AI-powered environment that simulates real-world production incidents and automatically selects the best mitigation action. This project demonstrates how intelligent agents can assist in automated incident response and reduce downtime in modern systems.

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

Incident → Environment → AI Agent → Decision Engine → Mitigation Action → Reward → System Recovery

---

## ⚙️ Features

- Simulates real-world production incidents  
- AI-based mitigation selection  
- Multi-step decision environment  
- Reinforcement learning compatible  
- Lightweight and modular architecture  
- Extensible for new incident types  
- Beginner-friendly structure  

---

## 🧠 Available Actions

The AI agent can choose:

- `scale_up`
- `restart`
- `rollback`
- `notify_team`

---

## 🔁 Multi-Step Environment

- Each episode allows **up to 3 actions**
- Episode ends when:
  - Correct action is taken  
  - OR maximum steps reached  

This simulates real-world decision making and improves agent planning.

---

## 🎯 Reward Logic

| Action Type     | Reward |
|-----------------|--------|
| Correct action  | +1.0   |
| Partial correct | +0.3   |
| Wrong action    | -0.2   |

---

## 📂 Project Structure


.
├── environment.py
├── inference.py
├── tasks/
│ └── incidents.json
├── grader.py
├── Dockerfile
└── README.md


---

## ▶️ How to Run

```bash
python inference.py
📊 Sample Output
Episode 1
Incident: CPU spike
Action: scale_up
Reward: +1.0
```
Episode 2
Incident: service crash
Action: restart
Reward: +1.0

Episodes: 5
Success Rate: 0.8
Average Steps: 2.0
Final Score: 1.25

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
Simulation environment
AI decision logic
Reinforcement learning compatible design

📈 Evaluation Metrics
Success Rate
Average Steps
Final Score
Recovery Time
Decision Accuracy

#  repository topics 
ai-agent
incident-response
reinforcement-learning
devops
simulation

👩‍💻 Author

Divya Shettar
AI & ML Enthusiast
GitHub: https://github.com/divya5623
