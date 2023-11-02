import random
from BaseAI import BaseAI
import time

class IntelligentAgent(BaseAI): 
    
    def __init__(self):
        self.depth_limit = 3
        self.time_limit = 0.2
        self.start_time = time.process_time()
    def getMove(self, grid):
        '''   
        # Selects a random move and returns it
        moveset = grid.getAvailableMoves()
        return random.choice(moveset)[0] if moveset else None
        '''
        moveset = grid.getAvailableMoves()
        best_move, _ = self.Maximize(grid, float("-inf"), float("inf"), 0)
        return best_move[0]
        
    def Minimize(self, grid, alpha, beta, depth):
        if self.terminalTest(grid) or depth >= self.depth_limit or time.process_time() > self.time_limit:
            return(None, self.evaluate(grid))
        
        minChild = None
        minUtility = float("inf")

        for child in grid.getAvailableMoves():
            Child_copy = grid.clone()
            Child_copy.move(child)

            _, utility = self.Maximize(Child_copy, alpha, beta, depth + 1) 

            if utility < minUtility:
                minChild, minUtility = child, utility
                
            if minUtility <= alpha:
                break
            if minUtility < beta:
                beta = minUtility
        return minChild, minUtility
    
    def Maximize(self, grid, alpha, beta, depth):
        if self.terminalTest(grid) or depth >= self.depth_limit or time.process_time() > self.time_limit:
            return(None, self.evaluate(grid))
        
        maxChild = None
        maxUtility = float("-inf")

        for child in grid.getAvailableMoves():
            Child_copy = grid.clone()
            Child_copy.move(child)
            _, utility = self.Minimize(Child_copy, alpha, beta, depth + 1) 

            if utility > maxUtility:
                maxChild, maxUtility = child, utility
                
            if maxUtility >= beta:
                break
            if maxUtility > alpha:
                alpha = maxUtility
        return maxChild, maxUtility
    
    def terminalTest(self, grid):
      return not grid.getAvailableMoves() or self.exceedTimeLimit()
    
    def exceedTimeLimit(self):
        return time.process_time()> self.time_limit

    def evaluate(self, grid):
        smoothness_weight = 1.0  # Adjust the weights as needed
        monotonicity_weight = 1.0
        return self.weighted_evaluation(grid, smoothness_weight, monotonicity_weight) 
        
    def weighted_evaluation(self, grid, smoothness_weight, monotonicity_weight):
        smoothness_score = self.smoothness(grid)
        monotonicity_score = self.monotonicity(grid)
        return smoothness_weight * smoothness_score + monotonicity_weight * monotonicity_score        

    def monotonicity(self, grid):
        ''' Checks rows and columns to determine if the 
            values are in a non-decreasing or non-increasing order 
            and accumulates a score based on these patterns.'''
        monotonicity_score = 0
        for i in range(grid.size):
            row = [grid.map[i][j] for j in range(grid.size)]
            reversed_row = row[::-1]
            if sorted(row) == row or sorted(reversed_row) == reversed_row:
                monotonicity_score += sum(row)
        for j in range(grid.size):
            col = [grid.map[i][j] for i in range(grid.size)]
            reversed_col = col[::-1]
            if sorted(col) == col or sorted(reversed_col) == reversed_col:
                monotonicity_score += sum(col)
        return monotonicity_score
    
    def smoothness(self, grid):
        ''' Penalizes adjacent tile differences, 
            encouraging smoother transitions between neighboring tiles.'''
        smoothness_score = 0
        for i in range(grid.size):
            for j in range(grid.size - 1):
                if grid.map[i][j] and grid.map[i][j + 1]:
                    smoothness_score -= abs(grid.map[i][j] - grid.map[i][j + 1])
        for j in range(grid.size):
            for i in range(grid.size - 1):
                if grid.map[i][j] and grid.map[i + 1][j]:
                    smoothness_score -= abs(grid.map[i][j] - grid.map[i + 1][j])
        return smoothness_score
    
