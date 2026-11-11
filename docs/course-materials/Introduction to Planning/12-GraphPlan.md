# 12-GraphPlan

Source: [12-GraphPlan.pdf](12-GraphPlan.pdf)

---

## Page 1

PLANNING BASED ON GRAPH
• In 1995 a new concept of planner based on graph has
been proposed by Blum and Furst CMU – GRAPHPLAN
• While planning it creates a graph called Planning Graph
– At each step of the search this data structure is
extended
• Graphplan inserts the TIME dimension in the plan
construction process.
• It is a correct and complete planner among the most
efficient that have been built
1

---

## Page 2

GRAPH PLAN: features
• Graphplan uses the CLOSED WORLD ASSUMPTION falling
into the category of off-line planners
• Graphplan returns either the shortest possible plan or returns an
inconsistency.
• Graphplan Inherits from linear planners the EARLY
COMMITMENT feature: ex. the action A is executed at time step
2
• Graphplan inherits from non-linear partial order planners the
ability to create partially ordered sets of actions:
• It generates parallel plans
2

---

## Page 3

GRAPH PLAN
• Actions are represented as the ones in STRIPS
– PRECONDITIONS
– ADD LIST
– DELETE LIST
• Objects have a type
• There is an action no-op that does not change the
state (frame problem)
• States are represented as sets of predicates that are
true in A given state.
3

---

## Page 4

PLANNING GRAPH
• The planning graph is a directed leveled graph
– nodes belong to different levels
– arcs connect nodes in adjacent levels.
• Level 0 corresponds to the initial state
• In the planning graph proposition levels and action
levels are interleaved and correspond to increasing
time steps
• In the planning graph interfearing actions and
propositions in a time step t can appear.
4

---

## Page 5

PLANNING GRAPH
• In a planning-graph There are different levels
– Proposition level: nodes represent propositions
– Action level: nodes represent actions
• Level 0 corresponds to the initial state and it is a
proposition level
• Arcs are divided into:
– Precondition arcs (proposition → action)
– Add arcs (action → proposition)
– Delete arcs (action → proposition)
5

---

## Page 6

PLANNING GRAPH
t = 0 t = 1 t = 2 t = 3
A
+ Add
Precond
- Delete
no-op
Precond Precond
frame Problem
In each time step an action A can be inserted if in the previous
time step all preconditions of A exist
6

---

## Page 7

PLANNING GRAPH
t = 0 t = 1 t = 2 t = 3
A
+ Add
Precond
- Delete
no-op
Precond Precond
frame Problem
There are special actions representing the “doing nothing” activity.
These actions are called no-op or frame actions
7

---

## Page 8

PLANNING GRAPH
• Each action level contains:
– all actions that are applicable at that time step
– constraints connecting pairs of actions that cannot be
performed simultaneously
• Each proposition level contains all literal that might result
from any choice of actions in the previous time step
including no-op
• NOTE: the construction process of the planning graph
does not imply ANY CHOICE on the selection of the action
that will be inserted in the plan
8

---

## Page 9

INCONSISTENCIES
During the construction of the planning graph inconsistencies are
identified, in particular
§ Two actions can be inconsistent in the same time step
§ Two propositions can be inconsistent in the same time step
In this case the action / propositions are mutually exclusive
§ They can not appear together in a plan
§ But they may appear in the same level of the planning graph
9

---

## Page 10

INCONSISTENT ACTIONS
• Inconsistent effects: one action negates the effect of
another
– The move action (part, dest) has the effect not at (part) while the no-op
action on at (part) has this effect
• Interference: an action deletes a precondition of the other
– The move action (part, dest) has the effect not at (part) while the no-op
action on at (part) has this as a precondition
• Competing needs: two actions that have mutually
exclusive preconditions.
– The load share (load means) has as a precondition not in (load means)
while the action unload (load means) has as a precondition for (load
means)
10

---

## Page 11

INCONSISTENT PROPOSITIONS
• Two propositions are inconsistent if
– one is the negation of the other
– If all the ways to reach them are mutually
exclusive
• Furthermore, there might be domain dependent
inconsistencies
– Ex: an object cannot be in two places at the same time in the
same time step.
11

---

## Page 12

