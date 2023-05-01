# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# MINIMAX algorithm
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Predictive function
from .predictive.none import predictBoardValue
# Value Selection function
from .value_selection.decay import selectTopMoveValue

from constants import *
from board import Board

# Statistics
stat_cycles = 0



# MINIMAX FUNCTION (recursive)
# DESCRIPTION: Gets the gamestate of the board inputted
# GAMESTATE: A number from -1 to 1 representing the outcome of the board if both players play optimaly
# SPECIAL ARGS:
# - depth: if is a natural number, simply keeps track of the current depth
#     - MAX DEPTH: to set max depth, set depth to the negative of the max depth,
#         once max depth is reached will call prediction function
def getBoardValue(board, depth=1):
    # Update statistics
    global stat_cycles
    stat_cycles = stat_cycles + 1

    # Set necessary varaibles
    # Set player and move choosing function
    player = board.getTurn()

    # Check if the board is at a terminal status (game over)
    # Get the state
    state = board.getTerminalGameState()
    # If game over
    if state != None:
        return state

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
        if depth != 0:
            # Run minimax function
            moveValues.append(getBoardValue(nb, depth=depth+1))
        else: # We cannot go further because of depth limitations
            # Get the state of the game
            terminalGameState = board.getTerminalGameState()
            if terminalGameState != None:
                moreValues.append(terminalGameState)
            else:
                # Do predictive algorithm (none)
                moveValues.append(predictBoardValue(nb))
    
    return selectTopMoveValue(moveValues, player)

