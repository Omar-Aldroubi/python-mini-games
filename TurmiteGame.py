import tkinter as tk
from elements import Element  # Importez Element ici



class TurmiteGame:
    def __init__(self, master,planet_tk, grid_size=(20, 20), cell_size=20):
        self.turmite = Element.Turmite(grid_size, cell_size)
        self.master = master
        self.planet_tk = planet_tk

        self.planet_tk.canvas = tk.Canvas(master, width=grid_size[1] * cell_size,height=grid_size[0] * cell_size)
        self.planet_tk.canvas.pack()

        self.grid_size = grid_size
        self.cell_size = cell_size

        self.turmite_x, self.turmite_y = self.grid_size[0] // 2, self.grid_size[1] // 2
        self.turmite_direction = 0

        self.cells = [[0 for _ in range(self.grid_size[1])] for _ in range(self.grid_size[0])]

    def start_game(self):

        self.update()

    def update(self):
        current_state = self.cells[self.turmite_x][self.turmite_y]
        if current_state == 0:
            self.turmite_direction = (self.turmite_direction + 1) % 4
            self.cells[self.turmite_x][self.turmite_y] = 1
        else:
            self.turmite_direction = (self.turmite_direction - 1) % 4
            self.cells[self.turmite_x][self.turmite_y] = 0

        if self.turmite_direction == 0:
            self.turmite_x = (self.turmite_x - 1) % self.grid_size[0]
        elif self.turmite_direction == 1:
            self.turmite_y = (self.turmite_y + 1) % self.grid_size[1]
        elif self.turmite_direction == 2:
            self.turmite_x = (self.turmite_x + 1) % self.grid_size[0]
        elif self.turmite_direction == 3:
            self.turmite_y = (self.turmite_y - 1) % self.grid_size[1]

        self.draw()

        self.planet_tk.canvas.after(100, self.update)

    def draw(self):
        self.planet_tk.canvas.delete("all")

        for x in range(self.grid_size[0]):
            for y in range(self.grid_size[1]):
                cell_color = "white" if self.cells[x][y] == 0 else "black"
                self.planet_tk.canvas.create_rectangle(
                    y * self.cell_size, x * self.cell_size,
                    (y + 1) * self.cell_size, (x + 1) * self.cell_size,
                    outline="grey", fill=cell_color
                )

        self.planet_tk.canvas.create_rectangle(
            self.turmite_y * self.cell_size, self.turmite_x * self.cell_size,
            (self.turmite_y + 1) * self.cell_size, (self.turmite_x + 1) * self.cell_size,
            outline="grey", fill="red"
        )
