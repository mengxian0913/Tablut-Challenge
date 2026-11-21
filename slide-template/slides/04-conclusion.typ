#import "@preview/typslides:1.4.0": *

#title-slide[
  Conclusion
]

#slide(title: "Limitations and future work", outlined: true)[
  - *No move ordering*: searching the best moves first would prune more.
  - *No transposition table*: repeated positions are searched again.
  - *Draw by repetition* is not handled by the rules engine.
  - *Heuristic not tuned*: the weights were set by hand.
  - Possible next step: move ordering, then automatic tuning of the heuristic.
]

#focus-slide[
  Thank you!
]
