# Tablut-Challenge
Repository of my project focused on creating a system that can play the game Tablut.

## Running the Player

The competition launches the player through a single script, `runmyplayer.sh`, with three positional parameters in this exact order:

```bash
./runmyplayer.sh <ROLE> <TIMEOUT> <SERVER_IP>

# example
./runmyplayer.sh WHITE 60 192.168.20.101
```

| # | Parameter | Description |
|---|-----------|-------------|
| 1 | `ROLE` | `WHITE` or `BLACK`. Full word, case-insensitive (`wHitE` must work). |
| 2 | `TIMEOUT` | Seconds allowed per move. May be lower than 60. The referee loses the player on expiry. |
| 3 | `SERVER_IP` | IP address of the referee server. Never hardcode `localhost`. |

The role selects the referee port: `WHITE` connects to `5800`, `BLACK` to `5801`.

Any additional optional parameter must have a default value and be documented in the delivery `.txt` file.

> `runmyplayer.sh` is still a placeholder: it will be implemented once the network infrastructure is finished.

## Development Setup

The project uses [uv](https://docs.astral.sh/uv/) for Python and dependency management, and [Ruff](https://docs.astral.sh/ruff/) for linting and formatting.

### uv

```bash
uv sync                  # create .venv and install all dependencies
uv run tablut-challenge  # run the project entry point
uv add <package>         # add a dependency
uv add --dev <package>   # add a dev-only dependency
uv remove <package>      # remove a dependency
```

- `pyproject.toml` — project metadata and dependencies
- `uv.lock` — locked versions, commit it
- `.python-version` — Python version used by uv (3.12)

### Ruff

```bash
uv run ruff check .          # lint
uv run ruff check --fix .    # lint and auto-fix
uv run ruff format .         # format
```

Ruff rules live in `pyproject.toml` under `[tool.ruff]`.

### VS Code

Install the recommended extensions in `.vscode/extensions.json`, mainly [Ruff](https://marketplace.visualstudio.com/items?itemName=charliermarsh.ruff). Files are then formatted, fixed and import-sorted automatically on save (`cmd + s`).

## Testing

Test individual players during development using the standalone test harnesses in `src/test/`:

```bash

# Terminal 1: Start the Server
cd path/to/server
ant gui-server

# Terminal 2: Connect WHITE player first (connects to port 5800)
uv run python src/test/_test_chess_game_white.py

# Terminal 3: Connect BLACK player second (connects to port 5801)
uv run python src/test/_test_chess_game_black.py
```

**Important:** Always connect WHITE first, then BLACK. The referee waits for both players to connect before starting the game.

### Automated tests

Unit tests for the search live in `tests/` (black-box and white-box, see [docs/test_cases/test_strategy.md](docs/test_cases/test_strategy.md)):

```bash
uv run pytest                  # all tests
uv run pytest -m blackbox      # public-API tests only
uv run pytest -m whitebox      # internal-structure tests only
```

A `pre-commit` hook runs them (with a 100% line + branch coverage gate on `cooked_tree`) before every commit and aborts the commit on failure. Enable it once per clone:

```bash
git config core.hooksPath .githooks
```

## Commit Convention

Commit messages follow [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/).

```text
<type>[optional scope]: <description>

[optional body]

[optional footer]
```

### Types

- `feat` — new feature or change to existing functionality
- `fix` — bug fix
- `refactor` — code change that is neither a feature nor a bug fix
- `style` — formatting changes only (whitespace, semicolons, etc.)
- `perf` — performance improvement
- `test` — adding or updating tests
- `docs` — documentation changes
- `build` — build system or dependency changes
- `ci` — CI configuration changes
- `chore` — anything else that does not touch source or test files
- `revert` — reverts a previous commit

