# # # # # # # # # # # # # # # # # # # # # # # # 
# BASE BOARD CLASS (board.py)
# # # # # # # # # # # # # # # # # # # # # # # # 

# Imports
from constants import *
from copy import deepcopy
import time

time_taken = 0

# BOARD CLASS
# Board structure [col][row] OR [x][y]
class Board:
    # ===================================
    # -----------------------INITIALIZER
    # ===================================
    def __init__ (self, boardMatrix):
        # Set board matrix
        self.matrix = boardMatrix
        self.cols = len(self.matrix)
        self.rows = len(self.matrix[0])

        # SET UP DIRECTIONAL CONNECTION MATRICES
        # ===========================================
        #   (UP_DIAG, HORIZONTAL, DOWN_DIAG, VERTICAL)
        m = self.matrix
        self.directional = ([], [], [], [])
        dr = self.directional

        # ADD COLUMNS
        # Vertical: Add same amount as matrix columns
        for i in range(self.cols):
            dr[DIR_VERTICAL].append([])
        # Horizontal: Add same amount as matrix rows
        for i in range(self.rows):
            dr[DIR_HORIZONTAL].append([])
        # Diagonals: Add amount -> matrix rows + columns - 1
        for i in range(self.cols+self.rows-1):
            dr[DIR_UP_DIAGONAL].append([])
            dr[DIR_DOWN_DIAGONAL].append([])
        
        # FILL DIRECTIONAL RELATIONS
        # Loop through indexes of all elements in matrix
        for x in range(self.cols):
            for y in range(self.rows):
                # Add to Verticle
                dr[DIR_VERTICAL][x].append((x, y))
                # Add to Horizontal
                dr[DIR_HORIZONTAL][y].append((x, y))
                # Add to Down Diagonal
                dr[DIR_DOWN_DIAGONAL][x+y].append((x, y))
                # Add to Up Diagonal
                dr[DIR_UP_DIAGONAL][x-y+self.rows-1].append((x, y))


        
    # ====================================================
    # -------------------------------------------METHODS
    # ====================================================
    # Clone => new Board: Clones the current board
    def clone(self):
        return Board(deepcopy(self.matrix))

    # On Board => Bool: determines whether a point is on the board or not
    def onBoard(self, x, y):
        return (x < BOARD_COLUMNS and x >= 0) and (y < BOARD_ROWS and y >= 0)

    def getSpace(self, x, y):
        if self.onBoard(x, y):
            return self.matrix[x][y]
        else:
            return None


    # Count Spaces => Int: Counts the number of spaces that are that type in the board
    def countSpaces(self, spaceType):
        s = 0
        for col in self.matrix:
            for space in col:
                if space == spaceType:
                    s = s + 1
        return s

    # Returns the player whos turn it is
    def getTurn(self):
        # If there's more yellow pieces than red
        if self.countSpaces(SPACE_YELLOW) > self.countSpaces(SPACE_RED):
            return PLAYER_MIN
        else:
            return PLAYER_MAX

    # GET GAME STATE: Gets the game state
    # - If an ending is not reached will return None
    # - If at an ending will return ending value
    def getGameState(self):
        global time_taken
        # Do time stats
        time_start = time.time()

        # For every direction in directional data
        for dirMatrix in self.directional:
            # For every connection column
            for connectColXYs in dirMatrix:
                # If the column has enough of one color to make a connect
                if len(connectColXYs) >= WIN_CONNECT_NUM:
                    connectNum = 0
                    currentColor = None
                    for spaceXY in connectColXYs:
                        space = self.matrix[spaceXY[0]][spaceXY[1]]
                        # BLANK: reset connect #, OCCUPIED: add to it
                        if space == SPACE_BLANK:
                            connectNum = 0
                        elif space == SPACE_YELLOW or space == SPACE_RED:
                            # If different color: reset
                            if space != currentColor:
                                currentColor = space
                                connectNum = 0
                            connectNum = connectNum + 1
                        # Check if the connectNumber is enough to win
                        if connectNum == WIN_CONNECT_NUM:
                            return space # Return the space that won

        time_taken = time_taken + time.time() - time_start
        return None



    # Get Moves => Array > (x, y): Gets the possible a player can make
    def getMoves(self):
        moves = []
        m = self.matrix
        # Loop through the columns
        for x in range(len(m)):
            # Check if a blank space is in the column
            if SPACE_BLANK in m[x]:
                # Get the coordinates for the last blank value in column
                #   Starts at the last value (length-1) and goes back as reversed index goes up
                moves.append((x, len(m[x])-1 - m[x][::-1].index(SPACE_BLANK)))
        return moves
    
    # Make Move => Void: Makes the move
    def move(self, xy, spaceType):
        x, y = xy
        self.matrix[x][y] = spaceType
    
    def printTime(self):
        global time_taken
        print("Time spent calculating state:", time_taken)
        time_taken = 0