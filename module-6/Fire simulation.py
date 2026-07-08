"""Forest Fire Sim, modified by Sue Sampson, based on a program by Al Sweigart
A simulation of wildfires spreading in a forest. Press Ctrl-C to stop.
Inspired by Nicky Case's Emoji Sim http://ncase.me/simulating/model/
** use spaces, not indentation to modify **
Tags: short, bext, simulation"""

import random, sys, time

try:
    import bext
except ImportError:
    print('This program requires the bext module, which you')
    print('can install by following the instructions at')
    print('https://pypi.org/project/Bext/')
    sys.exit()

# Set up the constants:
WIDTH = 79
HEIGHT = 22

TREE = 'A'
FIRE = '@'
EMPTY = ' '
WATER = '~'  # Module 6: Lake cells
# ==========================================================
# Module 6 TODO completed (Timothy Martin)
# ----------------------------------------------------------
# ==========================================================
# Module 6 completed
# Added the WATER constant (~) for the permanent lake.
# Water will be displayed in blue and acts as a firebreak.
# ==========================================================

# (!) Try changing these settings to anything between 0.0 and 1.0:
INITIAL_TREE_DENSITY = 0.20  # Amount of forest that starts with trees.
GROW_CHANCE = 0.02  # Chance a blank space turns into a tree.
FIRE_CHANCE = 0.02  # Chance a tree is hit by lightning & burns.

# (!) Try setting the pause length to 1.0 or 0.0:
PAUSE_LENGTH = 1.0


def main():
    forest = createNewForest()
    # # Module 6 TODO completed (Wendy Bronson)
    # Call createLake() immediately after the forest is initialized.
    # Keeping the lake creation in its own function makes the code
    # easier to read, maintain, and update later. This follows the
    # ideas from The Pragmatic Programmer about separating
    # responsibilities and writing code that is easier to change.
    createLake(forest)  # Module 6: Add the lake before the simulation starts.
    # ======================================================
    # Module 6 TODO COMPLETED (Wendy Bronson)
    # ------------------------------------------------------

    # # Lake creation is called after the forest is initialized.
    # See comments above for implementation details.
    # ======================================================
    bext.clear()

    while True:  # Main program loop.
        displayForest(forest)

        # Run a single simulation step:
        nextForest = {'width': forest['width'],
                      'height': forest['height']}

        for x in range(forest['width']):
            for y in range(forest['height']):
                if (x, y) in nextForest:
                    # If we've already set nextForest[(x, y)] on a
                    # previous iteration, just do nothing here:
                    continue
                # ==================================================
                # Module 6 TODO completed (Roxanne Buenaventura)
                # Check if the current location contains WATER.
                # If so:
                # Copy the water directly into nextForest.
                # Do NOT allow water to become fire.
                # Skip all remaining fire logic.
                # This matches the revised flowchart decision:
                # "Is location water (~)?"
                # ==================================================
                if ((forest[(x, y)] == WATER)):
                    # Copy the water directly into nextForest.
                    nextForest[(x, y)] = WATER
                    continue  # Skip all remaining fire logic.
                if ((forest[(x, y)] == EMPTY)
                        and (random.random() <= GROW_CHANCE)):
                    # Grow a tree in this empty space.
                    nextForest[(x, y)] = TREE
                elif ((forest[(x, y)] == TREE)
                      and (random.random() <= FIRE_CHANCE)):
                    # Lightning sets this tree on fire.
                    nextForest[(x, y)] = FIRE
                elif forest[(x, y)] == FIRE:
                    # ==================================================
                    # Module 6 TODO completed (Roxanne Buenaventura)
                    # Modify the fire spread logic so that fire cannot
                    # spread into or across WATER cells.
                    # Neighbor checks should ignore lake locations.
                    # ==================================================
                    # This tree is currently burning.
                    # Loop through all the neighboring spaces:
                    for ix in range(-1, 2):
                        for iy in range(-1, 2):
                            # Ignore  water cells when checking for fire spread.
                            if forest.get((x + ix, y + iy)) == WATER:
                                continue  # Skip water cells.
                            # Fire spreads to neighboring trees:
                            if forest.get((x + ix, y + iy)) == TREE:
                                nextForest[(x + ix, y + iy)] = FIRE
                    # The tree has burned down now, so erase it:
                    nextForest[(x, y)] = EMPTY
                else:
                    # Just copy the existing object:
                    nextForest[(x, y)] = forest[(x, y)]
        forest = nextForest

        time.sleep(PAUSE_LENGTH)


def createNewForest():
    """Returns a dictionary for a new forest data structure."""
    forest = {'width': WIDTH, 'height': HEIGHT}
    for x in range(WIDTH):
        for y in range(HEIGHT):
            if (random.random() * 100) <= INITIAL_TREE_DENSITY:
                forest[(x, y)] = TREE  # Start as a tree.
            else:
                forest[(x, y)] = EMPTY  # Start as an empty space.
    return forest


# ======================================================
# Module 6 TODO completed (Timothy Martin)
# ------------------------------------------------------
# dded the createLake() function, which creates a permanent
# rectangular lake near the center of the forest.
# The lake overwrites any trees or empty spaces and serves
# as a firebreak.
# ======================================================

def createLake(forest):
    """Creates a lake roughly in the center of the forest."""
    centerX = WIDTH // 2
    centerY = HEIGHT // 2
    # Create an 11 x 5 rectangular lake.
    for x in range(centerX - 5, centerX + 6):
        for y in range(centerY - 2, centerY + 3):
            forest[(x, y)] = WATER


def displayForest(forest):
    """Display the forest data structure on the screen."""
    bext.goto(0, 0)
    for y in range(forest['height']):
        for x in range(forest['width']):

            # ==========================================================
            # Module 6 TODO completed (Wendy Bronson)
            # ----------------------------------------------------------
            # Display WATER cells in blue so they are visually different
            # from trees and fire. Keeping each terrain type in its own
            # display case improves readability and makes the code easier
            # to maintain.
            # ==========================================================
            if forest[(x, y)] == TREE:
                bext.fg('green')
                print(TREE, end='')
            elif forest[(x, y)] == FIRE:
                bext.fg('red')
                print(FIRE, end='')
            elif forest[(x, y)] == WATER:
                bext.fg('blue')
                print(WATER, end='')
            elif forest[(x, y)] == EMPTY:
                print(EMPTY, end='')
        print()
    bext.fg('reset')  # Use the default font color.
    print('Grow chance: {}%  '.format(GROW_CHANCE * 100), end='')
    print('Lightning chance: {}%  '.format(FIRE_CHANCE * 100), end='')
    print('Press Ctrl-C to quit.')


# If this program was run (instead of imported), run the game:
# ==========================================================
# Module 6 Planned Changes
# 1. Add a WATER (~) feature displayed in blue.
# 2. Place the lake roughly in the center of the forest.
# 3. Water cells become permanent terrain.
# 4. Water cannot ignite or burn.
# 5. Fire cannot spread into or across lake cells.
# 6. Update display logic to render water in blue.
# These planned modifications correspond to the revised
# Module 6 flowchart.
# ==========================================================
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()  # When Ctrl-C is pressed, end the program.