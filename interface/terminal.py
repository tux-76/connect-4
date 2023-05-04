from constants import *
from termcolor import colored

# CHAR_SPACE_LIST = ['-', '0', '@']
# CHAR_SPACE_LIST = ['-', 'Y', 'R']
CHAR_SPACE_LIST = ['-', colored("o", "yellow"), colored("o", "red")]

TITLE_GAME_OVER_LIST = ["Game Draw", colored("YELLOW", "yellow")+" WIN", colored("RED", "red")+" WIN"]

# Display Board
class Interface():
    # Get the original board, for terminal it is just blank
    def getBoard(self):
        matrix = []
        for col in range(BOARD_COLUMNS):
            matrix.append([])
            for row in range(BOARD_ROWS):
                matrix[col].append(SPACE_BLANK)
        return matrix
    
    # Gets the move from the user
    def getMove(self, board):
        userMove = None
        success = False
        while not success:
            # Get valid input
            validInput = False
            while not validInput:
                # Get user move
                userMoveX = input("Make move by column number:")
                if userMoveX.isnumeric():
                    userMoveX = int(userMoveX) - 1
                    validInput = True
                elif userMoveX == "":
                    print("! No user input given !")
                    return 0
                else:
                    print("Please try again...")
            # Get valid moves
            validMoves = board.getMoves()
            # Loop through the valid moves to see if one matches our input
            for validMoveXY in validMoves:
                x, y = validMoveXY
                # If the x of this move fits our inputted column
                if x == userMoveX:
                    userMove = validMoveXY
                    success = True
                    break
            if success == False:
                print("That move can not be played...")
        
        return userMove


    def updateAIMove(self, aiMove):
        print("AI Selected:", aiMove[0]+1)
    
    # Display the board
    def displayBoard(self, board, lineStart="", end="\n"):
        m = board.matrix
        print()
        # Header
        for colInd in range(len(m)):
            print(str(colInd+1)+" ", end="")
        print()
        # Board
        # For every row
        for y in range(len(m[0])):
            print(lineStart, end="")
            for x in range(len(m)):
                print(CHAR_SPACE_LIST[SPACE_LIST.index( m[x][y] )], end=" ")
            print()
        print(end, end="")
    
    # Print end game things
    def endGame(self, board, gameState):
        print()
        self.displayBoard(board)
        print("GAME OVER")
        print(TITLE_GAME_OVER_LIST[gameState])