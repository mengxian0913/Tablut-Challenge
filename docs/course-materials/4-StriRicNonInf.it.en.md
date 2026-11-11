# 4-StriRicNonInf.it.en

Source: [4-StriRicNonInf.it.en.pdf](4-StriRicNonInf.it.en.pdf)

---

## Page 1

SEARCHING FOR SOLUTIONS
• Many AI problems can be solved by exploring the so called solution
space. It contains all possible sequences of actions that might be
applied by an agent. Some of these sequences lead to a solution.
– The agent examines alternative sequence of actions that lead to known
states and chooses, then, the best one.
– The process of trying this sequence is called SEARCH.
– It is useful to think about the search process like building a search tree
whose nodes are states and whose branches are operators/actions.
• A search algorithm takes as input a problem and returns a solution in
the form of a sequence of actions.
• Once the solution is found, the suggested actions can be performed.
– This is called EXECUTION.

---

## Page 2

SEARCHING FOR SOLUTIONS
Generate sequences of actions.
• Expansion: one starts from a state, and applying the operators (or
successor function) will generate new states.
• Search strategy: at each step, choose which state to expand.
• Search tree: It represents the expansion of all states starting from the
initial state (the root of the tree).
• The leaves of the tree represent either states to expand or solutions or
dead-ends

---

## Page 3

SEARCH TREES
• Basic idea:
– Off-line, simulated exploration obtained by expanding states that have
been already explored.

---

## Page 4

EXAMPLE
• A holiday in Romania; currently we are in Arad.
• Flights landing in Bucharest tomorrow
• goal:
– To be in Bucharest
• problem:
– States: Being in a city
– actions: Travel between two cities
• solution:
– Sequence locations, eg., Arad, Sibiu, Fagaras, Bucharest.

---

## Page 5

EXAMPLE

---

## Page 6

PROBLEM FORMULATION
The problem is defined by four points:
1. Initial state e.g., "at Arad"
2. Successor functions S (x) = Set of action-state pairs
– e.g., S (Arad) = {<Arad àZerind, Zerind>, ... }
• test goal, could be
– explicit, Eg., x = "At Bucharest"
– implicit, Eg., checkmap (x)
• Cost of the path e.g., distance travelled, the number of actions (hops) performed etc. c (x, a, y) ≥ 0
• A solution is a sequence of actions that lead from the
initial state to the goal.

---

## Page 7

EXAMPLE

---

## Page 8

EXAMPLE

---

## Page 9

EXAMPLE

---

## Page 10

NODE
• Each node in the search tree corresponds to a data
structure containing
• The state
• The parent node.
• The operator which has been applied to obtain the node.
• The depth of the node.
• The cost of the path from the initial state to the node

---

## Page 11

IMPLEMENTATION

---

## Page 12

SEARCH STRATEGY: EFFECTIVENESS
• Can we find a solution?
• Is it a good solution?
• minimum path solution – on-line cost
• What is the cost of the search?
• Time to find a solution - off-line cost
• Total cost = search path cost + cost of the search.
• Choosing states and actions à Importance of abstraction

---

## Page 13

EXAMPLE: THE GAME OF 8
• We have a three by three board with eight tiles and one
empty space (blank). We have to find the moves that lead
to a given position as goal
• States: position of each of the tiles;
• Operators: the blank moves to the right, left, up and down;
• Test target: description of the final state;
• Walk cost: each move costs 1.

---

## Page 14

EXAMPLE: THE GAME OF 8
Initial State
2
8 3
Goal
1 6 4
7 5
2
8 3
1 6 4
7 5
2
8 3
2
8 3
1 6
1 6 4
7 5
4
7 5
2
8
2
8 3
2
8 3
2
8 3
1 6
3
1 6 4
1 6
1 6 4
7 5
4
7 5
7 5
4
7 5
….
1
2
3
8
4
6
7 5
2
8 3
1 6 4
7 5
2
8 3
1
4
7 5
6

---

## Page 15

SEARCH STRATEGIES
• The choice on how to expand a search tree is called
strategy.
• At each node more actions may be performed (action:
operators of applications)
• STRATEGY . Two possibilities
– Non informed strategies Do not use any domain knowledge:
apply rules arbitrarily and do an exhaustive search strategy
– Impractical for some complex problems.
– Informed strategies Use domain knowledge: apply rules
following a heuristics
– If we had a perfect heuristics you do not need search

---

## Page 16

