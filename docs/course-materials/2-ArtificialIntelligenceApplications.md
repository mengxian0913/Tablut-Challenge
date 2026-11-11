# 2-ArtificialIntelligenceApplications

Source: [2-ArtificialIntelligenceApplications.pdf](2-ArtificialIntelligenceApplications.pdf)

> Text extracted with OCR; recognition may contain errors, especially in diagrams and images.

---

## Page 1

Artificial Intelligence applications
$2,000
$5,000
$5,000
ken
WATSON
BRAD
Medical data
is expected
to double
every 73 days
by 2020
IBM Watson Health
tộ: AlphaGo
(Figure frsm vinton.ataaferd.ada]

---

## Page 2

Artificial Intelligence applications
• Decision support systems
- Very specialized on a given domain
- Knowledge based and control
1042
• Formal systems and games (Chess/GO)
₴ &
8
- Limited number of moves and space
- Based on explicit, non-ambiguous rules
• Natural language - question answering (Watson)
- Ambiguous, implicit, context dependent
- Based on cognitive states
• Vision (ImageNet)
- Object recognition/classification
- Uncertanty and noise (simbolic/sub-simbolic)
• Robotics and Autonomous systems (Robot)
- Agents working in an environment
- Dynamic and real-time decisions
2

---

## Page 3

Knowledge based systems
"The power of an intelligent system primarily derives by the quantity and
quality of the knowledge it has on the problem". (Feigenbaum)
Various applications: Planning, Prediction, Diagnosys.
Knowledge acquisition: bottleneck of KBS
Problems
• The human expert cannot be substituted, but supported in long and
repetitive tasks
• Different knowledge sources (often in contrast and incomplete)
• Knowledge changes in time
• Knolwedge is not always explicit (discovery)
→ Learning and data-mining techniques
3

---

## Page 4

Decision support systems
•
Systems that support and do not replace human
experts in their decision making process through:
• Scenario generation, evaluation, visualiations,
predictions
• Various degrees of decision support:
• Data analysis for description
• Diagnosys
• Prediction
• Optimiation
• Decision automation is one step forward as it excludes
the human intervention
4

---

## Page 5

Human intervention in decisions
Analytics
Human Input
Descriptive
What happened?
Diagnostic
Why did it happen?
Predictive
Data
Decision
Action
What will happen?
Decision Support
Prescriptive
What should I do?
Decision Automation
Source: Gartner, #G00254653 (September 2013)
5

---

## Page 6

Descriptive analytics
Data are used to describe the system
Visualization dashboards
• Business intelligence
Statistical reports
• Geo-referenced data
Human intervention is largely needed

---

## Page 7

Example of descriptive analytics
• Configuration of
a productive system/process with
environmental constraints
600_ DECK MACHINERY &
EQUIPMENT
For each process component
Raw material
we have to characterize data
Piping Drawing
foundation
Machinery
Part manufacturing
Cast Fusion
on:
UPSTREAM
PROCESSES
Deck Machinery &
Equipment
Windlass
aneneans chain
• Energy consumption
Electrical
Hydraulic
Mechanical
• Water consumption
• Emissions in the air
Machinery
• Emissions in the water
Installation
Part Installation
• Time of work
CORE
• Cost
PROCESSES
Piping connection
Static data: system characterization
7

---

## Page 8

Example of descriptive analytics
Energy baseline
Yield impianto vs. baseline da irraggiamento [kWh/kWp]
September 18, 2016
September 19, 2016
September 20, 2016
September 21, 2016
September 22, 2016
September 23, 2016
0.3
ЛАЛЛАЛ
0.2
0.1
0.0-
01 03 05 07 09 11 13 15 17 19 21
01 03 05 07 09 11 13 15 17 19 21
01 03 05 07 09 11 13 15 17 19 21
03 05 07 09 11 13 15 17 19 21
01 03 05 07 09 11 13 15 17 19 21
CT 03 05 07 09 11 13 15 17 19 21
CUSUM (baseline da irraggiamento - produzione) [MWh]
September 18, 2016
September 19, 2016
September 20, 2016
September 21, 2016
September 22, 2016
September 23. 2016
0.4
CUSUM (MWh)
ALERT! (0.5 MWh)
baseline
-measured
0.0
-cumulated difference
01 03 05 07 09 11 13 15 17 19 21
01 03 05 07 09 11 13 15 17 19 21 01 03 05 07 09
13. 15 17 19 21
01 03 05
11 13 15: 17 19.21
Dt 03 05 07 09
11 13 15 17 19 21 01 03 05 07 09 11 13 15 17 19 21
seasIDe
8

