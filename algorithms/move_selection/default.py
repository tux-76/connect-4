# # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Default value selection
# # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Just chooses the first best move value
from constants import PLAYER_MAX
def selectMove(moves, moveValues, player):
    return moves[moveValues.index(max(moveValues) if player == PLAYER_MAX else min(moveValues))]