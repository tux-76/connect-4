# A class for obtaining input from a source other than internal AI

class User:
    def __init__(self, interface, allowSkip=True):
        self.interface = interface
        self.allowSkip = allowSkip

    def makeMove(self, board):
        # Show the board to the player
        self.interface.displayBoard(board)
        success = False
        while not success:
            move = self.interface.getMove(board)
            if not (move == None and self.allowSkip):
                board.move(move, board.getTurn())
                success = True
            else:
                print("! Skipping user input !")
                success = True