import tkinter as tk
from elements import Element

class TurmiteGame:
    def __init__(self, master, planet_tk, grid_size=(30, 30), cell_size=20):
        self.grid_size = (30, 30)
        self.cell_size = 25
        
        self.turmite = Element.Turmite(self.grid_size, self.cell_size)
        self.master = master
        self.planet_tk = planet_tk

        self.planet_tk.canvas = tk.Canvas(master, width=self.grid_size[1] * self.cell_size, height=self.grid_size[0] * self.cell_size, bg="white")
        
        self.planet_tk.canvas.place(relx=0.5, rely=0.5, anchor='center')

        self.turmite_x, self.turmite_y = self.grid_size[0] // 2, self.grid_size[1] // 2
        self.turmite_direction = 0

        self.cells = [[0 for _ in range(self.grid_size[1])] for _ in range(self.grid_size[0])]

        self.draw_initial_grid()
        self.ant_rect = None

    def draw_initial_grid(self):
        for x in range(self.grid_size[0]):
            for y in range(self.grid_size[1]):
                self.planet_tk.canvas.create_rectangle(
                    y * self.cell_size, x * self.cell_size,
                    (y + 1) * self.cell_size, (x + 1) * self.cell_size,
                    outline="grey", fill="white"
                )

    def start_game(self):
        self.update()

    def update(self):
        if not hasattr(self.planet_tk, 'canvas') or not self.planet_tk.canvas.winfo_exists():
            return

        for _ in range(10):
            old_x, old_y = self.turmite_x, self.turmite_y
            current_state = self.cells[self.turmite_x][self.turmite_y]

            if current_state == 0:
                self.turmite_direction = (self.turmite_direction + 1) % 4
                self.cells[self.turmite_x][self.turmite_y] = 1
                couleur = "black"
            else:
                self.turmite_direction = (self.turmite_direction - 1) % 4
                self.cells[self.turmite_x][self.turmite_y] = 0
                couleur = "white"

            self.planet_tk.canvas.create_rectangle(
                old_y * self.cell_size, old_x * self.cell_size,
                (old_y + 1) * self.cell_size, (old_x + 1) * self.cell_size,
                outline="grey", fill=couleur
            )

            if self.turmite_direction == 0:
                self.turmite_x = (self.turmite_x - 1) % self.grid_size[0]
            elif self.turmite_direction == 1:
                self.turmite_y = (self.turmite_y + 1) % self.grid_size[1]
            elif self.turmite_direction == 2:
                self.turmite_x = (self.turmite_x + 1) % self.grid_size[0]
            elif self.turmite_direction == 3:
                self.turmite_y = (self.turmite_y - 1) % self.grid_size[1]

        if self.ant_rect:
            self.planet_tk.canvas.delete(self.ant_rect)

        self.ant_rect = self.planet_tk.canvas.create_rectangle(
            self.turmite_y * self.cell_size, self.turmite_x * self.cell_size,
            (self.turmite_y + 1) * self.cell_size, (self.turmite_x + 1) * self.cell_size,
            outline="grey", fill="red"
        )

        self.planet_tk.canvas.after(40, self.update)