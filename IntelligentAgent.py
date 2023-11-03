import random
from BaseAI import BaseAI
import time
import math

class IntelligentAgent(BaseAI):
    def __init__(self):
        self.time_limit = None 
        self.depth_limit = 4
    def getMove(self, grid):
        #Selects a random move and returns it
        moveset = grid.getAvailableMoves()

        self.time_limit = 0.20 + time.process_time() 
        moveset = grid.getAvailableMoves()
        bestMove = self.expectMinimax(grid)

        if bestMove:
            return bestMove[0]
        else:
            return random.choice(moveset)[0] if moveset else None

    def expectMinimax(self, grid):
        return self.Maximize(grid, float("-inf"), float("inf"), 0)[0]

    def Minimize(self, grid, nodeValue, alpha, beta, depth):
        if depth > self.depth_limit or time.process_time() >= self.time_limit:
            return (None, self.evaluate(grid))
        
        minChild, minUtility = (None, float("inf"))

        for child in grid.getAvailableCells():
            child_copy = grid.clone()
            child_copy.insertTile(child, nodeValue)

            _, utility = self.Maximize(child_copy, alpha, beta, depth + 1)
            
            if utility < minUtility:
                minChild, minUtility = child_copy, utility

            if minUtility <= alpha:
                break

            if minUtility < beta:
                beta = minUtility

        return (minChild, minUtility)

    def Maximize(self, grid, alpha, beta, depth):
        if depth > self.depth_limit or time.process_time() >= self.time_limit:
            return (None, self.evaluate(grid))
        
        maxChild, maxUtility = (None, float("-inf"))
        for child in grid.getAvailableMoves():
            utility = self.ChanceNode(child[1], alpha, beta, depth)

            if utility > maxUtility:
                maxChild, maxUtility = child, utility

            if maxUtility >= beta:
                break

            if maxUtility > alpha:
                alpha = maxUtility

        return (maxChild, maxUtility)
    
    def ChanceNode(self, grid, alpha, beta, depth):
        if depth > self.depth_limit or time.process_time() >= self.time_limit:
            return self.evaluate(grid)
        
        probability2 = 0.9 * self.Minimize(grid, 2, alpha, beta, depth + 1)[1]
        probability4 = 0.1 * self.Minimize(grid, 4, alpha, beta, depth + 1)[1]

        return probability2 + probability4  
    
    def evaluate(self, grid):
        #Weights
        w1 = 12
        w2 = 1
        w3 = 1
        w4 = 7
        #Heuristics
        h1 = self.EmptyTiles(grid)
        h2 = math.log2(self.averageCellValue(grid))
        h3 = self.smoothness(grid)
        h4 = self.monotonicity(grid)
        return w1 * h1 + w2 * h2 + w3 * h3 * w4 * h4    

    def EmptyTiles(self, grid):
        if grid is not None:
            return len(grid.getAvailableCells())
        return 0

    def averageCellValue(self, grid):
        if grid is not None:
            tile_sum = 0
            tempMap = grid.map
            for row in tempMap:
                tile_sum += sum(row)
            return tile_sum
        return 0
    
    def smoothness(self, grid):
        smoothness = 0
        for row in range(grid.size):
            for col in range(1, grid.size):
                if grid.map[row][col-1] == grid.map[row][col]:
                    smoothness +=1
        for col in range(grid.size):
            for row in range(1, grid.size):
                if grid.map[row-1][col] == grid.map[row][col]:
                    smoothness +=1
        return smoothness

    def monotonicity(self, grid):
        ''' Checks rows and columns to determine if the 
        values are in a non-decreasing or non-increasing order 
        and accumulates a score based on these patterns.'''
        monotonicity = 0
        for row in range(3):
            for col in range(3):
                if grid.map[row][col] >= grid.map[row][col + 1]:
                    monotonicity += 1
                    if grid.map[col][row] >= grid.map[col][row + 1]:
                        monotonicity += 1
        return monotonicity


    