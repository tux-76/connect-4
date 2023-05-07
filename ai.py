import time

from constants import *


# Main Algorithm
from algorithms.minimax import Minimax
# Prediction function
from algorithms.predictive.none import predictBoardValue
# Move selection
from algorithms.move_selection.random import selectMove
# Value Assignment
from algorithms.value_assignment.default import assignTotalValue

class AI:
    def __init__(self, interface=None, mainAlgorithm=Minimax, predictive=predictBoardValue, moveSelection=selectMove, valueAssignment=assignTotalValue, searchDepth=4, doShortcuts=False):
        self.main = mainAlgorithm(predictive, valueAssignment)
        self.selectMove = moveSelection
        self.searchDepth = searchDepth
        self.interface = interface
        self.doShortcuts = doShortcuts

    
    # GET BEST MOVE: Similar to minimax, but just gets the values of all possible moves and
    #   returns the coordinates of the best one
    # ===============================================================================
    def getMove(self, board):
        # Do time stats
        time_start = time.time()

        # Get the players turn
        player = board.getTurn()

        # Get all possible moves
        moves = board.getMoves()

        # Get move values for every possible move
        moveValues = []
        for moveXY in moves:
            # Create a new board and make that move in it
            nb = board.clone()
            nb.move(moveXY, nb.getTurn())
            # Get the value of that board
            nbValue = self.main.getBoardValue(nb, depth=self.searchDepth-1)
            moveValues.append(nbValue)
            if DO_DEBUG:
                print("Move Choice:", moveValues[-1])
            # Check if the nbValue is already the best move for player
            if nbValue == player and self.doShortcuts:
                break

        time_elapsed = time.time() - time_start
        print("Approx. time ellapsed:", time_elapsed)
        board.printTime()
        return self.selectMove(moves, moveValues, player)
    
    # Make move (get move but actually does the move)
    def makeMove(self, board):
        self.interface.displayBoard(board)
        aiMove = self.getMove(board)
        board.move(aiMove, board.getTurn())
        self.interface.updateAIMove(aiMove)
        return aiMove