SEARCH STRATEGIES
• The Strategies are evaluated according to four criteria:
– Completeness: does the strategy guarantees to find a
solution if one exists?
– Time complexity: how long does it take to find a
solution?
– Space complexity: how much memory is needed to
carry out the search?
– Optimality: does the strategy find the best solution
when there are more solutions?

---

## Page 17

SEARCH STRATEGIES
• NON-INFORMED SEARCH STRATEGIES:
– breadth-first (at a uniform cost);
– depth-first;
– depth-first limited depth;
– iterative deepening.

---

## Page 18

THE GENERAL SEARCH STRATEGY

---

## Page 19

THE GENERAL SEARCH STRATEGY
Queuing-Fn is a function passed to append the
nodes obtained by the expansion

---

## Page 20

BREADTH-FIRST SEARCH
• Definition DEPTH:
– The depth of the root node is equal to 0;
– the depth of any other node is the depth of its parent plus 1
• Breadth-first search always EXPANDS LESS DEEP tree nodes.
• In the worst case, if depth is d and the branching factor is b then the
maximum number of nodes expanded in the worst case will be bd
.
Time and space complexity (many paths stored in memory)
– 1 + b + b2 + b3 + ... + (bd - 1) -> bd
• This strategy ensures COMPLETENESS, but we don’t have
EFFICIENT IMPLEMENTATIONS on single-processor systems (multi-
processor architectures).

---

## Page 21

BREADTH-FIRST SEARCH
The main disadvantage is the excessive memory
footprint. The example assumes that the branching factor is
b = 10. It expands 1000 nodes/ second. Each node uses 100
bytes of memory.

---

## Page 22

BREADTH-FIRST SEARCH
• The problem of memory seems to be the most serious.
• Breadth-first search always finds the min-cost path if the cost equals
the depth (otherwise we should use another strategy that always
expands the least cost node à uniform cost strategy).
• The uniform-cost strategy is comprehensive and, unlike the breadth-
first search, ideal when operators have not uniform costs. (Same
temporal and spatial complexity as breadth-first search).

---

## Page 23

BREADTH-FIRST SEARCH
• Expands The nodes at lower depths
• Implementation:
– fringe is a FIFO queue, i.e successors at bottom.

---

## Page 24

BREADTH-FIRST SEARCH
• Expands The nodes at lower depths
• Implementation:
– fringe is a FIFO queue, i.e successors at bottom

---

## Page 25

BREADTH-FIRST SEARCH
• Expands The nodes at lower depths
• Implementation:
– fringe is a FIFO queue, i.e successors at bottom

---

## Page 26

BREADTH-FIRST SEARCH
• Expands The nodes at lower depths
• Implementation:
– fringe is a FIFO queue, i.e successors at bottom

---

## Page 27

BREADTH-FIRST SEARCH
QueueingFn = Add the successors to the end of
the queue

---

## Page 28

b- Maximum of the search tree branching
d- depth of the least-cost solution
m- maximum depth of the state space (may be
infinite)

---

## Page 29

UNIFORM-COST SEARCH
Each node is labelled with a cost g(n)
QueueingFn = Enter the successors in order of
increasing path cost

---

## Page 30

DEPTH FIRST SEARCH
• Depth-first EXPANDS deepest nodes first;
• Nodes at equal depth are ARBITRARILY selected (leftmost).
• Depth-first search requires a modest memory occupation
• For a state space with branching factor b and maximum search depth
d we have to store b * d nodes.
• The temporal complexity is rather similar to that of breadth-first
search.
• In the worst case, if the maximum depth is d and the branching factor
is b the maximum number of nodes expanded is bd. (Time
complexity).

---

## Page 31

DEPTH FIRST SEARCH
• Depth-first search is EFFICIENT from an implementation point of view:
one path at a time is stored (a single stack)
• Depth-first search can be NON-COMPLETE with possible loops in the
presence of infinite branches.

---

## Page 32

DEPTH FIRST SEARCH
• Expands The deeper nodes first
• Implementation:
– fringe = LIFO stack

---

## Page 33

DEPTH FIRST SEARCH
• Expands The deeper nodes first
• Implementation:
– fringe = LIFO stack

---

## Page 34

DEPTH FIRST SEARCH
• Expands The deeper nodes first
• Implementation:
– fringe = LIFO stack

---

## Page 35

DEPTH FIRST SEARCH
• Expands The deeper nodes first
• Implementation:
– fringe = LIFO stack

---

## Page 36

DEPTH FIRST SEARCH
• Expands The deeper nodes first
• Implementation:
– fringe = LIFO stack

---

## Page 37

