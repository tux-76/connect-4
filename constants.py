# CONSTANTS
# # # # # # # # # # 
BOARD_COLUMNS = 7
BOARD_ROWS = 6

# connect numbers will start at 1 (for a single space)
WIN_CONNECT_NUM = 4

# PLACEHOLDERS
# # # # # # # # # # # # # 
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
STATE_LIST = [STATE_DRAW, STATE_WIN1, STATE_WIN2]

# DIRECTIONS FOR SEARCHING
# Direction links
DIR_UPRIGHT = 0
DIR_RIGHT = 1
DIR_DOWNRIGHT = 2
DIR_DOWN = 3
# Translation: for the DIR indexes, these show the x and y values that are moved in that
#   direction
DIR_TRANS_X = (1,  1, 1, 0)
DIR_TRANS_Y = (-1, 0, 1, 1)