
# possible cell states, bitwise-flags
CELL_MINE = 1
CELL_REVEALED = 2
CELL_FLAGGED = 4
CELL_HIDDEN = 8
CELL_EMPTY = 16

    # Colours for numbered cells.
COLORS = {
    1: 'blue',
    2: 'green',
    3: 'red',
    4: 'dark-blue',
    5: 'brown',
    6: 'purple',
    7: 'dark-green',
    8: 'orange'
}

    # [height, width, mines]
DIFFICULTIES = {
    'beginner': [9, 9, 10],
    'intermediate': [16, 16, 40],
    'advanced': [16, 30, 99]
}