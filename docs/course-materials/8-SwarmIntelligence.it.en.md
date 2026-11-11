# 8-SwarmIntelligence.it.en

Source: [8-SwarmIntelligence.it.en.pdf](8-SwarmIntelligence.it.en.pdf)

---

## Page 1

SWARM INTELLIGENCE
• Swarm intelligence (SI) is an artificial intelligence technique
based around the study of collective behavior in decentralized,
self-organized systems.
• SI systems are typically made up of a population of simple
agents interacting locally with one another and with their
environment. Although there is normally no centralized control
structure dictating how individual agents should behave, local
interactions between such agents often lead to the emergence
of global behavior. Examples of systems like this can be found
in nature, including ant colonies, bird flocking, animal herding,
bacteria molding and fish schooling (from Wikipedia).
1

---

## Page 2

MIND IS SOCIAL
• Human Intelligence is the result of social interaction
• Evaluate, compare and imitate other individuals, learn from
experience emulating the successful behavior of others, enables
people to adapt to complex environments and situations through the
discovery of optimal patterns, beliefs and behaviors (Kennedy &
Eberhart, 2001).
• Culture and cognition are consequences of human social
choices
• Culture emerges when individuals become similar through a process
of social learning
• To model human intelligence there is need to model individuals in a
social context.
2

---

## Page 3

FEATURES OF A SI SYSTEM
• A set of simple individuals with limited capacities
• Individuals are not aware of the system in its global view
• Local communication patterns (direct or indirect - stigmergic)
• Distributed computation: no centralized coordination of individual
activities
• Robustness
• Adaptivity
• NATURAL METAPHORS
– Ant colonies
– Bee colonies
– Fish shoals
– Bird flocks
3

---

## Page 4

SELF-ORGANISATION
• Ingredients:
– Multiple interactions among agents
• Simple agents (es. rule based)
• Multi-agent systems
– Positive Feedback
• Reinforcement of common behaviours
• Amplification di random fluctuations and structure formation
– Negative Feedback
• Saturation
• Competition
• Exhaust resources
4

---

## Page 5

STIGMERGY
• Stigmergy is a form of indirect communication
• An agent modifies the environment and the other react to this chance
– Example: ants communicate through pheromone
5

---

## Page 6

SWARM INTELLIGENCE ALGORITHMS
• Many algorithms exist based on the swarm intelligent concept
• Ant Colony Optimization ACO (Dorigo, 1992)
– Algorithm based on the behaviour of ants. Positive feedback based on
pheromone trails. Positive feedback based on pheromon trails that
reinforce components that contribute to the problem solution
• Artificial Bee Colony Algorithm (Karaboga in 2005)
– Algorithm based on the behaviour of bees. Population of bees that look
for nectar.
• Particle Swarm Optimization PSO (Kennedy, Eberhart 1995)
– Algorithm based on the observation of bird flocks or fish shouls.
Stigmergy as communication and imitation of neighborhoods.
6

---

## Page 7

ANT COLONY
• From the observation of the ants we discover that:
• Ants deposit pheromone trails while walking from the nest to the
food and vice versa
• Ants tend to choose (more likely) the paths marked with higher
pheromone concentrations.
• Cooperative interaction leads to the emergent behavior to find the
shortest path
7

---

## Page 8

ANT BEHAVIOUR
8

---

## Page 9

DOUBLE BRIDGE
9

---

## Page 10

ANT COLONY OPTIMIZATION
• Probabilistic parametrized model – the pheromone model – used to
model pheromon trails
• Ants build solution components in an incremental way.
• Stochastic steps on a fully connected graph called construction graph:
G = (C,L).
– Vertexes C are solution components
– Arcs L are connections
– States are paths on G
• Constraints can be represented to define what is a consistent solution
10

---

## Page 11

EXAMPLE: TSP
11

---

## Page 12

EXAMPLE: TSP
• A TSP model in ACO
– Nodes of G (solution components) are cities to be visited;
– Arcs are connections between cities
– A solution is an Hamiltonian path in the graph
– Constraints are used to avoid sub-cycles: each ant can visit a city once.
12

---

## Page 13

INFORMATION SOURCES
• Connections, solution components or both have the following
associated information:
– Pheromone t
– Heuristic value h
• The pheromone value abstracts natural pheromone trails and codes
the long term memory of the global search process.
• The heuristic value represents the prior background knowledge on the
problem.
13

---

## Page 14

BASIC SCHEMA
14

---

## Page 15

ACO SYSTEM
• First example of Ant Colony Optimization
• Ants build a solution following a path on the construction graph.
• A transition rule is followed to choose the next node to visit.
• The heuristics and the pheromone are used.
• Pheromone values are updated on the basis of the QUALITY OF THE
SOLUTION FOUND by the ants.
15

---

## Page 16

ANT-SYSTEM ALGORITHM
InitializePheromoneValues()
while termination conditions not met do
for all ants a Î A do
sa ¬ConstructSolution(t ,h )
end for
ApplyOnlineDelayedPheromoneUpdate()
end while
16

