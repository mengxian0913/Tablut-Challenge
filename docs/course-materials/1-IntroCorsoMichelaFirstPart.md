# 1-IntroCorsoMichelaFirstPart

Source: [1-IntroCorsoMichelaFirstPart.pdf](1-IntroCorsoMichelaFirstPart.pdf)

---

## Page 1

Foundations of Artificial Intelligence
Michela Milano
Dipartimento di Informatica – Scienza e Ingegneria
Università di Bologna
michela.milano@unibo.it
For internal didactic use
1

---

## Page 2

What is intelligence?
Intelligence has been defined in many ways, including: the
capacity for logic, understanding, self-awareness, learning,
emotional knowledge, reasoning, planning, creativity, critical
thinking and problem solving. More generally, it can be described
as the ability to perceive or infer information, and to retain it as
knowledge to be applied towards adaptive behaviors within an
environment or context.
From Wikipedia
2

---

## Page 3

Turing: Can machine think?
Computing Machinery and Intelligence (1950)
• Problem of defining a universal
machine and defining thinking
(ambiguous)
• Imitation game
• Three actors: a human, a
computer, a interrogator in a
different room. The interrogator
should classify the human and the
machine.
• Is it possible that a computer can
mislead the interrogator and be
classified as a human?
• Various objections to this test
3

---

## Page 4

Turing test and AI
• Computers should have the following abilities
– Natural language processing
– Knowledge representation
– Automatic reasoning
– Machine learning
• Beyond Turing test – Physical interactions: Robotics, Artificial Vision,
Speech, Movement, etc.
• In 2014, a chatbot ( Eugene Goostman), mimiking the answer of a 13
years old boy, has succeeded the test.
• Cleverbot (Machine Intelligence Prize 2010), SIRI (Apple), Cortana
(Microsoft), Alexa (Amazon) and ChatGPT (OpenAI)
• Often built indexing previous conversations. What is missing is
coherence (hallucinations), state of dialogue, semantics.
• Methodological perspective: engineering approach fostering emulation
more than achievement of real intelligence in limited domains.
4

---

## Page 5

Beyond Turing test
Mathematical puzzles: Require deep language
understanding, common-sense, reasoning capabilities, multi-
modal analysis.
Geometrical problems solving - Allen Institute
Example: Using integer numbers from 2 to 7, fill in the free
tiles such that the sum of the three numbers around the
black circle is 11.
5

---

## Page 6

Turing forecast: true or false?
• “I believe that in about fifty years' time it will be possible to
programme computers, with a storage capacity of about
109
, to make them play the imitation game so well that an
average interrogator will not have more than 70% chance
of making the right identification after five minutes of
questioning. … I believe that at the end of the century the
use of words and general educated opinion will have
altered so much that one will be able to speak of
machines thinking without expecting to be contradicted.
”
From: A. Turing," A Computing machinery and intelligence", Mind, vol.
59, n. 236, pp. 433-460, 1950.
6

---

## Page 7

AI Systems Classification
Weak vs Strong AI
Weak AI: research question Is it possible to build sytems that act as
if they were intelligent?
Strong AI: research question Is it possible to build sytems that are
intelligent? That have conscious minds, wills and sentiments?
General AI vs Narrow AI
General AI refers to systems which are able to cope with any
generalised task which is asked of it, much like a human.
Narrow AI refers to AI which is able to handle just one particular task.
AI systems display a certain degree of intelligence in a particular field,
but it remain computer systems that perform highly specialised tasks
for humans, within that narrow field.
7

---

## Page 8

Artificial Intelligence
• Born in 1956. (Minsky, McCarthy, Shannon, Newell, Simon).
• The study is to proceed on the basis of the conjecture that every
aspect of learning or any other feature of intelligence can in principle
be so precisely described that a machine can be made to simulate it.
”
[McCarthy 1955].
• Which definition of intelligence? Which definition of Artificial
Intelligence?
• Some definitions:
– Study of how to make computers do things that humans do better.
• Transitory definition (see chess)
– Study of how to build computers that pass the Turing test
(reasoning, natural language understanding, learning). If situated in
an environment also perception, vision, movement, robotics
– Other definitions of AI do not link directly to human intelligence but rather
on the ability of interacting with and adapting to an environment.
8

