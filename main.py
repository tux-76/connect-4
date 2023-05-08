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
from algorithms.predictive.openConnectLengths import predictBoardValue as predictByConnect
from algorithms.predictive.none import predictBoardValue as noPredict
# Move selection
from algorithms.move_selection.default import selectMove

# Necessary imports
from constants import *
from board import Board
from ai import AI
from user import User
from game import Game


    

# INIT
user = User()
ai = AI(predictive=predictByConnect, searchDepth=5, doShortcuts=True)
ai2 = AI(predictive=noPredict, searchDepth=5, doShortcuts=True)

# Main
game = Game(Interface, Board, (user, ai))

while game.loop():
    pass

game.end()