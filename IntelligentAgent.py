import random
from BaseAI import BaseAI
class IntelligentAgent(BaseAI): 
    def getMove(self, grid):   
        best_move = None
        best_utility = float("-inf")
        alpha = float("-inf")
        beta = float("inf")

        for move_tuple in  grid.getAvailableMoves():
            move = move_tuple[0]
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
            expected_utility = 0.0
            num_children = 0
            for cell in grid.getAvailableCells():
                for tile_value, probability in [(2, 0.9), (4, 0.1)]:
                    child = grid.clone()
                    child.setCellValue(cell, tile_value)
                    expected_utility += probability * self.expectiminimax(child, depth - 1, True, alpha, beta)
                    num_children += 1
                    if beta <= alpha:
                        break
            return expected_utility / num_children

    def evaluate(self, grid):
        smooth_weight = 0.1
        monotonic_weight = 1.0

        smoothness = self.calculate_smoothness(grid)
        monotonicity = self.calculate_monotonicity(grid)
        max_tile = grid.getMaxTile()
        empty_cells = len(grid.getAvailableCells())

        # Calculate the overall heuristic value
        heuristic = (
            monotonic_weight * monotonicity
            - smooth_weight * smoothness
            + max_tile
            + empty_cells
        )
        return heuristic
    
    def calculate_smoothness(self, grid):
        smoothness = 0.0
        for row in grid.map:
            smoothness += sum(abs(row[i] - row[i + 1]) for i in range(len(row) - 1))
        for col in range(len(grid.map[0])):
            smoothness += sum(abs(grid.map[row][col] - grid.map[row + 1][col]) for row in range(len(grid.map) - 1))

        # Normalize the smoothness heuristic
        smoothness /= (len(grid.map) * len(grid.map[0]) - 1)
        return smoothness  

    def calculate_monotonicity(self, grid):
        monotonicity = 0.0
        for row in grid.map:
            for i in range(len(row) - 1):
                monotonicity += abs(row[i] - row[i + 1])
        for col in range(len(grid.map[0])):
            for row in range(len(grid.map) - 1):
                monotonicity += abs(grid.map[row][col] - grid.map[row + 1][col])

        # Normalize the monotonicity heuristic
        monotonicity /= (len(grid.map) * len(grid.map[0]))
        return monotonicity

    def areMovesAvailable(self, grid):
        for move in grid.getAvailableMoves():
            return True
        return False        




            
        


    