---

## Page 9

Short history
• 1943-1956 The birth of AI
– Neural networks, chess programs, theorem provers;
• 1952-1969 Initial enthusiasm and big expectations
– General Problem Solver, LISP language, neural networks.
• 1966-1974 Down to earth
– Some programs were not adequate (ELIZA, syntactic translations, neural networkks), other
were too computationally expensive (combinatorial explosion).
• 1969-1979 knowledge based systems
– Deep knowledge in a limited domain. Expert systems.
• 1980-1988 AI enters in industry
– Commercial successful expert system. Fifth generation project in Japan. Companies working in
AI, research funds
• 1988-2010 Web and internet era
– Decision support systems, robotic agents, natural language
• 2010-today Machine learning and deep learning
– Big data and massive computing power have enabled deep networks to work properly.
Augmented intelligence and perception. Industrial interest, industry 4.0
• 2020-today Generative AI and Conversational Agents
9

---

## Page 10

Two main AI approaches
• Top-down or symbolic AI:
– Symbolic representation of knowledge
– Logics, ontologies, rule based systems, declarative architecture.
– Human understandable models
• Bottom up, or connessionist approach.
– Neural networks. Knowledge is not symbolic and it is “encoded”
into connections between neurons.
– Concepts are learned by examples
– Non understandable by humans
10

---

## Page 11

Reasoning and Logic
• Deductive reasoning (Aristotelian syllogism - deductive logic):
• From: All men are mortal and Socrates is a man then: Socrates is mortal
• Okay, but it does not allow us to "learn" new knowledge.
• Inductive Reasoning (Learning, reverse deduction)
• From the observation that several birds flying then All the birds fly (And penguins?).
• Production of new knowledge at the expense of correctness.
• Hypothetical or abductive reasoning (Dual of deductive):
• From the observation of Death of Socrates and knowing that All men are mortal
hypothesizes that Socrates is a man. (And if he were a cat?).
• It dates back to the causes through observation of the effects at the expense of
correctness.
• Reasoning by analogy (Metaphorical, case-based)
• It does not require a model or a lot of data, but it uses the principle of similarity.
Socrates and John "resemble" is Socrates loves philosophy then: John loves
philosophy.
• K-Nearest-Neighbor and Support Vector Machine (SVM).
• Constraint reasoning and optimization Using constraints, probability, statistics (Bayes
theorem)
11

---

## Page 12

Logic, automatic proof and Prolog
not interpreted
symbols
First order predicate
logic
Interpretation
Correctness
Syntax Semantics
Theorem provers Concept of logical
consequence
Completeness
axiomatic deductive
theories
Resolution (General
clauses)
Programming Logic and
Prolog (Declarative -
defined clauses)
Automated theorem proving
Most systems in AI using logic for automated
theorem proving are based on deduction and,
in particular, on the resolution method
defined by A Robinson in 1965.
12

---

## Page 13

Different algorithm interpretations
• Algorithm = data structures and instructions
• Algorithm = logic (knowledge) + control (engine
inference)
• Algorithm = examples (experience) + Machine learning
Level of generality and "intelligence” increases
13

---

## Page 14

Declarative languages and Prolog
Algorithm = Logic + CONTROL
• Problem knowledge is independent from its use
• It expresses WHAT and not HOW
• High modularity and flexibility
• Design scheme at the base of most KNOLWEDGE BASED
SYSTEMS (Expert Systems)
• LOGIC: knowledge about the problem determines correctness and
efficiency
• CONTROL: solution strategy determines the efficiency
PROLOG: PROgramming in LOGic
• It is the best known Logic Programming language. It is built on the
ideas by R. Kowalski and the first realization by A. Colmareur
(1973).
14

---

## Page 15

Prolog Program
– A PROLOG PROGRAM is a set of Horn clauses representing:
• FACTS about the object under examination and the relationships
• RULES on objects and relationships (IF ... ..THEN)
• GOAL (clauses with no head), on the basis of definite knowledge
– EXAMPLE: two individuals are colleagues if they work for the same
company
Head Body
colleague(X,Y):- works(X,Z), works(Y,Z), different(X,Y).
works(emp1,ibm).
works(emp2,ibm).
works(emp3,txt).
works(emp4,olivetti).
works(emp5,txt).
FACTS
:- colleague(X,Y).
GOAL
RULE
15

