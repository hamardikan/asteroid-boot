# Asteroid Boot

A small Pygame arcade shooter inspired by the classic Asteroids loop. Fly a triangular ship, dodge incoming rocks, and shoot them to split them into smaller pieces.

## Features
- Smooth ship movement and rotation
- Continuous asteroid spawns from screen edges
- Asteroid splitting on hit
- Basic event/state logging to JSONL

## Requirements
- Python 3.13
- Pygame 2.6.1

## Install
If you use uv:

```bash
uv sync
```

If you use pip:

```bash
pip install pygame==2.6.1
```

## Run

```bash
python main.py
```

## Controls
- `W`/`S`: thrust forward/back
- `A`/`D`: rotate left/right
- `Space`: shoot
- Close the window to quit

## Logs
The game writes logs in the project root each run:
- `game_state.jsonl`: periodic snapshots of sprite counts/positions
- `game_events.jsonl`: notable events (hits, splits)

## Notes
If the window is small or off-screen, check `SCREEN_WIDTH` and `SCREEN_HEIGHT` in `constants.py`.
