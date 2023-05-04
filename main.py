# # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# MAIN PYTHON FILE (main.py)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# GENERAL NOTES:
# - YELLOW refers to PLAYER_MAX's spaces (and the placeholders are 1)
# - RED refers to PLAYER_MIN's spaces (placeholders for: -1)
# - The x value (m[x]) in board.matrix is the column

# CUSTOMIZABLE FUNCTION IMPORTS
#   Note: These are not all the functions, there is a default selection in ai.py
# Interpreter
from interface.terminal import Interface
# Prediction function
from algorithms.predictive.none import predictBoardValue
# Move selection
from algorithms.move_selection.random import selectMove

# Necessary imports
from constants import *
from board import Board
from ai import AI
from user import User

# CHANGEABLE VARIABLES
#   Gamerule variables and others can be found in constants.py
# Seach Depth: The maximum depth to search, will use predictive functions after that
#   (set to negative one for infinite)
MAX_SEARCH_DEPTH = 4



    

# INIT
interface = Interface()
board = Board(interface.getBoard())
user = User(interface)
ai = AI(interface=interface, predictive=predictBoardValue, moveSelection=selectMove, searchDepth=4)
# ai2 = AI(interface=interface, mainAlgorithm=minimax, predictive=predictBoardValue, moveSelection=selectMove, searchDepth=4)

while not board.isTerminal():

    # Player
    user.makeMove(board)
    # ai2.makeMove(board)
    # interface.displayBoard(board)


    # Check
    if board.isTerminal():
        break

    # AI
    ai.makeMove(board)
    

interface.endGame(board, board.getTerminalGameState())