# CS50 Artificial Intelligence

## Overview

This repository is based on the course **CS50's Introduction to Artificial Intelligence with Python**. It contains my solution for the 12 different projects offered from this course and the lecture source codes as well. Overall, it is a really amazing open courseware, packed with concepts of various AI aspects with amazing lectures and intriguing projects. For more information about the course and to enroll for free, please refer to this [link to the official CS50 AI website](https://cs50.harvard.edu/ai/2020/).

## [Project 0a: Degrees](degrees)

### Degrees - Explanation

This program determines the 'degree of seperation' between 2 different actors based on data from IMDb. '1' degree means that the two actors have starred together in the same movie, '2' means that the two actors can be correlated in two steps, where each step consists of finding a film that two actors both starred in, and so on. The algorithm involves breadth first search using Queue Frontier, which requires general understanding of data structure (class, node, frontier) and searching algorithm.

### Degrees - How To Run

Assuming you have python installed, go to the project directory and run the following on your terminal:

```powershell
    # the 'large' folder contains actual data from IMDB in csv format
    # please do not move or rename the 'large' folder or else this code won't work
    # the 'small' folder is there for testing purpose only
    # you can also try typing python degrees.py small to play around with the sample data
    python degrees.py large
```

You will then be prompted to enter 2 names, please enter any 2 actors you know. It is suspected that 'Kevin Bacon' (ID 102) can be connected to any other actors in at most 6 steps. See for yourself that Kevin Bacon is indeed popular and the BFS algorithm works :) Note that you might need to wait for a few seconds (hey, there are over 10 million actors and hundred thousands of movies there!). If it took you more than a minute, most likely the actors needed 6 steps or more to be connected.

## [Project 0b: Tic-Tac-Toe](tictactoe)

### Tictactoe - Explanation

Implementing a simple Tic-Tac-Toe game functionality, along with an AI player that makes optimal move as either 'X' or 'O'. The AI never loses, it will always at least be a draw (if you play optimally), or a win for the AI if the human does not play optimally. The AI involves adverserial search using minimax algorithm with alpha-beta pruning.

### Tictactoe - How To Run

Assuming you have python and pip installed, go to the project directory and run the following on your terminal:

```powershell
    pip install -r requirements.txt # execute this if you haven't had pygame installed
    python runner.py
```

A pygame window will appear. You can play the game there using your mouse and the built-in user interface. Prove for yourself that the AI will never lose any game!

## [Project 1a: Knights](knights)

### Knights - Explanation

A program that solve logic puzzles by encoding the underlying propositional logic as the knowledge base, and letting the AI solve the puzzle. The model checking involves enumerating all of the possible outcome and checking for entailment.

### Knights - How To Run

Assuming you have python installed, go to the project directory and run the following on your terminal:

```powershell
    python puzzle.py
```

## [Project 1b: Minesweeper](minesweeper)

### Minesweeper - Explanation

