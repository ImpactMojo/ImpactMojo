# AI Game Agents — MiroFish-Inspired Opponents

## Overview

ImpactMojo's economics games now support **AI-powered opponents** inspired by [MiroFish](https://github.com/666ghj/MiroFish), an open-source swarm intelligence engine. Instead of simple rule-based payoff calculations, games can feature AI agents with distinct personalities, memories, and adaptive strategies — all grounded in South Asian development contexts.

## Architecture

```
┌─────────────────────┐     POST /game-agent     ┌──────────────────────────┐
│  Game Frontend       │ ──────────────────────→  │  Supabase Edge Function   │
│  (101.impactmojo.in) │ ←──────────────────────  │  game-agent/index.ts      │
│                       │    agent decision JSON   │                            │
│  Uses: game-agents.js │                          │  ┌─── LLM API ──────────┐ │
└─────────────────────┘                          │  │  (Haiku / GPT-4o-mini)│ │
                                                   │  └───────────────────────┘ │
                                                   │  ┌─── Fallback Engine ───┐ │
                                                   │  │  (personality weights) │ │
                                                   │  └───────────────────────┘ │
                                                   └──────────────────────────┘
```

### Two Modes

1. **LLM Mode** (Professional/Organization tier): Each agent decision is powered by an LLM call. The agent stays in character, remembers game history, and produces natural-language reasoning. Cost: ~$0.015 per game session.

2. **Fallback Mode** (Free/Practitioner tier or offline): A lightweight engine uses personality weights (cooperation_bias, risk_tolerance, memory_weight) to produce decisions locally in the browser. No API calls needed.

## Files

| File | Purpose |
|------|---------|
| `data/game-agents.json` | Agent personas — names, backstories, personality weights, strategy hints |
| `supabase/functions/game-agent/index.ts` | Edge Function — prompt builder, LLM caller, fallback engine |
| `js/game-agents.js` | Client library — games include this to get agent decisions |
| `js/state-manager.js` | State — `gameSession` and `gameHistory` for tracking AI game sessions |
| `catalog_data.json` | Metadata — `ai_agents` field on each game entry |

## Agent Personas

Each game has 2–4 agents with distinct archetypes:

### Public Good Game
| Agent | Archetype | Cooperation | Description |
|-------|-----------|-------------|-------------|
| Meera | Conditional cooperator | 0.8 | NGO manager, mirrors group behaviour |
| Arjun | Strategic free-rider | 0.25 | Consultant, minimizes contribution |
| Fatima | Reciprocator | 0.6 | Health worker, matches group average |
| Ravi | Unconditional cooperator | 0.95 | Lecturer, contributes regardless |

### Prisoners' Dilemma
| Agent | Archetype | Strategy |
|-------|-----------|----------|
| Sunita | Tit-for-tat | Cooperates first, mirrors opponent |
| Vikram | Grudger | Cooperates until betrayed, then defects forever |
| Lakshmi | Pavlov | Win-stay, lose-shift |
| Deepak | Unpredictable | Random mix, hard to exploit |

### Commons Crisis
| Agent | Archetype | Extraction Tendency |
|-------|-----------|-------------------|
| Priya | Sustainability-first | Low extraction, advocates limits |
| Raj | Short-term optimizer | High extraction, responds only to sanctions |
| Ananya | Institutional builder | Moderate, pushes for governance |
| Karthik | Norm-follower | Matches group average |

(See `data/game-agents.json` for full persona definitions across all 10 AI-enabled games.)

## Integration Guide (for Game Frontends)

### 1. Include the client library

```html
<script src="https://www.impactmojo.in/js/game-agents.js"></script>
```

### 2. Initialize for your game

```javascript
var agents = new IMGameAgents('public-good-game');
```

### 3. Get the agent roster (for UI)

```javascript
agents.getRoster().then(function(roster) {
  roster.forEach(function(agent) {
    // Display agent name, role, location, personality in game UI
    addAgentCard(agent.name, agent.role, agent.location, agent.personality.archetype);
  });
});
```

### 4. Request decisions each round

```javascript
agents.getAllDecisions({
  round: currentRound,
  totalRounds: 10,
  history: gameHistory,          // array of past rounds
  availableActions: ['contribute'],
  context: { max_contribution: 100 }
}).then(function(decisions) {
  // decisions = { 'pg-altruist': { action, amount, reasoning }, ... }
  Object.keys(decisions).forEach(function(agentId) {
    var d = decisions[agentId];
    updateGameState(agentId, d.action, d.amount);
    showAgentReasoning(agentId, d.reasoning);  // optional: show why
  });
});
```

### 5. Track session state

```javascript
// Save session after each round (for resume capability)
IMState.gameSession.set('public-good-game', {
  round: currentRound,
  history: gameHistory,
  agentDecisions: allDecisions,
  playerScore: playerScore,
  timestamp: new Date().toISOString()
});

// On game completion, add to history
IMState.gameHistory.add({
  gameId: 'public-good-game',
  completedAt: new Date().toISOString(),
  rounds: 10,
  playerScore: finalScore,
  usedLLM: true
});
```

## Deployment

### Environment Variables

Set these via `supabase secrets set`:

```bash
supabase secrets set LLM_API_KEY=sk-...
supabase secrets set LLM_BASE_URL=https://api.openai.com/v1
supabase secrets set LLM_MODEL=gpt-4o-mini
```

For Anthropic Claude (via compatible endpoint):
```bash
supabase secrets set LLM_API_KEY=sk-ant-...
supabase secrets set LLM_BASE_URL=https://api.anthropic.com/v1
supabase secrets set LLM_MODEL=claude-haiku-4-5-20251001
```

### Deploy the Edge Function

```bash
supabase functions deploy game-agent
```

### Cost Management

- Free and Practitioner tiers use the **fallback engine** (zero LLM cost)
- Professional tier gets LLM-powered agents (~$0.015/session with GPT-4o-mini)
- Rate limited to 30 requests/minute per user
- At 1,000 sessions/month: ~$10–15/month total LLM cost

## Extending

### Adding a new agent

Add an entry to `data/game-agents.json` under the appropriate game:

```json
{
  "id": "pg-new-agent",
  "name": "Devi",
  "role": "Village Sarpanch",
  "location": "Rajkot, Gujarat",
  "personality": {
    "archetype": "authority-figure",
    "cooperation_bias": 0.7,
    "risk_tolerance": 0.4,
    "memory_weight": 0.8,
    "description": "Uses positional authority to enforce cooperation norms."
  },
  "backstory": "Elected village leader who enforces social contracts.",
  "strategy_hint": "Contribute above average. Punish lowest contributors verbally."
}
```

### Adding a new game

1. Add a new game key in `data/game-agents.json` under `games`
2. Define 2–4 agents with relevant archetypes
3. Add action handling in the fallback engine (both Edge Function and client library)
4. Update `catalog_data.json` with the `ai_agents` field

## Design Principles

1. **South Asian context**: Every agent is a realistic development practitioner, bureaucrat, entrepreneur, or community member from the region.
2. **Pedagogically meaningful**: Agent archetypes map to real economic behaviour types (tit-for-tat, free-rider, conditional cooperator) that students learn in the debrief.
3. **Graceful degradation**: Games work without LLM (fallback engine), without internet (cached agent data), and without login (no auth required for free mode).
4. **Cost-conscious**: LLM calls use the cheapest adequate model. Personality weights handle most decisions without API calls.
