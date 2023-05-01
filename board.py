# # # # # # # # # # # # # # # # # # # # # # # # 
# BASE BOARD CLASS (board.py)
# # # # # # # # # # # # # # # # # # # # # # # # 

# Imports
from constants import *
from copy import deepcopy

# BOARD CLASS
# Board structure [col][row] OR [x][y]
class Board:
    def __init__ (self, boardMatrix):
        self.matrix = boardMatrix

    # Clone => new Board: Clones the current board
    def clone(self):
        return Board(deepcopy(self.matrix))

    # On Board => Bool: determines whether a point is on the board or not
    def onBoard(self, x, y):
        return (x < BOARD_COLUMNS and x >= 0) and (y < BOARD_ROWS and y >= 0)


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

    # Find Connect => (tuple) or -1: Checks for a connect4, 
    # - if found will return the coordinates (x, y)
    # - if not found will return -1
    def findConnect(self, spaceType):
        m = self.matrix
        # hasConnect: follows the given space to see if any connect4s are attached
        def hasConnect(x, y):
            # for every direction
            for direc in range(len(DIR_TRANS_X)):
                connectNum = 0
                cx, cy = x, y # cursor variables
                # while the cursor is on the sqaure type
                while m[cx][cy] == spaceType:
                    connectNum = connectNum + 1
                    if connectNum >= WIN_CONNECT_NUM:
                        return True
                    
                    cx = cx + DIR_TRANS_X[direc]
                    cy = cy + DIR_TRANS_Y[direc]
                    if not self.onBoard(cx, cy):
                        break

            # if this point is reached without returning anything, return false
            return False

        # START        
        # loop through the matrix (all the way down then right
        for x in range(len(m)):
            for y in range(len(m[0])):
                # if the type is right
                if (m[x][y] == spaceType):
                    if hasConnect(x, y):
                        return (x, y)
        return -1


    # Is Terminal => Bool: Determines wether the game is over
    def isTerminal(self):
        return (self.findConnect(SPACE_YELLOW) != -1 or self.findConnect(SPACE_RED) != -1) or self.countSpaces(SPACE_BLANK) == 0
    
    def getTerminalGameState(self):
        if self.findConnect(SPACE_YELLOW) != -1:
            return STATE_WIN1
        elif self.findConnect(SPACE_RED) != -1:
            return STATE_WIN2
        elif self.countSpaces(SPACE_BLANK) == 0:
            return STATE_DRAW
        else:
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