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
# Main Algorithm
from algorithms.minimax import getBoardValue
# Predictive Algorithm
from algorithms.predictive.random_value import predictBoardValue
# Move selection
from algorithms.move_selection.random import selectMove

# Necessary imports
from constants import *
from board import Board
from ai import AI

# CHANGEABLE VARIABLES
#   Gamerule variables and others can be found in constants.py
# Seach Depth: The maximum depth to search, will use predictive functions after that
#   (set to negative one for infinite)
MAX_SEARCH_DEPTH = 4



    

# INIT
interface = Interface()
board = Board(interface.getBoard())
ai = AI(interface, getBoardValue, predictBoardValue, selectMove, positiveSeachDepth=MAX_SEARCH_DEPTH)


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

while not board.isTerminal():
    # Player
    print()
    interface.makeMove(board)
    if board.isTerminal():
        break

    # AI
    ai.makeMove(board)
    

interface.endGame(board, board.getTerminalGameState())