---

## Page 16

Prolog Program
– Sum of two integer numbers. Declarative definition
sum(0,X,X).
FACT
sum(s(X),Y,s(Z)):- sum(X,Y,Z).
RULE
– sum is a non interpreted symbol
– Integer numbers defined with the successor structure s(X)
– Recursive definition
– Many possible queries (algorithms)
:- sum(s(0),s(s(0)),Y).
:- sum(s(0),Y,s(s(s(0)))).
:- sum(X,Y,s(s(s(0)))).
:- sum(X,Y,Z).
:- sum(X,Y,s(s(s(0)))), sum(X,s(0),Y).
16

---

## Page 17

Deduction and induction in logic
programming
T
B
E (deduction)
parent(X,Y) :- mother(X,Y).
parent(X,Y) :- father(X,Y).
!
mother(mary,vinni).
mother(mary,andre).
father(carrey,vinni).
father(carry,andre).
®
parent(mary,vinni).
parent(mary,andre).
parent(carrey,vinni).
parent(carrey,andre).
E+
parent(mary,vinni).
parent(mary,andre).
parent(carrey,vinni).
parent(carrey,andre).
B T (induction)
!
mother(mary,vinni).
mother(mary,andre).
father(carrey,vinni).
father(carry,andre).
®
parent(X,Y) :- mother(X,Y).
parent(X,Y) :- father(X,Y).
parent(mary,carrey).
E-
"e+ Î E+: BÈT |= e+ (T is complete)
"e- Î E-
: BÈT |= e- (T is consistent)
17

---

## Page 18

Abduction in logic programming
T
E
parent(X,Y) :- mother(X,Y).
parent(X,Y) :- father(X,Y).
parent(mary,vinni).
parent(mary,andre).
! ®
parent(carrey,vinni).
parent(carrey,andre).
B (abduction)
mother(mary,vinni) Ú father(mary, vinni).
mother(mary,andre) Ú father(mary,andre).
mother(carrey,vinni) Ú father(carrey,vinni).
mother(carey,andre) Ú father(carry,andre).
TÈB |= E
Often we use integrity constraints to control hypothesis
T
E
B (abduction)
parent(X,Y) :- mother(X,Y).
parent(X,Y) :- father(X,Y). mother(X,Y) → female(X).
father(X,Y) → male(X).
female(mary).
male(carrey).
parent(mary,vinni).
! ®
parent(mary,andre).
parent(carrey,vinni).
parent(carrey,andre).
mother(mary,vinni).
mother(mary,andre).
father(carrey,vinni).
father(carey,andre).
IC
TÈB |= E
TÈB |= IC
18

---

## Page 19

Prolog
• Great revolutionary idea
• The language is not linked to Von Neumann architectures
• European versus American
• Japanese Fifth generation project in the 80 (failed)
• Technology has made gigantic steps in the meantime...
• Why Prolog has not spread as believed in the 80s?
• Many applications, ideas, research, extensions Prolog in AI, but not all.
Many Prolog implementations:
SWI Prolog: widely used and well integrated with Semantic Web: http://www.swi-
prolog.org
tuProlog: Java based Prolog used for internet applications developed by Unibo.
http://apice.unibo.it/xwiki/bin/view/Tuprolog/
19

---

## Page 20

Machine learning
• Learning from experience, learning from one’s mistakes, learning
from teachers, learning by imitation, is a unique feature of
intelligence.
• Empiricist approach (which opposes to the rationalist approach).
• Definition1:
– Learning is constructing or modifying representations of what is
being experienced [Michalski 1986]
• Definition 2:
– Learning denotes changes in the system that are adaptive in the
sense that they enable the system to do the same task or tasks
drawn from the same population more efficiently and more
effectively the next time [Simon 1984], pag. 28
20

---

## Page 21

Machine learning
• Machine learning is one of the hot topics of Artificial
Intelligence
• All the most important ICT companies are investing
money on ML and hire people with a background in ML:
Google, Facebook, IBM, Baidu, Disney, . . .
WHY?
• They have many data. . .
•
. . . And want to extract value from data
21