PLANNING GRAPH: ALGORITHM
• The planning graph is built as follows:
– All true propositions in the initial state are inserted in the first
proposition level
CREATION of Action LEVEL
– For every operator and every way to unify its preconditions
to propositions in the previous proposition level, enter an
action node IF its preonditions are not labeled as mutually
exclusive
– In addition, for every proposition in the previous proposition
level, add a no-op operator
– Check if the action nodes do not interfere each other
otherwise mark them as mutually exclusive
12

---

## Page 13

PLANNING GRAPH: ALGORITHM
CREATION OF PROPOSITION LEVEL
– For each action node in the previous level, add propositions
in its add list through solid arcs and add dotted arcs
connected to the propositions in the delete list
– Do the same process for the no-op operators
– Mark as mutually exclusive two propositions such that all the
ways to achieve the first are incompatible with all the ways to
reach the second.
13

---

## Page 14

PLANNING GRAPH: ALGORITHM
Algorithm for the construction of the planning graph:
1. INITIALIZATION:
All true propositions in the initial state are included in the first
proposition level
2. CREATING AN ACTION LEVEL:
1. "operator "every way to unify its preconditions to not
mutually exclusive propositions in the previous level, enter
an action node
2. For every proposition in the previous proposition level,
enter a no-op operator
3. Identify the mutual exclusive relationship between the
newly constructed operators
14
14

---

## Page 15

PLANNING GRAPH: ALGORITHM
3. CREATING A PROPOSITION LEVEL:
1. For each action node in the previous action level, add the
propositions in his add list through solid arcs
2. For every "no-op" in the previous level, add the
corresponding proposition
3. For each action node in the previous action level, link
propositions in his delete list by dashed arcs
4. Identify incompatible propositions.
15
15

---

## Page 16

EXAMPLE
• We have a cart R and two loads A and B that are in
the starting position L and must be moved to the
target position P.
• Three actions (we see the syntax later)
– MOVE (R, PosA, PosB)
– LOAD (Pos, Object)
– UNLOAD (Pos, Object)
16

---

## Page 17

EXAMPLE
• MOVE(R,PosA, PosB)
– PRECONDIZIONI: at(R,PosA), div(PosA, PosB), hasFuel(R)
– ADD LIST: at(R,PosB)
– DELETE LIST: at(R,PosA), hasFuel(R)
• LOAD(Object, Pos)
– PRECONDIZIONI: at(R,Pos), at(Object,Pos)
– ADD LIST: in(R, Object)
– DELETE LIST: at(Object,Pos)
• UNLOAD(Object,Pos)
– PRECONDIZIONI: in(R, Object), at(R,Pos)
– ADD LIST: at(Object,Pos)
– DELETE LIST: in(R, Object)
17

---

## Page 18

EXAMPLE
• Objects
– Cart r
– Objects a, b
– Locations l, p
• Initial State
– at(a,l)
– at(b,l)
– at(r,l)
– hasFuel(r)
• Goal:
– at(a,p)
– at(b,p)
18

---

## Page 19

PLANNING GRAPH
• Starting from the initial state, we create an action level and a
proposition level
in (b, r)
load (b, l)
load (a, l)
move (r, l, p)
in (a, r)
at (r, p)
Inconsistencies between actions:
• For interference
load(a,l) and move(r,l,p)
load(b,l) and move(r,l,p)
load(a,l) with no-op on at(a,l)
load(b,l) with no-op on at(b,l)
move(l,r,p) with no-op on at(r,l)
move(l,r,p) with no-op on hasFuel(r)
at (a, l)
at (b, l)
at (r, l)
hasFuel (r)
at (a, l)
at (b, l)
at (r, l)
hasFuel (r)
19

---

## Page 20

PLANNING GRAPH
• Starting from the initial state, we create an action level and a
proposition level
in (b, r)
load (b, l)
load (a, l)
move (r, l, p)
in (a, r)
at (r, p)
Inconsistencies between
propositions:
in(a,r) and at(r,p)
in(b,r) and at(r,p)
in(a,r) and at(a,l)
in(b,r) and at(b,l)
at(r,p) and at(r,l)
at(r,p) and hasFuel(r)
at (a, l)
at (b, l)
at (r, l)
hasFuel (r)
at (a, l)
at (b, l)
at (r, l)
hasFuel (r)
19

---

## Page 21