---

## Page 9

Diagnostic analytics
• Uses data to understand causes
• Fault diagnosis
Root cause analysis
• To reach decisions human intervention is still
largely needed
9

---

## Page 10

Example of diagnostic analytics
• System for analyse data from a plant and to realize
a diagnostic system
E AMA Saltocentrali Termiche
70/12/2013
16:35:20
From plant data coming from
Visualia Grafico
Modifica Parametri
Connnessione Allarme Temp.EXT Temp.MAND Locale/Remoto
sensors
ST-40
ST-42
NO
ST-53
ST-43
NO
ST-44
vali a + fault data:
ST-45
NO
ST-47
• Identify temporal series that
ST-48
ST-49
NO
ST-50
ST-51
HO
NO
precede a fault
ST-52
ST-53
110
SPO
46 PC
ST-54
Remoto
11US1-C
TT02 (°C)
• Classify the temporal series
ST-55
NO
ST-56
NO
ST-57
NO
before the fault to identify the type
ST-58
ST-60
ST-59
NO
ST-62
S1-61
NO
of fault
Valvola 3 vie
ST-63
558
4,77 °C Temp Esterna (°C)
ST-65
ST-64
NO
Galleggiante
• Identify the most informative
ST-66
NO
sensors
© 2016 National Instruments Corporation
• Create models to identify causes.
10

---

## Page 11

Predictive analytics
• Uses data to predict future system evolutions
• Simulation systems
Temporal series prediction
Machine learning classification and regression
• To reach decisions we need what if analysis
11

---

## Page 12

Example of predictive analytics
• System to predict the consumption of a
photovoltaic system
Input
• Historical temporal series of past production
Meteo forecast
• Day/month/year
1.0г
0.8-
•
Output
0.6-
0.4-
Future production
0.2-
hides tale
0.0-
-0.2-
12

---

## Page 13

Example of predictive analytics
• System to predict the photovoltaic adoption
depending on diverse incentive schema
Model
Agents divided by type
• Agents characterised by social and economic
aspects
Past data (incentives/adoption)
Output
•
Simulative model
13

---

## Page 14

Decision support - prescriptive analytics
Prescriptive analytics
Optimization systems (mono and multi objective)
• Combinatorial problem solvers
• Logic based solvers
• To reach decisions we need to select the preferred
scenario.
14

---

## Page 15

Example of prescriptive analytics
• Decision support systems for proposing incentives
to foster a given PV adoption
Optimization system that takes as input
• Simulator model
Economic/financial/territorial
• Objective functions
• Output
Alternative scenarios
• Impacts
15

---

## Page 16

Human intervention in decisions
Analytics
Human Input
Descriptive
What happened?
Diagnostic
Why did it happen?
Predictive
Data
Decision
Action
What will happen?
Decision Support
Prescriptive
What should I do?
Decision Automation
Source: Gartner, #G00254653 (September 2013)
16

---

## Page 17

Human intervention in decisions
Value & Complexity
Act
Analyze
Prescriptive
Inform
Predictive
Analytics
Diagnostic
Analytics
Descriptive
Analytics
Analytics
What happened?
Why did it happen?
What will happen?
What shall we do?
Examples
• Plant operation report
• Load forecasting
• Self-learning systems
• Alarm management
• Fault report
• Fault prediction
• Control optimization
• Root cause identification
• Sales reports
• Price forecasts
• Load balancing
• Fault analysis
• Service statistics
• Demand forecasts
• Production re-planning
Current penetration across all industries (according to Gartner 2013)
Adopt by vast
Adopted by
Still few
Very few early
99%
majority but not
30%
minorities
13%
adopters
3%
adopters
all data
17

