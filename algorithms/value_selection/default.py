# DEFAULT VALUE SELECTIOn
# Selects the max value if player is max or minimum value if not
from constants import PLAYER_MAX
def selectTopMoveValue(moveValues, player):
    return max(moveValues) if player == PLAYER_MAX else min(moveValues)