PLANNING GRAPH
in (b, r)
load (b, l) load (b, l)
load (a, l)
move (r, l, p)
in (a, r)
in (b, r)
in (a, r)
load (a, l)
at (r, p)
at (r, p)
move (r, l, p)
at (a, l)
at (b, l)
at (r, l)
hasFuel (r)
at (a, l)
at (b, l)
at (r, l)
hasFuel (r)
at (a, l)
at (b, l)
at (r, l)
hasFuel (r)
in (b, r)
unload (b, p)
at (b, p)
in (a, r)
unload (a, p)
at (a, p)
at (r, p)
move (r, l, p)
at (a, l)
at (b, l)
at (r, l)
hasFuel (r)
load (b, l)
load (a, l)
19

---

## Page 22

EXTRACTION OF A VALID PLAN
• Once the planning graph is built, we have to extract a
valid-plan, i.e., a connected and consistent
subgraph of the planning graph
Features valid plan
§ Actions in the same time step can be performed in any order
(do not interfere)
§ Propositions at the same time step are not mutually exclusive
§ The last time step contains all the literals of the goal and these
are not marked as mutually exclusive
20

---

## Page 23

THEOREMS
1. 2. 3. If there is a valid plan then this is a subgraph of the planning
graph.
In a planning graph two actions are mutually exclusive in a time
step if a valid plan that contains both does not exist .
In a planning graph two propositions are mutually exclusive in a
time step if they are inconsistent, ie one of them denies the
occurrence of the other .
Important consequence:
The inconsistencies found by the algorithm prune paths in the
search tree
21

---

## Page 24

load (b, l)
load (a, l)
move (r, l, p)
at (a, l)
at (b, l)
at (r, l)
hasFuel (r)
VALID PLAN
in (b, r)
load (b, l) in (a, r)
load (a, l)
at (r, p)
move (r, l, p)
at (a, l)
at (b, l)
at (r, l)
hasFuel (r)
in (b, r)
in (a, r)
at (r, p)
at (a, l)
at (b, l)
at (r, l)
hasFuel (r)
in (b, r)
unload (b, p)
at (b, p)
in (a, r)
unload (a, p)
at (a, p)
at (r, p)
move (r, l, p)
at (a, l)
at (b, l)
at (r, l)
hasFuel (r)
load (b, l)
load (a, l)
22

---

## Page 25

ALGORITHM
function GRAPHPLAN(problem):
graph = INITIAL_GRAPH(problem)
targets = GOAL (problem)
do loop:
if objectives not mutex last step:
Sol = EXTRACT_ SOLUTION (graph, objectives)
if Sol ¹ fail: return Sol
else if LEVEL_OFF (graph): return fail
= EXPAND_GRAFO graph (graph, problem)
§ The first node contains the initial planning graph. This contains
only one time step (proposition level) with true propositions in
the initial state.
The initial graph is extracted from GRAFO_INIZIALE (problem)23

---

## Page 26

ALGORITHM
§ The goal to reach is extracted from the function
GOAL(problem)
§ If goals are not mutually exclusive in the last level, then the
planning graph could include a valid plan. The valid plan is
extracted through BACKWARD search EXTRACT_SOLUTION(graph,
objectives) that provides either a solution or a failure
§ Proceed level by level to better exploit the mutual exclusion
constraints
§ recursive method: given a set of goals at time t the algorithms
looks for a set of actions at time t-1 who have such goals as
add effects. The actions should not be mutually exclusive.
§ The search is the hybrid breadth/depth first and complete
24

---

## Page 27

ALGORITHM
§ memoization (Not a typo!)
If at some step of the search, a subset of goals is not satisfiable,
graphplan saves this result in a hash table. Whenever the same
subset of goals is selected in the future will automatically fail
25

---

## Page 28

FIRST EXAMPLE: Block World
(BlockA OBJECT)
(BlockB OBJECT)
(BlockC OBJECT)
(preconds
(On-table blockA)
(On-table blockB)
(On blockC blockA)
(Clear blockB)
(Clear blockC)
(Arm-empty))
C
A B
A
B
(effects
(On blockA blockB)
(On blockB blockC))
C
26
Place them in block_facts file

---

## Page 29

FIRST EXAMPLE: Block World
(operators
PICK-UP
(Params (<ob1> OBJECT))
(preconds
(effects
(Holding <ob1>)))
Place them in block_ops file
(Clear <ob1>) (on-table <ob1>) (arm-empty))
(operators
PUT-DOWN
(Params (<b> OBJECT))
(preconds
(Holding <b>))
(effects
(Clear <b>) (arm-empty) (on-table <b>)))
27