---

## Page 22

The era of big data…..
22

---

## Page 23

Machine learning
• Supervised Learning:
– It starts from a set of examples given by a teacher ( "training set").
– It solves problems of classification/regression (ex. patterns recognition).
• Unsupervised Learning:
– Through observations and discovery.
– From the outside it does not get any help, but the system that is in charge
of analysing the information available, to classify and structure them and
to discover patterns.
– Clustering/data mining
• Reinforcement Learning:
– Learning optimal behaviour from past experiences.
– Observation of good and bad choices made (through rewards and
punishments), and modify the behaviour accordingly.
– Mainly learns from mistakes
– Finds many applications in robotics.
23

---

## Page 24

What can we do with machine learning?
Classify incoming e-mails as spam or not
Figure source: http://www.resilientsystems.co.uk/
24

---

## Page 25

What can we do with machine learning?
Apple shares price prediction
25

---

## Page 26

What can we do with machine learning?
Diagnosis based on exams of a patient
26

---

## Page 27

What can we do with machine learning?
Understand VAT numbers
Figure source: [LeCun et al., 1989]
27

---

## Page 28

What can we do with machine learning?
Teach a robot to grab a cup
Figure source: http://www.informatik.uni-bremen.de/
28

---

## Page 29

What can we do with machine learning?
Design a molecule with specific properties
Figure source: http://pande.stanford.edu/
29

---

## Page 30

What can we do with machine learning?
Text translation
30

---

## Page 31

What can we do with machine learning?
Convert a voice in text
31

---

## Page 32

What can we do with machine learning?
Automatically write the caption to a figure
Figure source: Google Research
32

---

## Page 33

What can we do with machine learning?
Beat the world champion in a game
Figure source: Google Research
33

---

## Page 34

Machine learning task: classification
Classification is the task of approximating a
mapping function (f) from input variables (X) to
discrete/categorical output variables (y).
The output variables are often called labels or categories
or classes.
The mapping function predicts the class or category for a
given observation.
Supervised learning task
34

---

## Page 35

Machine learning task: classification
• A classification problem requires that examples be
classified into one of two or more classes.
• A classification can have real-valued or discrete input
variables.
• A problem with two classes is often called a two-class
or binary classification problem. A problem with
more than two classes is often called a multi-class
classification problem.
• A problem where an example is assigned multiple
classes is called a multi-label classification problem.
• The classification accuracy is the percentage of
correctly classified examples out of all predictions
made.
35

---

## Page 36

Machine learning task: regression
Regression is the task of approximating a mapping
function (f) from input variables (X) to a continuous
output variable (y).
A continuous output variable is a real-value, such as an
integer or floating point value. These are often quantities,
such as amounts and sizes.
Supervised learning task
36

---

## Page 37

Machine learning task: regression
• A regression problem requires the prediction of a
quantity.
• A regression can have real valued or discrete input
variables.
• A problem with multiple input variables is often called
a multivariate regression problem.
• A regression problem where input variables are
ordered by time is called a time series forecasting
problem.
• Because a regression predictive model predicts a
quantity, the skill of the model must be reported as an
error in those predictions, like the RMSE
37

---

## Page 38

Machine learning task: clustering
Clustering is the problem of organizing objects into
groups whose members are similar in some way.
Clustering determines the intrinsic grouping in a set of
unlabeled data
Clustering is the main unsupervised learning task
38

---

## Page 39

Machine learning task: clustering
Clustering types
Hard clustering: each element can be assigned to
one and only one group
Soft or fuzzy clustering: each element can belong to
more than one group
Most widely used algorithm for hard clustering
k-means MacQueen 1967
39

---

## Page 40

Symbolic and sub-symbolic learning
Decision tree Neuron
Albero di Decisione
Artificial
Neuron
Funzione di
a0vazione
pesi
Somma
pesata
Prolog
suggest(H) :- stelle(H,***).
suggest(H):- stelle(H,**),
centro(H,vicino).
Stelle Costo Centro Parchegg
io Classe
** Medio Vicino f +
Multi-layer networks
** Alto Lontano f -
** Alto Lontano v -
Rules
** Medio Lontano v -
** Basso Vicino v +
If the hotel is three star then
suggest it.
*** Medio Lontano f +
*** Alto Lontano v +
*** Basso Vicino f +
*** Alto Lontano v +
if the hotel is two star AND
close to the city center then
suggest it.
* Medio Lontano f -
* Basso Vicino f -
* Medio Lontano v +
* Basso Lontano v +
* Medio Lontano v +
40
…......

