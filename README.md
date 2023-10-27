# 2048 Adversarial Search Agent Assignment

In this assignment, you will create an adversarial search agent to play the 2048-puzzle game. A demo of the game is available [here](https://play2048.co/).

## Table of Contents
[I. 2048 As A Two-Player Game](#i-2048-as-a-two-player-game)
[II.Choosing a Search Algorithm: Expectiminimax](#ii-choosing-a-search-algorithm-expectiminimax)
[III.Using The Skeleton Code](#iii-using-the-skeleton-code)
[IV.What You Need to Submit](#iv-what-you-need-to-submit)
[V.Important Information](#v-important-information)
[VI.Optional Heuristics](#vi-optional-heuristics)
[VII.Before You Submit](#vii-before-you-submit)

## I. 2048 As A Two-Player Game
2048 is played on a 4x4 grid with numbered tiles which can slide up, down, left, or right. This game can be modeled as a two-player game, in which the computer AI generates a 2- or 4-tile placed randomly on the board, and the player then selects a direction to move the tiles. Note that the tiles move until they either (1) collide with another tile, or (2) collide with the edge of the grid. If two tiles of the same number collide in a move, they merge into a single tile valued at the sum of the two originals. The resulting tile cannot merge with another tile again in the same move.

Usually, each role in a two-player game has a similar set of moves to choose from, and similar objectives (e.g. chess). In 2048, however, the player roles are inherently asymmetric, as the Computer AI places tiles and the Player moves them. Adversarial search can still be applied! Using your previous experience with objects, states, nodes, functions, and implicit or explicit search trees, along with our skeleton code, focus on optimizing your player algorithm to solve 2048 as efficiently and consistently as possible.

## II. Choosing A Search Algorithm: Expectiminimax
Review the lecture on adversarial search. Is 2048 a zero-sum game? What are the minimax and expectiminimax principles? The tile-generating Computer AI of 2048 is not particularly adversarial as it spawns tiles irrespective of whether a spawn is the most adversarial to the user’s progress, with a 90% probability of a 2 and 10% for a 4 (from GameManager.py). However, our Player AI will play as if the computer is adversarial since this proves more effective in beating the game. We will specifically use the expectiminimax algorithm.

With expectiminimax, your game playing strategy assumes the Computer AI chooses a tile to place in a way that minimizes the Player’s outcome. Note whether or not the Computer AI is optimally adversarial is a question to consider. As a general principle, how far the opponent’s behavior deviates from the player’s assumption certainly affects how well the AI performs. However, you will see that this strategy works well in this game.

Expectiminimax is a natural extension of the minimax algorithm, so think about how to implement minimax first. As we saw in the simple case of tic-tac-toe, it is useful to employ the minimax algorithm assuming the opponent is a perfect ”minimizing” agent. In practice, an algorithm with the perfect opponent assumption deviates from reality when playing a sub-par opponent making silly moves, but still leads to the desired outcome of never losing. If the deviation goes the other way, however, (a ”maximax” opponent in which the opponent wants us to win), winning is obviously not guaranteed.

## III. Using the Skeleton Code
The skeleton code includes the following files. Note that you will only be working in one of them, and the rest are read-only:
- Read-only: GameManager.py. This is the driver program that loads your Computer AI and Player AI and begins a game where they compete with each other. See below on how to execute this program.
- Read-only: Grid.py. This module defines the Grid object, along with some useful operations: move(), getAvailableCells(), insertTile(), and clone(), which you may use in your code. These are by no means the most efficient methods available, so if you wish to strive for better performance, feel free to ignore these and write your own helper methods in a separate file.
- Read-only: BaseAI.py. This is the base class for any AI component. All AIs inherit from this module and implement the getMove() function, which takes a Grid object as parameter and returns a move (there are different ”moves” for different AIs).
- Read-only: ComputerAI.py. This inherits from BaseAI. The getMove() function returns a computer action that is a tuple (x, y) indicating the place you want to place a tile.
- Writable: IntelligentAgent.py. You will create this file. The IntelligentAgent class should inherit from BaseAI. The getMove() function to implement must return a number that indicates the player’s action. In particular, 0 stands for ”Up”, 1 stands for ”Down”, 2 stands for ”Left”, and 3 stands for ”Right”. This is where your player-optimizing logic lives and is executed. Feel free to create submodules for this file to use, and include any submodules in your submission.
- Read-only: BaseDisplayer.py and Displayer.py. These print the grid.

To test your code, execute the game manager like so: `$ python3 GameManager.py`. The progress of the game will be displayed on your terminal screen with one snapshot printed after each move that the Computer AI or Player AI makes. Your Player AI is allowed 0.2 seconds to come up with each move. The process continues until the game is over; that is, until no further legal moves can be made. At the end of the game, the maximum tile value on the board is printed.

IMPORTANT: Do not modify the files that are specified as read-only. When your submission is graded, the grader will first automatically overwrite all read-only files in the directory before executing your code. This is to ensure that all students are using the same game-play mechanism and computer opponent, and that you cannot ”work around” the skeleton program and manually output a high score.

## IV. What You Need To Submit
Your job in this assignment is to write IntelligentAgent.py, which intelligently plays the 2048-puzzle game.

Here is a snippet of starter code to allow you to observe how the game looks when it is played out. In the following ”naive” Player AI. The getMove() function simply selects a next move in random out of the available moves:

```python
import random
from BaseAI import BaseAI

class IntelligentAgent(BaseAI):
    def getMove(self, grid):
        # Selects a random move and returns it
        moveset = grid.getAvailableMoves()
        return random.choice(moveset)[0] if moveset else None
```

## For Any Questions and Detailed Instructions
For more detailed instructions and information, please refer to the full PDF document: [Download hw3_coding.pdf](hw3_coding.pdf).