---

## Page 18

Application domains of DSS
• Decision support systems apply to a large
variety of domains:
• Industry (manufacturing, automotive,
avionics, food, energy ....)
• Public sector (health, mobility, public
administration)
Global challenges (climate change, poverty,
conflict reduction, enviornmental health,
natural disaster mitigation)
18

---

## Page 19

Games: Chess challenge
L'esprit vaincuar la machine
gre de Bakou vaincu par une puce : le ligre,
rel Kasparov, le meilleur joueur d'échecs du monde :
st le Pentium, le plus rapide des
eurs sour Po A Londres, c'est le cerveau
vremporte furts danie hunhain
Pentiur
G. Kasparov
Process
Deep Blue, IBM Risk 2000 ...
- Evaluates 200 millions of moves per second
- knows 600.000 chess opening
• In 1997 Deep Blue beats Kasparov: is this intelligence?
Chomski about Deep Blue, "a computer program's beating a
grandmaster at chess is about as interesting as a bulldozer's
"winning" an Olympic weight-lifting competition"
19

---

## Page 20

Algoritmo minmax → the brute force
• The min
max algorithm is
designed to define the optimal
strategy for one player (max) and
for suggesting the best move: for
+1
doing that the has makes
the
a
Max
hypothesis that Min plays at his
best.
-1
+1
Min
• Huge problem space dimension.
First move: 400 alternatives.
-1
Second move 144.000
-1
+1
.....
Combinatorial explosion
f
Max
+1
• We need an evaluation function
-1
that evaluates the position of each h
Min
piece and the overall position on -1
+1
the chessboard.
n
q
+1
-1
+1
0
20

---

## Page 21

Games
(Ố: Google DeepMind
g) AlphaGo
Challenge Match
8 - 15 Мася 2016
ichafso
Lee Sedol

---

## Page 22

Games AlphaGO
ột AlphaGo
• AlphaGo has been developed from DeepMnd (acquired
by Google in 2014). It learns to play videogames (49
games for Atari 2600) better than humans.
• Deep learning and simbolic techniques.
• March 2016:
AlphaGo beated Lee Sedol, world
champion of Go
• Way more complex than chess: 10170 possible
positions (1050 for chess).
Challenge Match
• IJCAl Marvin Minsky Medal for Outstanding
8-15 March 2016
Achievements in Al in 2017. Michael Wooldridge, Chair
of the IJCAl Award: "What particularly impressed IJCAl
was that AlphaGo achieves what it does through a
brilliant combination of classic Al techniques as well as
the state-of-the-art machine learning techniques that
DeepMind is so closely associated with. It's a
breathtaking demonstration of contemporary Al...".
00 1
22

---

## Page 23

DNN
Learning but not
Deep Reasoning!
"After 240 minutes of training, [the
system] realizes that digging a tunnel
through the wall was the most
effective technique..."
BUT...
The system does not know neither
what is a tunnel nor what is a wall. It
has learnt contingencies in specific
scenarios.
23

---

## Page 24

Question answering and NLP
JEOPARDY!
Watson (IBM)
•
Jeopardy is one of the most popular quiz in US since 1964
•
You have possible answers (clue) and participants have to decide which is the
most appropriate question for that answer. Es. The President of the United
States in the sixties Proper question: Who is Kennedy?
Watson, the supercomputer developed by BM, won against Ken Jennings,
famous for the record of 74 consecutive victories and Brad Rutter, in Feb 2011:
2 won and one tie for Watson.
The knowledge in Watson has been built from texts, encyclopedia and the
web.
Watson is large like 10 fridges, it performs 80 trillion operators per second and
reads 200 million pages in 3 seconds
HINK
DEN
$2,000
$5,000
$5,000
Ken
WATSON
BRAD
24

---

## Page 25

