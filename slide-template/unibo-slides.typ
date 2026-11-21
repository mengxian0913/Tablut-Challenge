#import "@preview/typslides:1.4.0": *

// University of Bologna brand color.
// Approximate value: verify against the official UniBo visual identity kit.
#let unibo-red = rgb("#A6192E")

// Project configuration: applies the UniBo look to every slide.
#show: typslides.with(
  ratio: "16-9",
  theme: unibo-red,
  font: "Fira Sans",
  font-size: 20pt,
  link-style: "color",
  show-page-numbers: true,
  show-progress: true,
  back-color: white,
)

// ---------------------------------------------------------------
// Cover
// ---------------------------------------------------------------
// The logo is placed on the cover page only (scoped to this block).
#{
  set page(foreground: place(
    bottom + right,
    dx: -1.5cm,
    dy: -1cm,
    image("assets/logo_UNIBO-2018.png", width: 3.5cm),
  ))

  front-slide(
    title: "Tablut Challenge",
    subtitle: [Alpha-Beta search for an automatic Tablut player],
    authors: "Team members",
    info: [Alma Mater Studiorum -- Università di Bologna \ #datetime.today().display("[day] [month repr:long] [year]")],
  )
}

#table-of-contents()

// ---------------------------------------------------------------
// Sections: each file under slides/ owns one part of the talk.
// ---------------------------------------------------------------
#include "slides/01-introduction.typ"
#include "slides/02-algorithm.typ"
#include "slides/03-results.typ"
#include "slides/04-conclusion.typ"
