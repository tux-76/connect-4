from constants import *

class AI:
    def __init__(self, interface, mainAlgorithm, predictiveFunction, moveSelectionFunction, positiveSeachDepth=4):
        self.main = mainAlgorithm
        self.predictive = predictiveFunction
        self.selectMove = moveSelectionFunction
        # It's weird, but minimax will add to the running depth until it reaches 0, so thats why negative
        self.searchDepth = positiveSeachDepth*-1
        self.interface = interface

    
    # GET BEST MOVE: Similar to minimax, but just gets the values of all possible moves and
    #   returns the coordinates of the best one
    # ===============================================================================
    def getMove(self, board):
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
            moveValues.append(self.main(nb, depth=self.searchDepth+1))
            if DO_STATUS_PRINTS:
                print("Move Choice:", moveValues[-1])

        # if player == PLAYER_MAX:
        #     return moves[moveValues.index(max(moveValues))]
        # elif player == PLAYER_MIN:
        #     return moves[moveValues.index(min(moveValues))]
        return self.selectMove(moves, moveValues, player)
    
    # Make move (get move but actually does the move)
    def makeMove(self, board):
        aiMove = self.getMove(board)
        board.move(aiMove, board.getTurn())
        self.interface.updateAIMove(aiMove)