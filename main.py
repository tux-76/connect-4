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
from game import Game

# CHANGEABLE VARIABLES
#   Gamerule variables and others can be found in constants.py
# Seach Depth: The maximum depth to search, will use predictive functions after that
#   (set to negative one for infinite)
MAX_SEARCH_DEPTH = 4



    

# INIT
user = User()
ai = AI(predictive=predictBoardValue, moveSelection=selectMove, searchDepth=5)

# Main
game = Game(Interface, Board, (user, ai))

while game.loop():
    pass

game.end()