---

## Page 30

FIRST EXAMPLE: Block World
(operators
STACK
(Params (<b> OBJECT) (<underob> OBJECT))
(Preconds (clear <underob>) (holding <b>))
(Effects (arm-empty) (clear <b>)
(On <b> <underob>)))
(operators
UNSTACK
(Params (<b> OBJECT) (<underob> OBJECT))
(Preconds (on <b> <underob>) (clear <b>)
(Arm-empty))
(Effects (holding <b>) (clear <underob>)))
28

---

## Page 31

FAST FORWARD
Fast Forward
FF is a extremely efficient heuristic planner introduced by
Hoffmann in 2000
§ Heuristic = in each state S we compute an estimate of the distance to
the goal
Basic operation: hill climbing + A *
1. 2. 3. From a state S, examine all successors S '
If a successor state S* exists better than S, move on it and go back to point 1
If there is no state with a better evaluation, a complete A* search is run, using
the same heuristic
29
29

---

## Page 32

A* ALGORITHM: Short recap
• Instead of only considering the distance to the goal, also
consider the "cost" in reaching the node n from the root.
• We expand nodes for increasing values of f(n)
• f (n) = g (n) + h'(n)
• Where g (n) is the depth of the node, and h'(n) the
estimated distance from the goal.
• We choose the node to expand as the one for which this
sum is smaller.

---

## Page 33

A* ALGORITHM
• A * does not guarantee to find the optimal solution (it depends on the
heuristic function).
• Suppose you indicate with h(n) the true distance between the current
node and the goal.
• The heuristic function h'(n) is optimistic that if we always have
• h '(n) <= h (n).
• This heuristic function is said to be feasible.
• Theorem:
– If h '(n) <= h (n) for each node, then the A * algorithm always finds
the optimal path to the goal
• Obviously the perfect heuristic h '= h is always feasible.
• If h '= 0 we always obtain a feasible heuristic function Þ breadth-first
search

---

## Page 34

HEURISTIC FUNCTION
§ Given a problem P, a state S and a goal G, FF considers a
relaxed problem P+ that you get from P by neglecting delete
effects actions
in(t,c)
load(t,l)
load(b,l)
move(c,l,h)
in(b,c)
at(c,h)
in(t,c)
unload(t,h)
at(t,h)
in(b,c)
unload(b,h)
at(b,h)
at(c,h)
move(c,l,h)
at(b,l)
at(t,l)
at(c,l)
hasFuel(c)
at(b,l)
at(t,l)
at(c,l)
hasFuel(c)
at(b,l)
at(t,l)
at(c,l)
hasFuel(c)
load(t,l)
§ FF solves P+ with graphplan
load(b,l)
§ The number of actions in the resulting plan it is used as
30
heuristics
30

---

## Page 35

HEURISTIC FUNCTION
FF actually uses a so-called "enforced hill climbing"
function FF(problem): Return solution or fails
S = Initial_state (problem)
k = 1
do loop:
explore all states S 'at k steps
if a Better state S* is found: S = S *
else if k can be increased: k = k + 1
else perform complete A* search
§ In practice it is a complete breadth first search
§ A solution is always found, unless the current one is not a dead
end
31
31

---

## Page 36

REFERENCES
§ GRAPHPLAN
§ http://www.cs.cmu.edu/~avrim/graphplan.html
§ A. M. Blum and Furst, "Fast Planning Through Graph Analysis",
Artificial Intelligence, 90: 281-300 (1997).
§ Fast Forward
§ http://members.deri.at/~joergh/ff.html
§ J. Hoffmann, "FF: The Fast-Forward Planning System", in: AI Magazine,
Volume 22, Number 3, 2001, Pages 57-62
§ Blackbox FOR PROJECTS
§ http://www.cs.rochester.edu/u/kautz/satplan/blackbox/index.html
§ SATPLAN: http://www.cs.rochester.edu/u/kautz/satplan/index.htm
§ Henry Kautz and Bart Selman, "Planning as Satisfiability", Proceedings
ECAI-92.
§ Henry Kautz and Bart Selman, "Unifying SAT-based and Graph-based
Planning", Proc. IJCAI-99, Stockholm, 1999.
33
33