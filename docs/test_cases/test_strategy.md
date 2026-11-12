# CookedTree Test Strategy

Scope: [`src/tablut/cooked_tree/cooked_tree.py`](../../src/tablut/cooked_tree/cooked_tree.py)
(the Minimax + Alpha-Beta search core). The tests live in [`tests/`](../../tests).

## 1. Goals and scope

**What we want to guarantee**: whatever optimisation comes next (move ordering, iterative
deepening, transposition table, a C++ port), the search is *not computing wrong results*.
A search bug raises no exception: the agent silently plays worse and the cause is very hard to
spot in real games, so automated tests have to catch it.

| Scope | Description |
|---|---|
| In scope | Search logic, alpha-beta pruning, make/undo move, root move selection, order of the terminal/depth checks, piece enumeration |
| Out of scope | **Repeated positions (draw)** and **heuristic quality**: not implemented / not verified yet |
| Covered separately | **The Tablut rules** in `CookedTablut` (legal moves, captures, king capture): [`tests/cooked_tablut/test_tablut_rules.py`](../../tests/cooked_tablut/test_tablut_rules.py), with expected results taken from the referee's Java engine (`GameAshtonTablut.java`) |
| Out of scope | Network/socket layer and `game_interface` (they need the referee server; the manual scripts in `src/test/_*.py` cover them) |

> These tests verify that **the search is correct for any rule set**, not that the Tablut rules are correct.

## 2. Test-double design

The rules are not implemented yet, so the three rule functions of `CookedTree` can be **injected**
(`heuristic`, `game_status`, `is_valid_movement`); the defaults are still the original TODO
implementations. The tests inject simple **fake rules** ([`tests/tree_helpers.py`](../../tests/tree_helpers.py)):

- **Rook-like moves**: orthogonal slides, cannot cross or land on a piece, cannot leave the board, no captures.
- **Seeded heuristic**: a seeded random table, White perspective, very few ties, so pruning mistakes show up.
- **Constant heuristic**: every leaf is equal; used to test equality cut-offs and tie-breaking.
- **Programmable status**: e.g. "king on the top row means WHITE_WIN", used to build tactical scenarios.

Why: with injection there is no need to replace functions through name mangling
(`_CookedTree__xxx`), so renaming a function cannot make a test silently stop working. The few places
that must reach a private method (`__make_move`, ...) all go through `private()`, so a rename needs a
single fix.

## 3. Test levels and techniques

### 3.1 Black-box tests (`tests/cooked_tree/test_blackbox_search.py`, marker `blackbox`)

Only the public API `get_next_movement` is used; nothing is assumed about the implementation.

