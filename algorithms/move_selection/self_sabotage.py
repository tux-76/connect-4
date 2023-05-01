# # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# SELF SABOTAGE!!!
# # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Chooses the absolute worst value possible
from constants import PLAYER_MAX
def selectMove(moves, moveValues, player):
    return moves[moveValues.index(min(moveValues) if player == PLAYER_MAX else max(moveValues))]