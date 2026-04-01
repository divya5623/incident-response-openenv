# AI Incident Response OpenEnv

## Problem
This environment simulates real-world production incidents such as:
- CPU spikes
- Service crashes
- Deployment failures

The AI agent must choose the correct mitigation action.

## Actions
- scale_up
- restart
- rollback
- notify_team

## Reward
- Correct action: +1.0
- Wrong action: -0.5

## Files
- environment.py → environment logic
- tasks/ → incidents
- grader.py → scoring
- inference.py → AI agent
- Dockerfile → container

## Goal
Train AI agent to resolve incidents efficiently.
## Multi-Step Environment
The agent can take up to 3 actions before the episode ends.

## Reward Logic
- Correct action: +1.0
- Partial correct: +0.3
- Wrong action: -0.2

## Goal
Resolve incidents using correct mitigation steps.