---

## Page 17

ANT-SYSTEM
• Memory is used to remind past paths
• Starting from node i, we have to probabilistically chose the next
consistent node to visit
• The probabilistic choice depends on
pheromone trail tij
heuristics hij = 1/dij
a and b weight the importance of the
pheromone and the heuristics
a b
[tij] [hij] if j consistent
a b
Sk feasible [tij] [hij]
pij=
0 otherwise
17

---

## Page 18

ANT SYSTEM
• The pheromone is updated with the following rule
m
k
• t ← (1 - ρ) t + S Dt (ρ: evaporation coefficient)
ij
ij k=1
ij
1/L if ant k used arc (i,j)
k
• Dt =
ij
0 otherwise
• L k
: length of the path followed by ant k
18

---

## Page 19

ALGORITHM
while termination conditions not met do
ScheduleActivities
AntBasedSolutionConstruction()
PheromoneUpdate()
DaemonActions() {optional}
end ScheduleActivities
end while
19

---

## Page 20

ALGORITHM STEPS
• AntBasedSolutionConstruction()
– Ants move by applying a stochastic local decision policy that uses values
of pheromone and heuristic on graph components.
– While moving, ants take track of the partial solutions (paths) that have
been built
• PheromoneUpdate()
• Ants update the pheromone during the solution construction (online
step-by-step pheromone update).
• Ants can update backward the pheromone on components used on
the basis of the quality of the overall solution (online delayed
pheromone update).
• Evaporation is applied all time.
20

---

## Page 21

ALGORITHM STEPS
• DemonActions()
– Are “centralised” actions that cannot be executed by the single ants:
– local search procedure applied to each solution built
– Collection of global information to decide whether to leave additional
pheromone to guide search from a global perspective
21

---

## Page 22

ACO - SYSTEM
• Papers on the course web-site
– MAX-MIN Ant System
– Hyper-cube Framework
– Multi-level ACO
– Beam ACO
• EU Project: SWARM-BOT, SWARMANOID
• http://www.swarm-bots.org/
• Video youtube
• http://www.youtube.com/watch?v=seGqyO32pv4m/watch?v=3YDkbltz
MmA
22

---

## Page 23

HONEY BEE-COLONY
• Artificial Bee Colony Algorithm: ABC Algorithm
• Artificial bees of three types:
– employed bees that are associated with a specific nectar source,
– onlookers that observing the employed bees chose a nectar source and
– scouts that discover new food sources
• Initially, food sources are discovered by scout bees. Then food is
consumed and the source exhausted. The employed bees in that
source become scout.
• Food position: solution (we have as many solutions as employed
bees)
• Food quantity: fitness
23

---

## Page 24

ABC ALGORITHM
InitializationPhase()
repeat
EmployedBeePhase()
OnlookerBeePhase()
ScoutBeePhase()
Sol=BestSolutionSoFar
Until (Cycle=MaxCycleNum or MaxCPUtime)
24

---

## Page 25

ABC ALGORITHM
InitializationPhase()
• A set of food source positions are randomly selected by the bees and
their nectar amounts are determined.
• Each solution Xm (m=1..Npopol.) is composed of n variables Xmi
(i=1..n). Each variable is subject to a lower and upper bound and
initialized to
Xmi = lbi + rand(0,1) (ubi- lbi )
25

---

## Page 26

ABC ALGORITHM
EmployedBeePhase()
• After sharing the information about the nectar amount, every
employed bee goes to the food source area visited by herself at the
previous cycle since that food source exists in her memory, and then
chooses a new food source by means of visual information in the
neighbourhood of the present one.
• Fitness function of Xm : we use the objective function of the problem
to compute the fitness as follows
1/(1+obj(Xm)) se obj(Xm) ³ 0
ftn(Xm) =
1+|obj(Xm)| se obj(Xm) < 0
26

---

## Page 27

ABC ALGORITHM
OnlookerBeePhase()
• An onlooker bee chooses a food source depending on the probability
value associated with that food source
pm =
ftn(Xm)
Npopol.
S ftn(Xi)
i=1
Positive feedback
27

---

## Page 28

ABC ALGORITHM
ScoutPhase()
• Scouts chose nectar sources random.
• The employed bees that cannot improve the solution after a given
number of attempts become scout and abandon the food source.
• Negative feedback
28

---

## Page 29

ABC APPLICATIONS
• Training neural network: optimization function that represents the
mean squared error
• Karaboga D. Basturk B. Ozturk C. (2007) Artificial bee colony (ABC) optimization
algorithm for training feed-forward neural network, Modeling Decisions for Artificial
Intelligence, LNCS 4617. 318-319.
• Numerical Optimization
• http://chern.ie.nthu.edu.tw/gen/4a-Karaboga-tr06_2005-original.pdf
• Combinatorial Optimization
• Karaboga D. Basturk B. (2007) Artificial bee colony (ABC) optimization algorithm for
solving constrained optimization problems, Advances in Soft Computing, LNCS 4529.
789-798.
29

