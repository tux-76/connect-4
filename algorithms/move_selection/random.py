# # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Random value selection
# # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Chooses a random move if there are multiple best moves
import random
from constants import PLAYER_MAX
def selectMove(moves, moveValues, player):
    # Get the best possible move value for the player
    bestValue = max(moveValues) if player == PLAYER_MAX else min(moveValues)
    # Get the indices of all moves that have that value
    bestValueIndices = [i for i, value in enumerate(moveValues) if value == bestValue]
    # Return the move that corresponds to a random one of those indices
    return moves[bestValueIndices[random.randint(0, len(bestValueIndices)-1)]]
