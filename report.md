# Adversarial Isolation game playing event

## Introduction
Using alpha-beta pruning with openning book for the first 4 depth.

## Questions
###how did you choose the winner for opening book?
10 random rollout was simulated for each state in the first 4 depth and each win is rewarded 1 point and a loss is rewarded -1 point
The move with the highest score is chosen
### What opening moves does your book suggest are most effective on an empty board for player 1 and what is player 2's best reply?

### Result


I used a random action agent as a baseline to compare against alpha-beta pruner and alpha-beta pruner with openbook. I have also included a q table open book only algorithm for comparison

| algorithm | win % (1000 trials)| loss % (1000 trials)|
|-----------|--------------------|---------------------|
|random action|                  |                     |
|alpha beta pruner|              |                     |
|openbook +abpruner|             |                     |
|q table (openbook) only|        |                     |



We can conclude that openbook + alpha beta pruner is the best algorithm out of the tree.


### Evaluation

Book can be made deeper and the scoring of openbook can be constructed with minimax random policy instead of outright guesses if resources and time are available. Furthermore, symmetry techniques can be used to reduce the search requirment and improve the odds while deeplearning techniques can be used if GPU is available.