| Technique | Where it is used |
|---|---|
| **Differential testing (oracle)** | Compared with a plain Minimax without pruning. The oracle generates moves on its own (it does not reuse `CookedTree`'s vector table), so missing moves and wrong cut-offs are both detected |
| **Property testing** | Seeded random boards: the move is legal, the true value of the move equals the reported score, the score is within `[-INF, INF]`, the input board is not modified |
| **Scenario testing** | Concrete tactics: taking an immediate win, blocking the only escape, blocking Black's winning path, the effect of search depth |
| **Equivalence partitioning** | The three terminal statuses (White win / Black win / draw) x both roles; with / without legal moves |
| **Boundary-value analysis** | Longest slide (8 cells) in all four directions, depth limit, no legal move, no pieces, lone king |
| **State-leak testing** | The same object handles different boards in a row and the results stay reproducible |

### 3.2 White-box tests (`tests/cooked_tree/test_whitebox_internals.py`, marker `whitebox`)

Designed from the internal structure; the target is **every branch** and **every comparison operator**.

| Technique | Where it is used |
|---|---|
| **Statement / branch coverage** | 100% line and branch coverage of `cooked_tree.py` is required (see section 5) |
| **Structure checks** | Move-vector table (32 entries, no duplicates, every rook displacement), piece enumeration (White includes the king, row-major order) |
| **State checks for make/undo** | Leaving the throne leaves `THRONE`, undo restores the target's *original* content instead of a fixed `EMPTY`, king leaving and returning to the throne |
| **Interaction checks (spies)** | The terminal check comes before the depth cut-off (a decided node never calls the heuristic), rule functions receive the side to move |
| **Pruning-behaviour check** | The number of evaluated leaves is compared, one by one, with an independent textbook alpha-beta; this catches "correct result but worse pruning" |
| **Characterization tests** | Record the current behaviour: ties keep the first move, depth 0 behaves like depth 1, default rules are placeholders |

> **Characterization tests** are marked `CHARACTERIZATION`: they describe "how it is now", not "how it must be".
> They are **expected to change** when move ordering or the real rules are added; make sure the change is intentional.

## 4. Test case list

| ID | Type | Description |
|---|---|---|
| BB-01 | Black-box / differential | Score equals plain Minimax (2 roles x depth 1-3 x several random boards) |
| BB-02 | Black-box / property | The returned move is legal and its true value equals the reported score |
| BB-03 | Black-box / property | The caller's board is unchanged after the search |
| BB-04 | Black-box / scenario | Depth 1: White takes the heuristic maximum, Black the minimum |
| BB-05 | Black-box / scenario | White takes an immediate win; a win is recognised even at the depth limit |
| BB-06 | Black-box / scenario | Black blocks the only escape route (depth 2) |
| BB-07 | Black-box / scenario | White blocks Black's winning path; depth 1 cannot see the threat; an unstoppable threat is recognised as a loss |
| BB-08 | Black-box / equivalence | All White win / Black win / draw: correct score and still a legal move (a lost position still has to play something) |
| BB-09 | Black-box / boundary | No legal move or no pieces: the `(-1,-1)` sentinel and the worst score for that side |
| BB-10 | Black-box | Deterministic; the same object handles different boards without leaking state |
| BB-11 | Black-box | A lone king can move; each side only moves its own pieces |
| BB-12 | Black-box / boundary | The longest (8-cell) slide in all four directions, seen both at the root and at deeper nodes |
| WB-01 | White-box | Move-vector table: 32 entries, no duplicates, every rook displacement |
| WB-02 | White-box | Piece enumeration: White includes the king, row-major order; Black only black pieces; an empty board gives an empty list |
| WB-03~06 | White-box | Make/undo: plain move, leaving the throne leaves `THRONE`, target restored to its original content, captured pieces removed and restored by undo, king round trip through the throne |
| WB-07 | White-box / characterization | Default rules of the base class are placeholders (no captures) |
| WB-08 | White-box | Injected rules replace the defaults |
| WB-09 | White-box / spy | The terminal check comes before the depth cut-off; decided nodes never call the heuristic |
| WB-10 | White-box / spy | Rule functions receive the side to move |
| WB-11 | White-box | Pruning really reduces the number of leaves; equality cut-offs (`>=`, `<=`) |
| WB-12 | White-box / characterization | Ties keep the first move in enumeration order; a later, strictly better move replaces the default |
| WB-13 | White-box / characterization | Depth 0 behaves like depth 1 |
| WB-14 | White-box | The oracle's move generator agrees with the fake rule (the checker itself is checked) |
| WB-15 | White-box | Same score, move and number of evaluated leaves as an independent textbook alpha-beta |
| WB-16 | White-box | Iterative deepening with enough time equals the fixed-depth search of the last depth |
| WB-17 | White-box / fake clock | Deadline in the middle of a depth: the last completed depth is returned, the board is restored, the deadline is cleared |
| WB-18 | White-box / boundary | Depth 1 always completes, even with no time at all |
| WB-19 | White-box | A decided position (forced win/loss) is not searched deeper |
| WB-20 | White-box / fake clock | The next depth is not started when the previous one took longer than the time left |

## 5. Coverage and mutation testing

- **Coverage gate**: **100% line + branch coverage** of `cooked_tree.py`
  (`--cov-branch --cov-fail-under=100`).
- **Coverage does not mean the tests are effective**: it only proves the code was executed. So we also
  ran **mutation testing** (manually, a one-off check on 2026-11-02, not automated): 28 bugs were injected one at a
  time into the source and the tests had to fail for each of them.

  | Category | Injected bugs (examples) |
  |---|---|
  | Cut-off conditions | `>=` to `>`, `<=` to `<`, `>=` to `<=` |
  | alpha / beta updates | `max` <-> `min`, update removed, child receives a fresh window, root does not update or does not pass the window |
  | Root selection | `>` to `>=`, default move removed |
  | Check order and scores | depth check off by one, draw score, sign of win/loss |
  | Board handling | `THRONE` not kept, undo forces `EMPTY`, origin cell not restored |
  | Move generation | White without the king, one vector missing, first vector skipped, legality check removed, role not switched |

  **Result: 28 / 28 killed.** One gap was found along the way (random boards almost never contain an
  8-cell slide, so a bug dropping that vector went unnoticed); it was closed with BB-12.

## 6. How to run

```bash
uv run pytest                      # all tests
uv run pytest -m blackbox          # black-box only
uv run pytest -m whitebox          # white-box only
uv run pytest --cov=tablut.cooked_tree --cov-branch --cov-report=term-missing   # coverage report
```

The whole suite takes about 15 seconds (200 tests).

## 7. Git commit workflow

`.githooks/pre-commit` runs the tests (including the 100% coverage gate) before every `git commit` and
**aborts the commit if they fail**. Enable it once per clone:

```bash
git config core.hooksPath .githooks
```

In an emergency it can be bypassed with `git commit --no-verify` (not recommended). The hook only runs the
tests, not the linter (the project still has pre-existing `E501` errors in `game_interface.py`).

## 8. Maintenance rules

1. When the **public interface** (`get_next_movement` and the constructor parameters) is renamed, update the
   tests; private functions can be refactored freely.
2. What to expect when adding optimisations:
   - **Move ordering**: scores must not change (BB-01 must still pass); WB-12 and WB-15 will fail, which is
     expected: check the change is intended, then update them.
   - **Iterative deepening / time limit** (`get_next_movement_in_time`, WB-16..20): it calls the
     fixed-depth `get_next_movement` once per depth, so the fixed-depth behaviour must stay the same. The
     tests replace `_clock` with a hand-driven clock; never test it with real sleeps.
   - **Transposition table**: the BB-01 differential test must still pass (it is the most important safety
     net); also add a test that a cache hit gives the same result as a miss.
   - **C++ port**: compare the Python and C++ scores on the same random boards.
3. **Rules**: captures are applied by `__make_move` through the `_get_captures` hook and restored by
   `__undo_move` (WB-05). When a rule in `CookedTablut` changes, update
   `tests/cooked_tablut/test_tablut_rules.py` using the referee's Java engine as the reference.
   Repeated positions (draw) are still to be added.
4. When adding features, first check that 100% coverage still holds, then cover the new operators and
   boundaries with new tests.

## 9. Known gaps

- Repeated positions (draw) are not implemented. The heuristic only has a few tests for its scoring
  rules (perspective, support and cover checks); its playing strength is not verified.
- The rule tests are hand-written cases derived from the referee's source; there is no automated
  differential test against the Java engine.
- Mutation testing is run by hand and is not part of CI; repeat it after any large change to the search.
- The search tests use simplified rook-like fake rules; only two tests run the search with the real rules.
