# PZ Stats Mod

This is a Project Zomboid Lua mod that tracks game events and logs them for processing.

## Tracked Events

- **Zombie Kills:** Tracks when a player kills a zombie.
- **Player Deaths:** Tracks when a player dies.

## Data Flow

The mod prints JSON-formatted strings to the server console with a `[PZSTATS]` prefix. These logs are intended to be picked up by a log forwarder and sent to the backend API.

Example log:
```
[PZSTATS] {"event": "zombie_kill", "username": "Survivor123"}
```

## Installation

1. Copy the `mod` directory to your Project Zomboid `mods` folder.
2. Enable "PZ Stats" in the game's mod menu.
