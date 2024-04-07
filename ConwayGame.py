import tkinter as tk
from PlanetAlpha import Grid
import copy
from elements import Element


class ConwayGame:
    def __init__(self, master,planet_tk, grid_size=(20, 20), cell_size=20):
        self.master = master
        self.planet_tk = planet_tk
        self.grid_size = grid_size
        self.cell_size = cell_size
        self.grid = [[0] * grid_size[1] for _ in range(grid_size[0])]
        self.running = False

        self.planet_tk.canvas = tk.Canvas(master, width=grid_size[1] * cell_size,
                                height=grid_size[0] * cell_size)
        self.planet_tk.canvas.pack()

        self.planet_tk.canvas.bind('<Button-1>', self.toggle_cell)

        self.start_button = tk.Button(master, text='Start', command=self.start_game)
        self.start_button.pack(side='left')

        self.stop_button = tk.Button(master, text='Stop', command=self.stop_game)
        self.stop_button.pack(side='left')

        self.clear_button = tk.Button(master, text='Clear', command=self.clear_grid)
        self.clear_button.pack(side='left')

        self.draw_grid()

    def draw_grid(self):
        self.planet_tk.canvas.delete('all')
        for i in range(self.grid_size[0]):
            for j in range(self.grid_size[1]):
                color = 'black' if self.grid[i][j] else 'white'
                self.planet_tk.canvas.create_rectangle(j * self.cell_size, i * self.cell_size,
                                             (j + 1) * self.cell_size, (i + 1) * self.cell_size,
                                             outline='grey', fill=color)


    def toggle_cell(self, event):
        x, y = event.x // self.cell_size, event.y // self.cell_size
        self.grid[y][x] = not self.grid[y][x]
        self.draw_grid()

    def start_game(self):
        if not self.running:
            self.running = True
            self.run_game()

    def stop_game(self):
        self.running = False

    def clear_grid(self):
        self.stop_game()
        self.grid = [[0] * self.grid_size[1] for _ in range(self.grid_size[0])]
        self.draw_grid()

    def run_game(self):
        if self.running:
            self.update_grid()
            self.draw_grid()
            self.master.after(100, self.run_game)

    def update_grid(self):
        new_grid = copy.deepcopy(self.grid)
        for i in range(self.grid_size[0]):
            for j in range(self.grid_size[1]):
                live_neighbors = self.count_live_neighbors(i, j)
                if self.grid[i][j]:
                    if live_neighbors < 2 or live_neighbors > 3:
                        new_grid[i][j] = 0
                else:
                    if live_neighbors == 3:
                        new_grid[i][j] = 1
        self.grid = new_grid

    def update_game(self):
        if self.running:
            self.grid.update_conway()
            self.draw_grid()
            self.master.after(100, self.update_game)
    def count_live_neighbors(self, y, x):
        count = 0
        for i in range(max(0, y - 1), min(y + 2, self.grid_size[0])):
            for j in range(max(0, x - 1), min(x + 2, self.grid_size[1])):
                if (i, j) != (y, x):
                    count += self.grid[i][j]
        return count

