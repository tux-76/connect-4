# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# MINIMAX algorithm
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

from constants import *
from board import Board

# Statistics
stat_cycles = 0



# MINIMAX CLASS (recursive)
# DESCRIPTION: Gets the gamestate of the board inputted
# GAMESTATE: A number from -1 to 1 representing the outcome of the board if both players play optimaly
class Minimax():
    def __init__(self, predictiveFunction, valueAssignmentFunction):
        self.predictBoardValue = predictiveFunction
        self.assignTotalValue = valueAssignmentFunction

    # MAIN FUNCTION
    def getBoardValue(self, board, depth=5):
        # Update statistics
        global stat_cycles
        stat_cycles = stat_cycles + 1

        # Set necessary varaibles
        # Set player and move choosing function
        player = board.getTurn()

        # Check if the board is at a terminal status (game over)
        # Get the state
        state = board.getGameState()
        # If game over
        if state != None:
            return state
        
        # Check if the 
        if depth == 0:
            return self.predictBoardValue(board)
            
        # BEGIN CRAWLING
        # Get all possible moves
        moves = board.getMoves()

        # Get move values for every possible move
        moveValues = []
        for moveXY in moves:
            # Create a new board and make that move in it
            nb = board.clone()
            nb.move(moveXY, nb.getTurn())

            # Do statistical prints
            if DO_DEBUG:
                if stat_cycles % 100 == 0:
                    print(".", end="")

            #   Run this function again on the new board with +1 depth
            nbValue = self.getBoardValue(nb, depth=depth-1)
            moveValues.append(nbValue)
            
            # Check if the nbValue is already the best move for player
            if nbValue == player:
                break
        
        return self.assignTotalValue(moveValues, player)

