import tkinter as tk
import tkinter.ttk as ttk
import src.config as Config
import src.Cell as Cell


class PySweeperUI:

    name = 'PySweeper'
    window = None

    # dict of different UI elements.
    elements = {}

    # definition of all elements within the header/footer of the UI. For easy customisation
    @property
    def header(self):
        return {
            'title': {
                'element': ttk.Label,
                'attributes': {
                    'text': self.name
                },
                'insert': lambda elem: elem.grid(row=0, column=0)
            },
            'new_game': {
                'element': ttk.Button,
                'attributes': {
                    'text': 'New Game',
                    'command': self.new_game
                },
                'insert': lambda elem: elem.grid(row=0, column=3)
            },
            'selector': {
                'element': ttk.Combobox,
                'attributes': {
                    'values': [dif.capitalize() for dif in Config.DIFFICULTIES.keys()],
                    'state': 'readonly'
                },
                'after': self.__init_difficulty
            }
        }

    @property
    def footer(self):
        return {
            'timer': {
                'element': ttk.Label,
                'attributes': {
                    'text': '00:00'
                }
            }
        }

    def __init__(self, window=None):
        if isinstance(window, tk.Tk):
            self.window = window
        else:
            self.window = tk.Tk()

        self.window.title('PySweeper')

        #import our styles in. This is done after the main window creation.
        import src.styles

        # header/footer won't be changed after init, so not storage needed.
        # main is stored for updating of grid.
        header = tk.Frame(master=self.window)
        self.main = tk.Frame(master=self.window)
        footer = tk.Frame(master=self.window)

        self.add_elements(header, self.header)
        header.grid()

        self.main.grid()

        self.add_elements(footer, self.footer)
        footer.grid()

    def add_elements(self, frame, elements):
        for name, obj in elements.items():
            element = obj.get('element')
            attributes = obj.get('attributes')
            after = obj.get('after')
            insert = obj.get('show')

            if element:
                item = element(master=frame)

                if attributes:
                    for attr, value in attributes.items():
                        item[attr] = value

                if after:
                    after(item)

                if insert:
                    insert(item)
                else:
                    item.pack()

                self.elements[name] = item

    def new_game(self):
        selector = self.get_element('selector')
        difficulty = selector.get() if selector else 'beginner'
        difficulty = difficulty.lower()
        game_specs = Config.DIFFICULTIES[difficulty]

        self.create_grid(game_specs[0], game_specs[1])

        print('Starting new game with difficulty: ' + difficulty)


    def create_grid(self, rows, columns):
        for y in range(rows):
            for x in range(columns):
                name = Cell.Cell.create_name(x, y)
                cell = ttk.Button(self.main, name = name, style = 'PyCell.TButton')
                cell.bind('<ButtonPress-1>', self.__cell_click)
                cell.bind('<ButtonPress-2>', self.__cell_flag)
                cell.grid(column=x, row=y)



    def say_hi(self, e):
        print(e)

    def get_element(self, elem):
        if elem in self.elements:
            return self.elements[elem]
        else:
            print(f'Warning: element {elem} does not exist.')
            return ttk.Label()

    # private internal functions

    def __init_difficulty(self, elem):
        elem.current(0)
       # elem.bind('<<ComboboxSelected>>', self.say_hi)

    def __cell_click(self, e):
        print('cell clicked')

    def __cell_flag(self, e):
        print('cell flagged')
