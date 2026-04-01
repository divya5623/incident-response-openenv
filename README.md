# AI Incident Response OpenEnv

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
