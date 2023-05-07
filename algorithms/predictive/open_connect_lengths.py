# OPEN CONNECT LENGTHS
# 
# Predicts based on the amount of open connect possiblilities

from constants import *
import math

# The range from -r to r of the output
SIGMOID_RANGE = 0.75
BLANK_WEIGHT = 0.25
SPACE_WEIGHT = 1

def predictBoardValue(board):
    totalValue = 0

    # For every connection column
    for connectColXYs in board.directional[DIR_UP_DIAGONAL]+board.directional[DIR_DOWN_DIAGONAL]+board.directional[DIR_HORIZONTAL]:
        # If the column has enough of one color to make a connect
        if len(connectColXYs) >= WIN_CONNECT_NUM:
            # print(connectColXYs)
            runningValue = 0
            blankValue = 0
            currentColor = 0
            for spaceXY in connectColXYs:
                space = board.matrix[spaceXY[0]][spaceXY[1]]
                if space == SPACE_BLANK:
                    # Check the one below
                    if board.getSpace(spaceXY[0], spaceXY[1]-1) in (SPACE_YELLOW, SPACE_RED, None):
                        blankValue = blankValue + BLANK_WEIGHT
                else:
                    if space != currentColor:
                        # Add it to the total value (multiply by player, which is either -1 or 1)
                        totalValue = totalValue + (runningValue + blankValue) * currentColor
                        # Reset everything
                        runningValue = 0
                        blankValue = 0
                        currentColor = space
                    runningValue = runningValue + SPACE_WEIGHT
                        
    # Get sigmoid value
    return (1 / (1 + math.exp(totalValue*-1))) * 2 * SIGMOID_RANGE - SIGMOID_RANGE