John Searle: "Watson Doesn't Know It Won on 'Jeopardy!'
IBM invented an ingenious program—not a computer that can think."
Noam Chomsky: "Watson understands nothing. It's a bigger steamroller.
Actually, I work in Al, and a lot of what is done impresses me, but not these
devices to sell computers."
Watson tells us that intelligence is a mixture between algorithms,
knowledge and the way this is stored, used, organized.
Due tasks: text generation (humans better than computer) and
answer generation (computer better than humans).
~1 000 000
million
lines of code
Element
Number
Time to answer one
5 years
of cores
Jeopardy! question
development
(20 men)
Single core
1
2 hours
Memory:
Single IBM Power 750 server
32
<4 min
20 TB
200 million
Single rack (10 servers)
320
<30 seconds
pages
(~1 000 000
IBM Watson (90 servers)
2 880
<3 seconds
books)
25

---

## Page 26

Internet and the Semantic Web
The Web contains everything an intelligent agent should "know". Search
Engines always allow to retrieve the required information.
The Web is a
"distributed",
"emergent",
"autonomous" and "complete" repository of human
knowledge.
Internet is full of information and knowledge and it can be used by
humans and computers. It should be structured and made easier to
retrieve.
→ Semantic web..... "uses" e "reasons on" Web data
→ WWW development, memory cost reduction and mthe presence of
instructured big data, the augmented computing power, has changed
the nature of Al applications.
→ Storing all human knowledge and storing common sense in a usable
way is possible. Can it be achieved now?
→ Knowledge should be organized and structured: Ontologies
26

---

## Page 27

