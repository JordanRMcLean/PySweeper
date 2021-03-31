# object to represent active game.

import random
from datetime import datetime

import src.config as Config
from src.Board import Board


class Game:

    started = False
    finished = False
    start_time = 0
    finish_time = 0
    board = None

    # cell co-ords are
    def __init__(self, columns, rows, mines):
        self.columns = columns
        self.rows = rows
        self.mines = mines
        self.start_time = 0

        self.mines_left = mines
        self.cells_left = (columns * rows) - mines

    # the game only starts when clicking first cell.
    # additionally the first cell must not be a mine and open up some play.
    def start(self, first_cell):
        self.started = True
        self.start_time = datetime.now()
        self.board = Board(self.columns, self.rows, self.mines)


    def finish(self, lost):
        self.finished = True
        self.finish_time = datetime.now()

        # reveal all other cells.

        # finish time.

        if lost:
            self.lost()
        else:
            self.won()

    def lost(self):
        return
        # reveal all other cells

        # highlight incorrectly flagged mines

    def won(self):
        return
        # check if finish time is a hi score.
        # update UI

    def flag_cell(self):
        return

    def click_cell(self):
        return