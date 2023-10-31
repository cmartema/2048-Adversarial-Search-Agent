import random
from BaseAI import BaseAI
class IntelligentAgent(BaseAI): 
    def getMove(self, grid):
        moveset = grid.getAvailableMoves()
        best_move = None
        best_utility = float("-inf")
        alpha = float("-inf")
        beta = float("inf")

        for move in moveset:
            child = grid.clone()
            child.move(move)
            utility = self.expectiminimax(child, 3, False, alpha, beta)

            if utility > best_utility:
                best_move = move
                best_utility = utility

            alpha = max(alpha, utility)

        return best_move

    def expectiminimax(self, grid, depth, maximizing_player, alpha, beta):
        if depth == 0 or not self.areMovesAvailable(grid):
            return self.evaluate(grid)

        if maximizing_player:
            max_utility = float("-inf")
            for move in grid.getAvailableMoves():
                child = grid.clone()
                child.move(move)
                utility = self.expectiminimax(child, depth - 1, False, alpha, beta)
                max_utility = max(max_utility, utility)
                alpha = max(alpha, utility)
                if beta <= alpha:
                    break
            return max_utility
        else:
            min_utility = 0
            num_children = 0
            for cell in grid.getAvailableCells():
                child2 = grid.clone()
                child2.setCellValue(cell, 2)
                min_utility += 0.9 * self.expectiminimax(child2, depth - 1, True, alpha, beta)
                num_children += 1
                child4 = grid.clone()
                child4.setCellValue(cell, 4)
                min_utility += 0.1 * self.expectiminimax(child4, depth - 1, True, alpha, beta)
                num_children += 1
            return min_utility / num_children

    def evaluate(self, grid):
        pass

    def areMovesAvailable(self, grid):
        for move in grid.getAvailableMoves():
            return True
        return False        


            
        


    