# DECAY
# Same as default, but decays the value over time
from constants import PLAYER_MAX

DECAY_RATE = 0.01

def selectTopMoveValue(moveValues, player):
    return (max(moveValues) if player == PLAYER_MAX else min(moveValues))*(1-DECAY_RATE)