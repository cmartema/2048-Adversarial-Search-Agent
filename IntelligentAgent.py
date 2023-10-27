import random
from BaseAI import BaseAI
class IntelligentAgent(BaseAI): 
    def getMove(self, grid):
        # Selects a random move and returns it
        moveset = grid.getAvailableMoves()
        return random.choice(moveset) if moveset else None
    
    #Constants for directions
    ACTIONS = {
        'UP': 0,
        'DOWN': 1,
        'LEFT': 2,
        'RIGHT': 3
    }
    
    def minimize(self, state, a, b, depth):
        '''Find the child state with the lowest utility value'''
        if self.terminal_test(state) or depth == 0:
            return(None, self.evaluate(state))
        
        minChild = None 
        minUtility = float("inf")

        for child in state.children:
            _, utility = self.maximize(child, a, b, depth - 1)

            if utility < minUtility:
                minChild = child
                minUtility = utility

            if minUtility <= a:
                break
            if minUtility < b:
                b = minUtility
        return (minChild, minUtility) 

    def maximize(self, state, a, b, depth):
        '''Find the child state with the highest utility value'''
        if self.terminal_test(state) or depth == 0:
            return(None, self.evaluate(state))

        maxChild = None
        maxUtility = float("-inf")

        for child in state.children:
            _, utility = self.minimize(child, a, b, depth - 1)
            if utility > maxUtility:
                maxChild = child
                maxUtility = utility
            if maxUtility >= b:
                break
            if maxUtility > a:
                a = maxUtility
            return (maxChild, maxUtility)


            
        


    