# Analysis scripts

Experiments that measure the search algorithm of the Tablut player. They are
kept out of `src/` and `tests/` because they are one-off measurements, not part
of the player.

## `node_count.py`: plain Minimax vs Alpha-Beta

Compares the number of nodes visited by plain Minimax and by the Alpha-Beta
search used in `CookedTree`, from the standard opening position, at increasing
depths.

Run from the repository root:

```bash
uv run scripts/analize/node_count.py                 # Alpha-Beta up to depth 4, plain up to depth 3
uv run scripts/analize/node_count.py --max-plain 2   # faster run
```

Options:

- `--max-alpha-beta N`: deepest depth for Alpha-Beta (default 4).
- `--max-plain N`: deepest depth for plain Minimax (default 3). Plain Minimax
  grows as O(b^d), so depth 4 is skipped by default.

### Output columns

- `Plain nodes`: nodes visited by plain Minimax at that depth.
- `Alpha-Beta nodes`: nodes visited by Alpha-Beta at that depth.
- `Reduction`: plain nodes divided by Alpha-Beta nodes.
- `Root score match`: `yes` if both searches return the same root score. This
  is a correctness check: Alpha-Beta must not change the minimax value.
- `AB time (s)`: wall-clock time of the Alpha-Beta search.

### How it works

- `CountingTablut` subclasses the game and counts every call to
  `_get_game_status`. `CookedTree` calls it exactly once per visited node, so
  the count equals the number of visited nodes.
- The plain Minimax uses the same move generator and the same leaf evaluation
  as `CookedTree`, but without pruning. It calls the base class's
  `_get_game_status` directly, so it is not counted by the subclass.

Node counts do not depend on the machine, so they are a more reliable
comparison than time. Timings are only indicative.
