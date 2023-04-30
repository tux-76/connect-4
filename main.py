# # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# MAIN PYTHON FILE (main.py)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# GENERAL NOTES:
# - YELLOW refers to PLAYER_MAX's spaces (and the placeholders are 1)
# - RED refers to PLAYER_MIN's spaces (placeholders for: -1)
# - The x value (m[x]) in board.matrix is the column

# IMPORTS
# Interpreter
from interface.terminal import Interface
# Algorithm
from algorithms.minimax import getBoardValue
# Move selection
from algorithms.move_selection.random import selectMove

# Necessary imports
from constants import *
from board import Board

# CHANGEABLE VARIABLES
#   Gamerule variables and others can be found in constants.py
# Seach Depth: The maximum depth to search, will use predictive functions after that
#   (set to negative one for infinite)
MAX_SEARCH_DEPTH = 4


# GET BEST MOVE: Similar to minimax, but just gets the values of all possible moves and
#   returns the coordinates of the best one
# ===============================================================================
def getBestMove(board, depth=1):
    # Get the players turn
    player = board.getTurn()

    # Get all possible moves
    moves = board.getMoves()

    # Get move values for every possible move
    moveValues = []
    for moveXY in moves:
        # Create a new board and make that move in it
        nb = board.clone()
        nb.makeMove(moveXY, nb.getTurn())
        # Get the value of that board
        moveValues.append(getBoardValue(nb, depth=depth+1))
        if DO_STATUS_PRINTS:
            print("Move Choice:", moveValues[-1])

    # if player == PLAYER_MAX:
    #     return moves[moveValues.index(max(moveValues))]
    # elif player == PLAYER_MIN:
    #     return moves[moveValues.index(min(moveValues))]
    return selectMove(moves, moveValues, player)
    

# INIT
interface = Interface()
board = Board(interface.getBoard())


# TRAP PRESET (yellow play 2)
# board.matrix=[
#     [0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 1],
#     [0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, -1],
#     [0, 0, 0, 0, 0, 0],
# ]

# interface.displayBoard(board)
# interface.updatePlayerMove(board)
# interface.displayBoard(board)

# getBestMove(board, depth=-3)
# getBoardValue(board, depth=-4)

while not board.isTerminal():
    # Player
    print()
    interface.updatePlayerMove(board)
    if board.isTerminal():
        break

    # AI
    aiMove = getBestMove(board, depth=MAX_SEARCH_DEPTH*-1)
    print("AI move selected:", aiMove[0]+1)
    board.makeMove(aiMove, board.getTurn())

interface.endGame(board, board.getTerminalGameState())