This project involves creating an AI that can play Minesweeper optimally based on knowlege engineering. In this case, the usual propositional logic and model checking takes too much time and information to be represented, so the approach is to use an alternate knowledge representation and inference approach. Please refer to [this](https://cs50.harvard.edu/ai/2020/projects/1/minesweeper/#knowledge-representation) page to understand how the knowledge representation works.

### Minesweeper - How To Run

Assuming you have python and pip installed, go to the project directory and run the following on your terminal:

```powershell
    pip install -r requirements.txt # execute this if you haven't had pygame installed
    python runner.py
```

A pygame window will appear and you can play the game using your mouse or let the AI makes a move for you. Prove for yourself how much faster the AI can make inference compared to us, humans! Please note that the AI is still able to lose, in case it gets unlucky and clicks on a 'bomb' in the first move when it has no knowlege information yet.

## [Project 2a: Pagerank](pagerank)

### Pagerank - Explanation

This program replicates [Google's pagerank algorithm](https://en.wikipedia.org/wiki/PageRank) which is used to rank websites based on importance. This project uses two different approach, first being the random surfer model which represents a user randomly clicking links for very many times. The second approach uses the formal iterative approach formula with the consideration of damping factor. Concepts involved in this project including probability theory, sampling and Markov Chain.

### Pagerank - How To Run

Assuming you have python installed, go to the project directory and run the following on your terminal:

```powershell
    python pagerank.py corpus2 # you can also try with corpus0 and corpus1
```

You will then get the pagerank results of each html file for both sampling and iterative approach. You may also provide your own corpus (html files with links to each other) as well and execute `python pagerank.py <folder_name>` to see the results of the pagerank algorithm!

## [Project 2b: Heredity](heredity)

### Heredity - Explanation

This AI assess the likelihood of a person inherits hearing impairment by the [mutated GJB2 gene] (see [here](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1285178/) for more details) based on their parents' information and known joint probabilities. It involves manually constructing Bayesian Network (see [here](https://en.wikipedia.org/wiki/Bayesian_network) for reference) structure involving probability theory.

### Heredity - How To Run

Assuming you have python installed, go to the project directory and run the following on your terminal:

```powershell
    python heredity.py data/family2.csv
```

You will see the probability of each person printed out on the terminal. You can also try other files by running `python heredity.py data/family1.csv` or `python heredity.py data/family0.csv`, as well as using your own data.

## [Project 3: Crossword](crossword)

### Crossword - Explanation

This AI generates a random crossword based on a list of words to use, that fits into a given structure of a crossword puzzle. This project mainly focuses on solving constraint satisfaction problem, by implementing various algorithm including enforcing arc and node consistency, backtracking, and pruning using MRV and degree heuristic.

### Crossword - How To Run

Assuming you have python installed, go to the project directory and run the following on your terminal:

```powershell
    python generate.py data/structure2.txt data/words2.txt
    # you can try other combinations of structure and words as well, such as:
    python generate.py data/structure0.txt data/words1.txt
    # you can also have your own list of words or crossword structure to generate
```

Note that there is not always going to be a solution.

## [Project 4a: Shopping](shopping)

### Shopping - Explanation

Implementing k-nearest neighbor classifier supervised learning model that predicts whether an online shopping customer will complete a purchase based on 17 different evidences. This project tested our ability to load and model huge data, train the model, and evaluate the accuracy of the learning outcome based on specificity and sensitivity.

### Shopping - How To Run

Assuming you have python and pip installed, go to the project directory and run the following on your terminal:

```powershell
    pip install scikit-learn # execute this if you haven't had scikit-learn installed
    python shopping.py shopping.csv
```

Note that the specificity and sensitivity percentage gained might not always be the same for every execution.

## [Project 4b: Nim](nim)

### Nim - Explanation

An AI using epsilon-delta q-learning (see algorithm [here](https://en.wikipedia.org/wiki/Q-learning#Algorithm)) that learns to play the game Nim on its own by playing against itself for numerous times and gain experience throughout the process. The last player who takes the last pile loses the game.

### Nim - How To Run

Assuming you have python installed, go to the project directory and run the following on your terminal:

```powershell
    python play.py
```

You can then take turn playing against the AI. Please note that the algorithm has an epsilon rate of 0.1, which is the chance for the AI to explore random moves apart from exploiting known paths, which means that the AI still can sometimes lose even with high training numbers. You can also customize the game by changing the initial number of piles and its count, or the number of games training played.

### Project 5: Traffic

Implementing computer vision using convolutional neural network and deep learning to distinguish 43 different traffic signs with thousand of distinct images based on the GTSRB dataset. It requires us to load and convert a whole image as image arrays, experimenting with various configurations of convolutional, pooling and hidden layers as well as documenting the training process.

### Project 6a: Parser

sfsf

### Project 6b: Questions

sfsdf

## Course Materials

### Week 1

various search algorithms such as breadth f...

### Week 2

### Week 3

### Week 4

### Week 5

### Week 6