Simple example
• Through ontologies, we can add semantis. The cat and lion are both
feline so are subclasses of this concept
{animal, beast}
• Each time I search for «feline» both cats and lions images will be
found even if none of them has been tagged as feline.
• Ontologies are also used to solve natural language ambiguity. In italy
{mammal;
for examklpe Feline is a salami type.
• WordNet: https://wordnet.princeton.edu/
• BabelnNet https://babelnet.org/
{feline}
{dog}
{cat}
{lion}
felino
{tabby cat}
27

---

## Page 28

Text-to-speech
Google: Tacotron 2, is a text-to-speech system based on neural networks.
https://google.github.io/tacotron/publications/tacotron2/index.html
"George Washington was the first President of the United States."
One of the audio is human while the other is synthetic voice
They are indistinguishable.
28

---

## Page 29

Computer Vision
• ImageNet Challenge: Universal image classifier
•
14M images
20k categories
•
Tagged via crowdsourcing
• Labelled with the WordNet hierarchy
• In 2011 classification error 26%, today 3% (humans are less efficient:
error 5%).
[Figure from vinion.atanford.adu)
Russakovsky, O., Deng, J., Su, H., Krause, J., Satheesh, S., Ma, S., ... & Fei-Fei, L. (2015). Imagenet large
scale visual recognition challenge. arXiv preprint arXiv: 1409.0575.

---

## Page 30

Computer Vision
mite
conta
ner ship
motor scooter
leopard
ontain
motor scoote
black widow
go-kar
COckroach
mog
bek
fireboat
bumper car
snow leopard
starfish
destling platform
golfeart
Egyptian cat
grille
mushroom
cherry
Madagascar cat
convertible
agaric
dalmatian
squirrel monkey
grille
mushroom
grape
spider monkey
pickup
jelly fungus
elderberry
titi
beach wagon
gill fungus
Mordshire bullterrier
Indiri
fire engine
dead-man's-fingers
CurranT
howler monkey
[Figure from Krizhevsky et al., 2012]
30

---

## Page 31

Captioning
• Describe the content of an image (from Google).
Describes without errors
Describes with minor errors
Somewhat related to the image
Unrelated to the image
A person riding a
Two dogs play in the grass.
A skateboarder does a trick
A dog is jumping to catch a
motorcycle on a dirt road.
on a ramp.
frisbee.
A group of young people
Two hockey players are fighting
A little girl in a pink hat is
playing a game of frisbee.
over the puck.
A refrigerator filled with lots of
blowing bubbles.
food and drinks.
31

---

## Page 32

DNN: sometimes they make big mistakes!
DNN can be unstable: by applying some perturbations to inputs we can
arbitrarily change the output.
Original Image
Hacked Image
Persian cat m
• 87%
toaster
1 98%
lynx 0%
Crock Pot 1%
Angora 8%
Siamese cat 0%
dishwasher 0%
wallaby 0%
Pomeranian 0%
carton 0%
"Only modification of some pixels not evident to the human eye".
https://medium.com/@ageitgey/machine-learning-is-fun-part-8-how-to-intentionally-trick-neural-networks-b55da32b7196
32

---

## Page 33

Can we trust DNN
DNN are extremely effective in perception tasks but.....
"Are data and computational power eager and work in a known and
stable world."
We coud have problems is we work on new data that are far from the training data (overfitting)
Data might be biased (more on this later)
"Hardly explainable"
Millions of parametrs that are hard to understand not onlyby users but also by developers. Noe easy to
explain the reason of a decision.
"Do not distinguish between causality and correlation"
DNN are statistical techniques that can discover complex and non linear correlations between input and
output but these are not necessarily cause-effect relations. Just curve-fitting.
"Not trustworthy"
They can make big mistakes that are "different" from mistaked made by humans.
THE BOOK OF WHY: The New Science of Cause and Effect
le, 15 May 2018.
Gary Marcus, "Deep Learning: A Critical Appraisal". CoRR abs/1801.00631 (2018).
"Explainable Artificial Intelligence: Understanding, Visualizing and Interpreting Deep Learning
Models",
', W. Samek, T. Wiegand, K. Müller (August 2017).
33

---

## Page 34

Far from causality
Funny example: http://tylervigen.com/spurious-correlations
Per capita consumption of mozzarella cheese
correlates with
Civil engineering doctorates awarded
Correlation: 95.86% (r=0.958648)
2000
2001
2002
2003
2004
2005
2006
2007
2008
2009
12lbs
1000 degrees
11lbs
800 degrees
Mozzarella cheese consumption
Engineering doctorates
10lbs
600 degrees
9lbs
400 degrees
2000
2001
2002
2003
2004
2005
2006
2007
2008
2009
• Engineering doctorates • Mozzarella cheese consumption
tylervigen.com
Data sources: U.S. Department of Agriculture and National Science Foundation
34

---

## Page 35

Mind needs a body
sensors
percepts
think
environment
agent
actions
effectors
35

---

## Page 36

Atlas doing Parkour (Boston Dynamics)
CAUTION
Boston Dynamics
36

---

## Page 37

Robocup
• Contest started in Japan in 1997 with the goal of creating a soccer team
within 2050 able to play against (and possibly beat) the world champion
team
• Too ambitious? Deep Blue has been created 50 years after the first
computer was invented, Moon landing (1969) 50 years after the first
airplane.
New challenge very different from games: immersed in an environment
• Autonomous Robots, with real-time sensing, reaction, communication,
vision, perception, movement, coordination, planning learning cababilities.
• Full Turing Test
37

---

## Page 38

Nao: structure
TACTILE SENSORS
SPEAKERS IX2I AND
FRONT & REAR
EARLEOS
MICROPHONES
INFRARED EMMITER/
RECEIVER AND EYELEDS
CAMERAS (XZ)
LATERAL
HEAD JOINT
MICROPHONES [X2)
SHOULDER JOINT
CHEST BUTTON
SONARS (X4)
ELBOW JOINT
BATTERY
HIP JOINT
- WRIST JOINT
PREHENSILE
HANDS
- TACTILE SENSORS
KNEE JOINT
ANKLE JOINT
BUMPERS IX2I
ALDEBARAN
Robotic
3838

---

## Page 39

NAO and Robocup
FARTING
3
g r
rinance
HT
HTWK
Letarig
By Nao-Team HTWK, Università di Lipsia
39

---

## Page 40

Nao reads a text (in italian)
Thesys of Andrea Di Luzio, Università di Bologna
40

---

## Page 41

Nao plays with natural language
Thesys of Laura Bosso, Università di Bologna, and Al group DISI
41

---

## Page 42

Nao solves math expressions
Thesys of Paolo Magnani - Università di Bologna
42