DEPTH FIRST SEARCH
• Expands The deeper nodes first
• Implementation:
– fringe = LIFO stack

---

## Page 38

DEPTH FIRST SEARCH
• Expands The deeper nodes first
• Implementation:
– fringe = LIFO stack

---

## Page 39

DEPTH FIRST SEARCH
• Expands The deeper nodes first
• Implementation:
– fringe = LIFO stack

---

## Page 40

DEPTH FIRST SEARCH
• Expands The deeper nodes first
• Implementation:
– fringe = LIFO stack

---

## Page 41

DEPTH FIRST SEARCH
• Expands The deeper nodes first
• Implementation:
– fringe = LIFO stack

---

## Page 42

DEPTH FIRST SEARCH
• Expands The deeper nodes first
• Implementation:
– fringe = LIFO stack

---

## Page 43

DEPTH FIRST SEARCH

---

## Page 44

DEPTH FIRST SEARCH
QueueingFn = Enter the successors to the top of the stack.
It is assumed that the nodes of depth 3 does not have
successors

---

## Page 45

b- Maximum of the search tree branching
d- depth of the least-cost solution
m- maximum depth of the state space (may be infinite)

---

## Page 46

EXAMPLE: DEPTH-FIRST
n0
n1 n2 n3 n4
n11 n12 n13 n21
goal
n22 n31 n32 n33 n41 n42
• Depth-first: nodes expanded added at the head of L
– n0
– n1, n2, n3, n4
– n11, n12, n13, n2, n3, n4
– n11, n12, n13, n2, n3, n4
– n12, n13, n2, n3, n4
– n13, n2, n3, n4
– n2, n3, n4
– n21, n22, n3, n4 Success

---

## Page 47

EXAMPLE: BREADTH-FIRST
n0
n1 n2 n3 n4
n11 n12 n13 n21
goal
n22 n31 n32 n33 n41 n42
§ Breadth-first: nodes expanded appended to L.
– n0
– n1, n2, n3, n4
– n2, n3, n4, n11, n12, n13
– n3, n4, n11, n12, n13, n21, n22
– n4, n11, n12, n13, n21, n22, n31, n32, n33
– n11, n12, n13, n21, n22, n31, n32, n33, n41, n42
– n12, n13, n21, n22, n31, n32, n33, n41, n42
– n13, n21, n22, n31, n32, n33, n41, n42
– n21, N22, n31, n32, n33, n41, n42 Success

---

## Page 48

LIMITED DEPTH SEARCH
• It is a depth-first variant
• It includes a MAXIMUM DEPTH parameter
• When you reach the maximum depth or a failure, it explores
alternative paths (if they exist), then alternative paths at less than
one unit of depth, and so forth (backtracking).
• You may establish a maximum limit of depth (it does not necessarily
solve the problem of completeness).
• Avoids infinite branches

---

## Page 49

LIMITED DEPTH SEARCH
The nodes at depths l have no successors.
• Recursive Implementation:

---

## Page 50

ITERATIVE DEEPENING
• Iterative deepening search avoids the problem of choosing the
maximum depth limit by trying all possible depth limits.
– Start with 0, then 1, then 2 etc ...
• It combines the advantages of depth and breadth-first strategies. It is
complete and explores a single branch at a time.
• Many states are expanded multiple times, but this does not worsen
considerably the execution time.
• In particular, the total number of expansions is: (d+1)1 + (d)b + (d-1)b2
+…+ 3bd-2 + 2bd-1 +bd
.
• In general it is the favourite search strategy when the search space is
very large.

---

## Page 51

ITERATIVE DEEPENING
• It can emulate the breadth-first search through repeated applications
of the depth first search with an increasing depth limit.
1. C = 1
2. 3. Apply depth-first with depth limit of C, if you find a solution stop
Otherwise, increase C and go to step 2

---

## Page 52

ITERATIVE DEEPENING SEARCH

---

## Page 53

ITERATIVE DEEPENING SEARCH L = 0

---

## Page 54

ITERATIVE DEEPENING SEARCH L = 1

---

## Page 55

ITERATIVE DEEPENING SEARCH L = 2

---

## Page 56

ITERATIVE DEEPENING SEARCH L = 3

---

## Page 57

ITERATIVE DEEPENING SEARCH

---

## Page 58

b- Maximum of the search tree branching
d- depth of the least-cost solution
m- maximum depth of the state space (may be infinite)

---

## Page 59

Comparison of search strategies
b = branching factor; d = profondià of the solution; m = maximum depth
of the search tree; l = depth limit.