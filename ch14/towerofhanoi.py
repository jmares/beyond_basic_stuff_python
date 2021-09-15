"""THE TOWER OF HANOI, by Al Sweigart al@inventwithpython.com
A stack-moving puzzle game."""

import copy
import sys
TOTAL_DISKS = 5     # More disks means a more difficult puzzle

# Start with all disk on tower A:
SOLVED_TOWER = list(range(TOTAL_DISKS, 0, -1))


def main():
    """Runs a single game of The Tower of Hanoi."""
    print("""THE TOWER OF HANOI, by Al Sweigart al@inventwithpython.com

Move the tower of disks, one disk at a time, to another tower. Larger
disks cannot rest on top of a smaller disk.

More info at https://en.wikipedia.org/wiki/Tower_of_Hanoi
""")

    """The towers dictionary has keys "A", "B", and "C" and values
    that are lists representing a tower of disks. The list contains
    integers representing disks of different sizes, and the start of
    the list is the bottom of the tower. For a game with 5 disks,
    the list [5, 4, 3, 2, 1] represents a completed tower. The blank
    list [] represents a tower of no disks. The list [1, 3] has a
    larger disk on top of a smaller disk and is an invalid
    configuration. The list [3, 1] is allowed since smaller disks
    can go on top of larger ones."""
    towers = {"A": copy.copy(SOLVED_TOWER), "B": [], "C": []}
    while True:     # Run a single turn on each iteration of this loop
        # Display the towers and disks:
        display_towers(towers)

        # As the user for a move
        from_tower, to_tower = get_player_move(towers)

        # Move the top disk from form_tower to to_tower
        disk = towers[from_tower].pop()
        towers[to_tower].append(disk)

        # Check if the user has solved the puzzle:
        if SOLVED_TOWER in (towers["B"], towers["C"]):
            display_towers(towers)     # Display the towers one last time
            print("You have solved the puzzle! Well done!")
            sys.exit()


def get_player_move(towers):
    """Asks the player for a move. Returns (fromTower, toTower)."""

    while True:   # Keep asking player until they enter a valid move.
        print('Enter the letters of "from" and "to" towers, or QUIT.')
        print("(e.g., AB to moves a disk from tower A to tower B.)")
        print()
        response = input("> ").upper().strip()

        if response == "QUIT":
            print("Thanks for playing!")
            sys.exit()

        # Make sure the user entered valid tower letters:
        if response not in ("AB", "AC", "BA", "BC", "CA", "CB"):
            print("Enter one of AB, AC, BA, BC, CA, or CB.")
            continue  # Ask player again for their move.

        # Use more descriptive variable names:
        from_tower, to_tower = response[0], response[1]

        if len(towers[from_tower]) == 0:
            # The "from" tower cannot be an empty tower:
            print("You selected a tower with no disks.")
            continue  # Ask player again for their move.
        elif len(towers[to_tower]) == 0:
            # Any disk can be moved onto an empty "to" tower:
            return from_tower, to_tower
        elif towers[to_tower][-1] < towers[from_tower][-1]:
            print("Can't put larger disks on top of smaller ones.")
            continue  # Ask player again for their move.
        else:
            # This is a valid move, so return the selected towers:
            return from_tower, to_tower


def display_towers(towers):
    """Display the three towers with their disks."""

    # Display the three towers:
    for level in range(TOTAL_DISKS, -1, -1):
        for tower in (towers["A"], towers["B"], towers["C"]):
            if level >= len(tower):
                display_disk(0)     # Display the bare pole with no disk
            else:
                display_disk(tower[level])     # Display the disk
        print()
    
    # Display the tower labels A, B and C:
    empty_space = " " * (TOTAL_DISKS)
    print("{0} A{0}{0} B{0}{0} C\n".format(empty_space))


def display_disk(width):
    """Display a disk of the given width. A width of 0 means no disk."""
    empty_space = " " * (TOTAL_DISKS - width)

    if width == 0:
        # Display a pole segment without a disk:
        print(f"{empty_space}||{empty_space}", end="")
    else:
        # Display the disk:
        disk = "@" * width
        numLabel = str(width).rjust(2, "_")
        print(f"{empty_space}{disk}{numLabel}{disk}{empty_space}", end="")


# If this program was run (instead of imported), run the game:
if __name__ == "__main__":
    main()


