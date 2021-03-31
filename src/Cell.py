
'''
Object to represent a cell within the mine grid.
Type of cell and neighbours.
'''

class Cell:

    neighbours = {}

    # cell co-ordinates are stored as their x and y position.
    def __init__(self, x, y, state):
        self.name = self.create_name(x, y)
        self.x = x
        self.y = y
        self.state = state

    def has_state(self, state):
        return True if self.state & state else False

    def modify_state(self, state):
        self.state = state

    def add_state(self, state):
        self.modify_state(self.state | state)

    def del_state(self, state):
        self.modify_state(self.state & ~state)

    @property
    def neighbours(self):
        x = self.x
        y = self.y

        return [
            self.create_name(x, y - 1), # N - north neighbour
            self.create_name(x + 1, y - 1), # NE
            self.create_name(x + 1, y), # E
            self.create_name(x + 1, y + 1), # SE
            self.create_name(x, y + 1), # S
            self.create_name(x - 1, y + 1), # SW
            self.create_name(x - 1, y), # W
            self.create_name(x - 1, y - 1) # NW
        ]

    @staticmethod
    def create_name(x, y):
        return f'x{x}y{y}'