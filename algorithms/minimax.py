# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# MINIMAX algorithm
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Value Selection function
from .value_assignment.decay import assignTotalValue

from constants import *
from board import Board

# Statistics
stat_cycles = 0



# MINIMAX CLASS (recursive)
# DESCRIPTION: Gets the gamestate of the board inputted
# GAMESTATE: A number from -1 to 1 representing the outcome of the board if both players play optimaly
# SPECIAL ARGS:
# - depth: if is a natural number, simply keeps track of the current depth
#     - MAX DEPTH: to set max depth, set depth to the negative of the max depth,
#         once max depth is reached will call prediction function
class minimax():
    def __init__(self, predictiveFunction, valueAssignmentFunction, depth):
        self.predictBoardValue = predictiveFunction
        self.assignTotalValue = valueAssignmentFunction
        self.depth = depth

    # MAIN FUNCTION
    def getBoardValue(self, board, depth=4):
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
            if DO_STATUS_PRINTS:
                if stat_cycles % 100 == 0:
                    print(".", end="")

            # If the depth isn't at 0:
            #   Run this function again on the new board with +1 depth
            moveValues.append(self.getBoardValue(nb, depth=depth-1))
        
        return assignTotalValue(moveValues, player)

