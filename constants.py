# VARIABLES
# # # # # # # # # # 
BOARD_COLUMNS = 7
BOARD_ROWS = 6

# connect numbers will start at 1 (for a single space)
WIN_CONNECT_NUM = 4

# Do status prints?
DO_STATUS_PRINTS = True


# PLACEHOLDERS
# # # # # # # # # # # # # 
# Note: It is crucial that player1's value stays tied to yellow and vice-versa
# PLAYERS
PLAYER_MAX = 1
PLAYER_MIN = -1

# SPACES
SPACE_BLANK = 0
SPACE_YELLOW = 1
SPACE_RED = -1
SPACE_LIST = [SPACE_BLANK, SPACE_YELLOW, SPACE_RED]

# GAME STATES
STATE_WIN1 = 1
STATE_WIN2 = -1
STATE_DRAW = 0

# DIRECTIONS FOR SEARCHING
DIR_UP_DIAGONAL = 0
DIR_HORIZONTAL = 1
DIR_DOWN_DIAGONAL = 2
DIR_VERTICAL = 3
# Translation: for the DIR indexes, these show the x and y values that are moved in that
#   direction
DIR_TRANS_X = (1,  1, 1, 0)
DIR_TRANS_Y = (-1, 0, 1, 1)