---

## Page 41

Symbolic learning: decision trees (ID3, C4.5)
Possible training set of hotels: Corresponding decision tree
Stelle Costo Centro Parcheggio Classe
** Medio Vicino f +
** Alto Lontano f -
** Alto Lontano v -
** Medio Lontano v -
** Basso Vicino v +
*** Medio Lontano f +
*** Alto Lontano v +
Rules
*** Basso Vicino f +
*** Alto Lontano v +
* Medio Lontano f -
* Basso Vicino f -
* Medio Lontano v +
If the hotel is three star then suggest it.
if the hotel is two star AND close to the
city center then suggest it.
* Basso Lontano v +
* Medio Lontano v +
…......
41

---

## Page 42

Artificial Neuron
Idea: directly simulate brain functioning
in a computer, and build an intelligent
machine from artificial neurons.
First mathematical model of an artificial
neuron has been inspired by the
biological neurons proposed in 1943 by
McCulloch and Pitts.
A neuron receives a set of inputs,
makes a weighted sum and then
applies an activation function to
calculate the output.
The output is controlled by an
activation function: each neuron is
active only in case its input exceeds a
certain threshold.
pesi
Somma
pesata
Funzione di
a0vazione
42

---

## Page 43

Two input perceptron
-1
w1
q
x1
X
net
S y
w2
x2
y = HS (w1 x1 + w2 x2 - q)
The patterns belonging to the class will be
those such that:
w1 x1 + w2 x2 - q > 0
43
43

---

## Page 44

Linear separation of the input space
x2 > -(w1/ w2) x1 + q / w2
x2
q/ w2
class C
q/ w1
x1
Class not C
44
44

---

## Page 45

Learning an AND gate
y = 1 if x2 > -(w1/ w2) x1 + q / w2
x2
(0,1)
(1,1)
(0,0) (1,0)
WEIGHTS
w1 =
w2 =
q =
0.5
1
1
(Dw = hdx)
x1
45
45

---

## Page 46

Neural Networks
• To represent more complex concepts
networks of neurons should be built: multi-
layer architectures (forward or feed-
forward networks), and new learning
algorithms.
• Significantly different approach from the
symbolic one. The knowledge is not
explicit but inherent in the network
structure and connection weights.
NEURAL
NETWORK
DATA
OUTPUT
OUTPUT
LAYER
INPUT
LAYER
SECOND
HIDDEN LAYER
FIRST HIDDEN
LAYER
feed-forward network with
two hidden layers
46

---

## Page 47

Three-layer networks
They are able to separate convex regions
number of edges £ number hidden neurons
x2
x1 x2
x1
47
47

---

## Page 48

Three-layer networks
They are able to separate convex regions
number of edges £ number hidden neurons
x2
x1 x2
x1
48
48

---

## Page 49

Three-layer networks
They are able to separate convex regions
number of edges £ number hidden neurons
x2
x1 x2
x1
49
49

---

## Page 50

Four-layer networks
• They are able to separate regions of every
shape
x2
x1
x1 x2
50
50

---

## Page 51

Neural networks: power and limitations
• The perceptron can represent only linear functions. If, however, we
use multi-layer networks, the expressive power increases
substantially.
• Universal approximation theorem: A feed-forward network with one
hidden layer and a finite number of neurons can approximate any
continuous function with desired accuracy.
• Interesting theory, but it says nothing about how to configure the
neural network and how to apply the learning algorithms to get a good
approximation. What output functions? How many neurons? How
many layers?
• From the 80s more complex and detailed models have been designed
for artificial neurons, with different non-linear functions (for example
the sigmoid).
• Also various architectures have been identified, and more
sophisticated learning algorithms have been developed
51

---

## Page 52

