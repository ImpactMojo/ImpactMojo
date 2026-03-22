---
name: memory
description: Read, update, or query Claude's persistent memory for this project. Use when the user says "remember this", "what do you remember", "update memory", "add to memory", "forget", or at session start/end to sync context.
---

# Claude Memory Management

Manage persistent context at two levels:
- **Global** (`~/.claude/memory.md`): user preferences, cross-project notes
- **Project** (`.claude/memory.md`): project-specific state, decisions, session logs

Both files are read at session start for full context.

## Commands

Based on the user's intent, perform ONE of these operations:

### 1. **Read memory** (default if no args, or "what do you remember")
- Read both `~/.claude/memory.md` (global) and `.claude/memory.md` (project)
- Summarize the current state from both levels
- Highlight any stale entries (dates older than 30 days)

### 2. **Remember / Add** (user says "remember X" or "add to memory")
- Read `.claude/memory.md`
- Append the new information to the appropriate section:
  - Decisions → `## Recent Decisions`
  - Bugs/issues → `## Known Issues`
  - State changes → `## Project State`
- Prepend a `- **YYYY-MM-DD**: ` prefix to the entry
- Write the updated file

### 3. **Log session** (triggered at session end or "log this session")
- Read `.claude/memory.md`
- Append to `## Session Log`:
  ```
  - **YYYY-MM-DD**: [brief summary of what was accomplished]
  ```
- Update `## Project State` if content counts or architecture changed
- Write the updated file

### 4. **Forget** (user says "forget X" or "remove from memory")
- Read `.claude/memory.md`
- Remove the matching entry
- Write the updated file

### 5. **Sync counts** (user says "sync memory" or after content changes)
- Grep `index.html` for current game/course/lab/handout counts
- Update `## Project State` with accurate numbers
- Update `Last verified` date
- Write the updated file

## Rules

- Always read the file before writing to avoid data loss
- Keep entries concise — one line per item
- Use ISO dates (YYYY-MM-DD)
- Never store secrets, API keys, or credentials
- Project memory (`.claude/memory.md`) is committed to git — keep it safe for version control
- Global memory (`~/.claude/memory.md`) is user-local, not committed
- When adding cross-project notes, write to global; project-specific to project
- Works on both local CLI and Claude Code web (web reads from repo files)
