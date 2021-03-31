# object to represent game board, grid containing all cells.

from src.Cell import Cell

class Board:

    virtual_grid = {}

    def __init__(self, columns, rows, mines):
        self.columns = columns
        self.rows = rows
        self.mines = mines
        self.hidden_cells = columns * rows

        # fill our grid with hidden cells.
        for x in range(self.columns):
            for y in range(self.rows):
                cell = Cell(x, y, Config.CELL_HIDDEN)
                self.virtual_grid[cell.name] = cell

    def start(self, immune_cell):

        # get all the neighbours of the first cell.
        # they are all also immune from being mines.
        immune_cells = self.virtual_grid[immune_cell].neighbours
        immune_cells.append(immune_cell)

        def random_cell():
            rand_x = random.randint(0, self.columns - 1)
            rand_y = random.randint(0, self.rows - 1)
            return self.get_cell_from_xy(rand_x, rand_y)

            # now lets randomly place the mines.
        for i in range(self.mines):
            rand_cell = random_cell()

            # if this cell is already a mine, or immune, get another random cell
            while rand_cell.has_state(Config.CELL_MINE) or rand_cell.name in immune_cells:
                rand_cell = random_cell()

            rand_cell.add_state(Config.CELL_MINE)

    def get_cell_from_name(self, name):
        if name in self.virtual_grid:
            return self.virtual_grid[name]
        else:
            return None

    def get_cell_from_xy(self, x, y):
        return self.get_cell_from_name(Cell.create_name(x, y))

