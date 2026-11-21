#import "@preview/typslides:1.4.0": *

#title-slide[
  Results
]

#slide(title: "Node count: plain Minimax vs Alpha-Beta")[
  Standard opening position, White to move.

  #v(0.3em)
  #table(
    columns: (auto, auto, auto, auto, auto),
    align: (center, right, right, right, center),
    inset: 6pt,
    [*Depth*], [*Plain nodes*], [*Alpha-Beta nodes*], [*Reduction*], [*Same root score*],
    [1], [56], [56], [1.0$times$], [yes],
    [2], [4,464], [273], [16.4$times$], [yes],
    [3], [252,920], [10,271], [24.6$times$], [yes],
    [4], [not run], [95,406], [--], [--],
  )
]

#slide(title: "Plain Minimax vs Alpha-Beta: growth")[
  #align(center)[
    #image("../assets/node_count.png", width: 75%)
  ]
  #v(0.3em)
  The gap grows with depth: pruning matters more as the tree gets deeper.
]

#slide(title: "Reading the results")[
  - Node counts do not depend on the machine, so they are the main comparison.
  - The root score is equal at every depth checked: pruning does not change the decision.
  - Depth 4 needs about 95 thousand Alpha-Beta nodes, roughly 18 seconds on the measurement machine.
  - Time values are indicative only and depend on the hardware.
]
