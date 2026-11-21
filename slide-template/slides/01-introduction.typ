#import "@preview/typslides:1.4.0": *

#title-slide[
  Introduction
]

#slide(title: "Goal and rules", outlined: true)[
  - Tablut Challenge: build an automatic player that must move within *60 seconds*.
  - Board: 9 $times$ 9 squares, asymmetric sides.
    - *Black* (attackers) tries to capture the king.
    - *White* (defenders) wins if the king reaches an escape square.
  - A timeout counts as a loss, so the search must always return a move in time.
]

#slide(title: "Architecture")[
  #cols(columns: (1fr, 1fr, 1fr), gutter: 1em)[
    #framed(title: "Game interface")[
      Talks to the referee server and runs the move timer.
    ]
  ][
    #framed(title: "CookedTree")[
      Search: Minimax, Alpha-Beta, iterative deepening.
    ]
  ][
    #framed(title: "CookedTablut")[
      Rules, legal moves, captures and the heuristic.
    ]
  ]

  #v(1em)
  The search only uses the rules engine through a small interface, so the
  algorithm can be tested against a plain reference implementation.
]
