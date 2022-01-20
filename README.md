# CS50-AI

## Overview

This repository is based on the course CS50's Introduction to Artificial Intelligence with Python. It contains my solution for the 12 different projects offered from this course. Overall, it is really an amazing open-source course, packed with information on various AI aspects with very amazing lectures and intriguing projects. For more information about the course, please refer to this [link to the official CS50 AI website](https://cs50.harvard.edu/ai/2020/).  

## All Projects

### Project 0a: Degrees

This program determines the 'degree of seperation' between 2 different actors based on data from IMDb, '1' degree means that the two actors have starred together in the same movie, '2' means that the two actors can be correlated in two steps, where each step consists of finding a film that two actors both starred in, and so on. The algorithm involves breadth first search using Queue Frontier, which requires general understanding of data structure (class, node, frontier) and searching algorithm.

### Project 0b: Tic-Tac-Toe

Implementing a simple Tic-Tac-Toe game functionality, along with an AI player that makes optimal move as either 'X' or 'O'. The AI never loses, it will always at least be a draw (if you play optimally), or a win for the AI if the human does not play optimally. The AI involves adverserial search using minimax algorithm with alpha-beta pruning.

### Project 1a: Knights

A program that solve logic puzzles by encoding the underlying propositional logic as the knowledge base, and letting the AI solve the puzzle. The model checking involves enumerating all of the possible outcome and checking for entailment.

### Project 1b: Minesweeper

This project involves creating an AI that can play Minesweeper optimally based on knowlege engineering. In this case, the usual propositional logic and model checking takes too much time and information to be represented, so this problem use an alternate knowledge representation and inference approach. Please note that the AI is still able to lose, in case it gets unlucky and clicks on a 'bomb' in the first move when it has no knowlege information yet.

### Project 2a: Pagerank

This program replicates Google's pagerank algorithm which is used to rank websites based on importance. This project uses two different approach, first being the random surfer model which represents a user randomly clicking links for very many times. The second approach uses the formal iterative approach formula with the consideration of damping factor. Concepts involved in this project including probability theory, sampling and Markov Chain.

### Project 2b: Heredity

This AI assess the likelihood of a person inherits hearing impairment by the GJB2 gene based on their parents' information and known joint probabilities. It involves manually constructing Bayesian Network structure involving probability theory.

### Project 3: Crossword

This AI generates a random crossword based on a list of words to use, that fits into a given structure of a crossword puzzle. This project mainly focuses on solving constraint satisfaction problem, by implementing various algorithm including enforcing arc and node consistency, backtracking, and pruning using MRV and degree heuristic.

### Project 4a: Shopping

Implementing k-nearest neighbor classifier supervised learning model that predicts whether an online shopping customer will complete a purchase based on 17 different evidences. This project tested our ability to load and model huge data, train the model, and evaluate the accuracy of the learning outcome based on true positive and negative rate.

### Project 4b: Nim

An AI using epsilon-delta q-learning (reinforcement learning) that learns to play the game Nim on its own by playing against itself for numerous times and gain experience throughout the process. Please note that the algorithm has an epsilon rate of 0.1, which is the chance for the AI to explore random moves apart from exploiting known paths, which means that the AI still can sometimes lose even with high training numbers.

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
