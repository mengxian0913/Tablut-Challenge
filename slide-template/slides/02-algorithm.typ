#import "@preview/typslides:1.4.0": *

#title-slide[
  Search algorithm
]

#slide(title: "Move generation")[
  - Every piece moves along a row or column: 4 directions $times$ 8 distances, so *32 candidate vectors*.
  - A move is legal only if the path is free and the throne and camp rules allow it.
  - The board is changed in place: each move is applied, searched, then undone.

  #v(0.5em)
  #set text(size: 15pt)
  ```python
  for from_node in alive_chess:
      for mv_row, mv_col in zip(self.move_row, self.move_col, strict=True):
          next_node = Node(from_node.row + mv_row, from_node.col + mv_col)
          if not self._is_valid_movement(chess_board, from_node, next_node):
              continue
  ```
]

#slide(title: "Minimax with Alpha-Beta")[
  - Minimax: White maximises the score, Black minimises it.
  - Alpha-Beta keeps a window $[alpha, beta]$ and stops a branch as soon as it cannot change the result.
  - The root score is the same as plain Minimax; only fewer nodes are visited.

  #v(0.5em)
  #set text(size: 15pt)
  ```python
  if role == ROLE.WHITE:
      best = max(best, score)
      alpha = max(alpha, best)
      if best >= beta:
          return best          # Black will never allow this line
  else:
      best = min(best, score)
      beta = min(beta, best)
      if best <= alpha:
          return best          # White already has a better option
  ```
]

#slide(title: "Iterative deepening under a time limit")[
  - Search depth 1, then 2, then 3, and so on.
  - A new depth starts only if the time left is likely enough for it.
  - If the deadline is hit in the middle of a depth, the board is restored and the last complete depth is used.
  - The budget is the remaining time minus a *3-second* safety margin.

  #v(0.5em)
  #set text(size: 15pt)
  ```python
  if self.__deadline is not None and self._clock() >= self.__deadline:
      raise SearchTimeout
  ```
]

#slide(title: "Evaluation function")[
  Score = White evaluation $-$ Black evaluation (higher is better for White).

  #cols(columns: (1fr, 1fr), gutter: 2em)[
    - *King on an open line* to an escape square: $+5$ for each one.
    - *Pressure*: each adjacent enemy counts, at most two.
  ][
    - *Single enemy*: a friendly piece right behind it changes the score by $3$.
    - The weights are hand-chosen, not tuned automatically.
  ]
]

#slide(title: "Complexity")[
  Let $b$ be the branching factor and $d$ the depth.

  - Plain Minimax visits $O(b^d)$ nodes.
  - Alpha-Beta with perfect move ordering visits about $O(b^(d/2))$ nodes.
  - Our move ordering is the generation order, so the gain is smaller than the best case.
  - The results on the next slides measure the real gain.
]
