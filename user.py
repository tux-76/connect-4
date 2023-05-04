# A class for obtaining input from a source other than internal AI

class User:
    def __init__(self, interface):
        self.interface = interface

    def makeMove(self, board):
        # Show the board to the player
        self.interface.displayBoard(board)
        board.move(self.interface.getMove(board), board.getTurn())