---

## Page 30

PARTICLE SWARM OPTIMIZATION
• Particle Swarm Optimization PSO has been proposed in1995 by:
– A psyco-social scientist James Kennedy
– An electrical engineer Russel Eberart
• The research activity starts from the analysis of interaction
mechanisms between individuals that compose the swarm
• Particularly interesting when the whole swarm has a common goal
such as food search
30

---

## Page 31

PARTICLE SWARM OPTIMIZATION
• The observation of rules that guide the bird flock moves show that
each individual entity has three driving trends
– Follow neighbours
– Stay in the flock
– Avoid collisions
• With these rules it is possible to describe and model the collective
move of a flock with NO COMMON OBJECTIVE
• PSO adds a common objective: food search
31

---

## Page 32

PARTICLE SWARM OPTIMIZATION
• With a common objective, a single individuals that finds a food source
has two alternatives:
– Move away from the group to reach the food (individualistic choice)
– Stay in the group (social choice)
• If more than one individual entity moves toward the food other flock
members do the same
• Gradually the whole group changes direction toward promising areas.
The information propagates to all members.
32

---

## Page 33

PARTICLE SWARM OPTIMIZATION
• With PSO we can solve optimization problems with the following
analogy:
– individuals: tentative configurations that move and sample the solution N-
dimensional space.
– Social interaction: each individual agent takes advantage from other
searches moving toward promising regions (best solution globally found)
• Search strategy can be found as a balance between exploration and
exploitation:
– Exploration: individual agents that search for a solution
– Exploitation: social behaviour which is the exploitation of other individual
successful behaviour
33

---

## Page 34

NEIGHBORHOOD
• A feature that appears to be important is the concept of proximity
– individuals are affected by the actions of other individuals that are closer
to them (sub-groups)
– individuals are part of more sub-groups, and then the spread of
information is globally guaranteed
• Sub-groups are not tied to the physical proximity of the configurations
in the parameter space but are a priori defined and may take into
account also considerable shifts between individuals
34

---

## Page 35

ALGORITHM
• PSO optimizes a problem by setting a population (Swarm) of
candidate solutions (particles).
• PSO moves these particles in the search space through simple
mathematical formulas.
• The movement of particles is guided by the best position found so far
in search space (from individual to population) and it is updated when
better solutions are discovered
• f: ℝn → ℝ fitness or cost function to minimize: it takes a solution
(vector) and produces a fitness value. The gradient of f is not known.
• Goal:find solution a such that f(a) ≤ f(b) for all b in the search space
35

---

## Page 36

ALGORITHM
• S number of particles in population.
• Each particle has
– a position xi ∈ ℝn in the search space
– a speed vi ∈ ℝn
.
• pi is the best solution found so far by particle i
• g is the best solution found so far by the entire swarm.
• For each particle i = 1, ..., S do:
– Initialize the particle's position with a uniformly distributed random vector:
xi~ U(blo, bup), where blo and bup are the lower and upper boundaries of
the search-space.
– Initialize the particle's best known position to its initial position: pi ← xi
– If (f(pi) < f(g)) update the swarm's best known position: g ← pi
– Initialize the particle's velocity: vi~ U(-|bup-blo|, |bup-blo|)
36

---

## Page 37

ALGORITHM
• Until a termination criterion is met (e.g. number of iterations
performed, or adequate fitness reached), repeat:
– For each particle i = 1, ..., S do:
• Pick random numbers: rp, rg ~ U(0,1)
• Update the particle's velocity: vi ← ω vi + φp rp (pi-xi) + φg rg (g-xi)
• Update the particle's position: xi ← xi + vi
• If (f(xi) < f(pi)) do:
• Update the particle's best known position: pi ← xi
• If (f(pi) < f(g)) update the swarm's best known position:
g ← pi
• Return g : best found solution.
• Parameters ω, φp, is φg should be carefully selected as they strongly
influence the effectiveness and the efficiency of the PSO method.
37

---

## Page 38

ROBOT BASED ON PSO
• Article where PSO is introduced
• Kennedy, J .; Eberhart, R. (1995). "Particle Swarm Optimization".
Proceedings of the IEEE International Conference on Neural
Networks. IV. pp. 1942-1948..
• movie robots
• http://www.youtube.com/watch?v=RLIA1EKfSys
• Source in movement
• http://www.youtube.com/watch?v=nul8nYIQ8ug&feature=related
38

---

## Page 39

PARAMETER TUNING
• These algorithms are very simple but require an accurate parameter
tuning activity
• Tedious and error prone operation. It is hard to find the optimal
parameter configuration
• Techniques for automatic parameter tuning
– ParamILS http://www.cs.ubc.ca/labs/beta/Projects/ParamILS/
– Available on line
39