Deep Neural Networks and Deep
learning
• Deep Learning: models and algorithms that use
neural networks with many neurons and many layers.
They can learn complex functions, trying to identify
most relevant data (rough).
• The most commonly used DNNs consist of a very
number of levels (even some hundreds)
• Computational expensive training process
• The supervised algorithms currently get good
performance with around 5,000 examples for each
category and surpass humans with 10 million
examples.
• It is not a "simulation" of the brain that has more
neurons and a much more complex structure. With a
further development of computing power, we will have
a comparable number of neurons with human in 2050.
Da: I. Goodfellow, Y. Bengio, A. Courville: “Deep Learning”, MIT Press,
http://www.deeplearningbook.org, 2016
52

---

## Page 53

Deep Neural Networks and Deep learning
In Deep Learning concepts are learnt through a hierarchy of features,
from the simplest to more abstract and complex. Representation is
implicitly distributed in different layers
https://leonardoaraujosantos.gitbooks.io/artificial-inteligence/content/deep_learning.html
53

---

## Page 54

54

---

## Page 55

55

---

## Page 56

56

---

## Page 57

57

---

## Page 58

Automated Planning
Automated Planning is an important problem solving
activity which consists in synthesizing a sequence of
actions performed by an agent that leads from an
initial state of the world to a given target state (goal)
Given:
• an initial state
• a set of actions you can perform
• a state to achieve (goal)
Find:
a plan: a partially or totally ordered set of
actions needed to achieve the goal from the
initial state
58

---

## Page 59

Automated Planning
An automated planner is an intelligent agent that
operates in a certain domain described by:
1. 2. 3. a representation of the initial state
a representation of a goal
a formal description of the executable actions (also
called operators) in terms of precondition and effects
It dynamically defines the plan of actions needed to
reach the goal from the initial state.
59

---

## Page 60

Example: block world
Actions:
STACK (X, Y)
IF: holding (X) and clear (Y)
THEN: handempty and clear (X) and on (X, Y);
UNSTACK (X, Y)
IF: handempty and clear (X) and on (X, Y)
THEN: holding (X) and clear (Y);
X
Y
X
Y
X
Y
X
Y
60

---

## Page 61

Example: block world
PICKUP (X)
IF: ontable (X) and clear (X) and handempty
THEN: holding (X);
PUTDOWN (X)
IF: holding (X)
THEN: ontable (X) and clear (X) and handempty.
X
X
X
X
61

---

## Page 62

Planning Techniques
• Deductive planning / planning as search/ linear planning in
Foundations of AI
• Nonlinear planning
• Partial Order Planning (POP)
• Hierarchical planning
• Conditional planning
• Graph-based planning
• Planning for robotics paths
• Planning as emergent behavior: swarm intelligence
• Reinforcement learning (to learn a policy)
62

---

## Page 63

Swarm intelligence
Nature has developed verious forms of
distributed intelligence
• our organism, spieces selections for
adapting to environmental changes
(Genetic algos)
• Coordination among animals (ants
building huge nests or moving heavy
objects without any central coordination)
(Swarm Intelligence)
Who is governing all this? Who is giving
instructions, predict future dynamics,
produce plans and maintain equilibrium?
• These smart behaviour emerge
autonomously with no central
coordination nor supervision.
• Development of intelligent systems
based on natural metaphores, that are
robust and adaptive.
• Swarm intelligence and swarm robotics
63

---

## Page 64

Ants and food search
64

---

## Page 65

Genetic and evolutionary algorithms
• Genetic algorithms (and evolutionary
algorithms in general) are inspired by the
natural evolution and have been
developed in the 70s by John Holland.
• We start from an initial ramdom
population of individuals, that create new
individuals through specific laws (cross-
over - mutation).
• Fitness: ensures that only the best
individuals are kept.
• Mutation: new elements introduced
randomly
• Cross-over combines good parent
solutions.
• Fitness is not always easy to define. Can
be asked to the user in some cases.
• These algorithms are useful when a
model of the problem is hard to be
defined.
65

---

## Page 66

Reinforcement learning
• Learning policies: how to act given a system state
Yk
Zk
X k
Learner
Controlled
System
R
Critic
Reinforcement: punishment or reward
66

---

## Page 67

Reinforcement learning
Beat the world champion in a game
Figure source: Google Research
67

---

## Page 68

Reinforcement learning
68