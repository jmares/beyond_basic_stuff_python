"""Four-in-a-Row, by Al Sweigart al@inventwithpython.com
A tile-dropping game to get four-in-a-row, similar to Connect Four."""

import sys

# Constants used for displaying the board:

EMPTY_SPACE = "."
PLAYER_X = "X"
PLAYER_O = "O"

# Note: Update BOARD_TEMPLATE & COLUMN_LABELS if BOARD_WIDTH is changed.
BOARD_WIDTH = 7
BOARD_HEIGHT = 6
COLUMN_LABELS = ("1", "2", "3", "4", "5", "6", "7")
assert len(COLUMN_LABELS) == BOARD_WIDTH

# The template string for displaying the board:
BOARD_TEMPLATE = """
     1234567
    +-------+
    |{}{}{}{}{}{}{}|
    |{}{}{}{}{}{}{}|
    |{}{}{}{}{}{}{}|
    |{}{}{}{}{}{}{}|
    |{}{}{}{}{}{}{}|
    |{}{}{}{}{}{}{}|
    +-------+"""


def get_new_board():
    """Returns a dictionary that represents a Four-in-a-Row board.

    The keys are (columnIndex, rowIndex) tuples of two integers, and the
    values are one of the "X", "O" or "." (empty space) strings."""
    board = {}
    for row_index in range(BOARD_HEIGHT):
        for column_index in range(BOARD_WIDTH):
            board[(column_index, row_index)] = EMPTY_SPACE
    return board



def display_board(board):
    """Display the board and its tiles on the screen."""

    # Prepare a list to pass to the format() string method for the board
    # template. The list holds all of the board's tiles (and empty
    # spaces) going left to right, top to bottom:
    tile_chars = []
    for row_index in range(BOARD_HEIGHT):
        for column_index in range(BOARD_WIDTH):
            tile_chars.append(board[(column_index, row_index)])
    # Display the board
    print(BOARD_TEMPLATE.format(*tile_chars))


def get_player_move(player_tile, board):
    """Let a player select a column on the board to drop a tile into.

    Returns a tuple of the (column, row) that the tile falls into."""
    while True:    # Keep asking player until they enter a valid row
        print(f"Player {player_tile}, enter 1 to {BOARD_WIDTH} or QUIT:")
        response = input("> ").upper().strip()

        if response == "QUIT":
            print("Thanks for playing!")
            sys.exit()

        if response not in COLUMN_LABELS:
            print(f"Enter a number from 1 to {BOARD_WIDTH}.")
            continue

        column_index = int(response) - 1     # -1 for 0-based column indexes

        # If the column is full, ask for a move again:
        if board[(column_index, 0)] != EMPTY_SPACE:
            print("That column is full, select another one.")
            continue

        # Starting from the bottom find the first empty space
        for row_index in range(BOARD_HEIGHT - 1, -1, -1):
            if board[(column_index, row_index)] == EMPTY_SPACE:
                return (column_index, row_index)


def is_full(board):
    """Returns True if the `board` has no empty spaces, otherwise
    returns False."""
    for row_index in range(BOARD_HEIGHT):
        for column_index in range(BOARD_WIDTH):
            if board[(column_index, row_index)] == EMPTY_SPACE:
                return False
    return True


def is_winner(player_tile, board):
    """Returns True if `player_tile` has four tiles in a row on `board`,
    otherwise returns False."""
    
    # Go through the entire board, checking for four in a row
    for column_index in range(BOARD_WIDTH - 3):
        for row_index in range(BOARD_HEIGHT):
            # Check for four in a row going across to the right:
            tile1 = board[(column_index, row_index)]
            tile2 = board[(column_index + 1, row_index)]
            tile3 = board[(column_index + 2, row_index)]
            tile4 = board[(column_index + 3, row_index)]
            if tile1 == tile2 == tile3 == tile4 == player_tile:
                return True
    
    for column_index in range(BOARD_WIDTH):
        for row_index in range(BOARD_HEIGHT - 3):
            # Check for four in a row going down:
            tile1 = board[(column_index, row_index)]
            tile2 = board[(column_index, row_index + 1)]
            tile3 = board[(column_index, row_index + 2)]
            tile4 = board[(column_index, row_index + 3)]
            if tile1 == tile2 == tile3 == tile4 == player_tile:
                return True
    
    for column_index in range(BOARD_WIDTH - 3):
        for row_index in range(BOARD_HEIGHT - 3):
            # Check for four in a row going righ down diagonal
            tile1 = board[(column_index, row_index)]
            tile2 = board[(column_index + 1, row_index + 1)]
            tile3 = board[(column_index + 2, row_index + 2)]
            tile4 = board[(column_index + 3, row_index + 3)]
            if tile1 == tile2 == tile3 == tile4 == player_tile:
                return True

            # Check for four in a row going left down diagonal
            tile1 = board[(column_index + 3, row_index)]
            tile2 = board[(column_index + 2, row_index + 1)]
            tile3 = board[(column_index + 1, row_index + 2)]
            tile4 = board[(column_index, row_index + 3)]
            if tile1 == tile2 == tile3 == tile4 == player_tile:
                return True

    return False


def main():
    """Runs a single game of Four-in-a-Row."""
    print(
        """Four-in-a-Row, by Al Sweigart al@inventwithpython.com

Two players take turns dropping tiles into one of seven columns, trying
to make Four-in-a-Row horizontally, vertically, or diagonally.
""")

    # Set up a new game
    game_board = get_new_board()
    player_turn = PLAYER_X

    while True:
        # Display the board and get the player's move
        display_board(game_board)
        player_move = get_player_move(player_turn, game_board)
        game_board[player_move] = player_turn

        # Check for a win or tie
        if is_winner(player_turn, game_board):
            display_board(game_board)
            print("Player {} has won!".format(player_turn))
            sys.exit()
        elif is_full(game_board):
            display_board(game_board)
            print("There is a tie!")
            sys.exit()

        # switch turns to the other player
        if player_turn == PLAYER_X:
            player_turn = PLAYER_O
        elif player_turn == PLAYER_O:
            player_turn = PLAYER_X


# If this program was run (instead of imported), run the game:
if __name__ == "__main__":
    main()
