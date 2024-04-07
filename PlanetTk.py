import tkinter as tk
from PlanetAlpha import Grid
import copy
from elements import Element

class PlanetTk:
    def __init__(self, master,cell_size=40):
        self.master = master
        self.grid = Grid([[0] * 20 for _ in range(20)])
        self.cell_size = cell_size
        self.grid_size = [50,50]

        canvas_width = self.grid.get_columns_count() * cell_size
        canvas_height = self.grid.get_lines_count()* cell_size

        self.apple_image = tk.PhotoImage(file='./img/apple_image.png')
        self.rotting_apple_image = tk.PhotoImage(file='./img/rotting_apple_image.png')
        self.snake_head_image = tk.PhotoImage(file='./img/snake_head_image.png')

        self.snake_head_images = {
            "Up": tk.PhotoImage(file="./img/snake_head_up.png"),
            "Down": tk.PhotoImage(file="./img/snake_head_image.png"),
            "Left": tk.PhotoImage(file="./img/snake_head_ gauche.png"),
            "Right": tk.PhotoImage(file="./img/snake_head_ droite.png")
        }

    def draw(self, snake_elements, apple_position, rotting_apples_positions,direction):
        self.canvas.delete("all")
        self.background_image = tk.PhotoImage(file="./img/background_image.png")
        self.canvas.create_image(0, 0, image=self.background_image, anchor="nw")

        for row in range(self.grid.get_lines_count()):
            for col in range(self.grid.get_columns_count()):
                x1 = col * self.cell_size
                y1 = row * self.cell_size
                x2 = x1 + self.cell_size
                y2 = y1 + self.cell_size
                self.canvas.create_rectangle(x1, y1, x2, y2, outline="gray")

        for segment in snake_elements[1:]:
            x1, y1 = segment[1] * self.cell_size, segment[0] * self.cell_size
            x2, y2 = x1 + self.cell_size, y1 + self.cell_size
            self.canvas.create_rectangle(x1, y1, x2, y2, fill="green", outline="gray")

        apple_x, apple_y = apple_position[1] * self.cell_size, apple_position[0] * self.cell_size
        self.canvas.create_image(apple_x, apple_y, image=self.apple_image, anchor="nw")

        head_image = self.snake_head_images[direction]
        head_x, head_y = snake_elements[0][1] * self.cell_size, snake_elements[0][0] * self.cell_size
        self.canvas.create_image(head_x, head_y, image=head_image, anchor="nw")

        for rotting_apple in rotting_apples_positions:
            rotting_apple_x, rotting_apple_y = rotting_apple[1] * self.cell_size, rotting_apple[0] * self.cell_size
            self.canvas.create_image(rotting_apple_x, rotting_apple_y, image=self.rotting_apple_image, anchor="nw")

    def draw_conway(self, conway):
        self.canvas.delete("all")
        for i, row in enumerate(conway.grid):
            for j, cell in enumerate(row):
                color = "black" if cell == 1 else "white"
                x1, y1 = j * self.cell_size, i * self.cell_size
                x2, y2 = x1 + self.cell_size, y1 + self.cell_size
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="gray")

    def random_fill_grid(self):
        values = [0, 1]
        self.grid.fill_random(values)
        self.draw_grid()



    def draw_grid(self):
        self.canvas.delete('all')
        self.cell_size=20
        for i in range(self.grid.get_lines_count()):
            for j in range(self.grid.get_columns_count()):
                color = 'black' if self.grid.get_cell(self.grid.get_cell_number_from_coordinates(i, j)) else 'white'
                self.canvas.create_rectangle(j * self.cell_size, i * self.cell_size,
                                             (j + 1) * self.cell_size, (i + 1) * self.cell_size,
                                             outline='grey', fill=color)

    def update_grid(self):

        new_grid_values = [[0 for _ in range(self.grid_size[1])] for _ in range(self.grid_size[0])]
        for y in range(self.grid_size[0]):
            for x in range(self.grid_size[1]):
                neighbors = self.grid.get_neighborhood(y, x,
                                                       [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0),
                                                        (1, 1)], is_tore=False)
                human_neighbors = sum(neighbors)
                cell_currently_occupied = self.grid.get_cell(self.grid.get_cell_number_from_coordinates(y, x))

                if human_neighbors == 3 or (cell_currently_occupied and human_neighbors == 2):
                    new_grid_values[y][x] = 1

        Grid.set_grid(new_grid_values)












# Assurez-vous que les chemins d'accès aux images sont corrects et que la classe Grid est définie correctement.


"""
class PlanetTK:
    def __init__(self, master, cell_size=50):
        self.master = master
        self.grid = Grid([[0] * 20 for _ in range(20)])
        self.cell_size = cell_size

        canvas_width = self.grid.get_columns_count() * cell_size
        canvas_height = self.grid.get_lines_count() * cell_size

        self.canvas = tk.Canvas(master, width=canvas_width, height=canvas_height)
        self.canvas.pack()
        # Charger les images des pommes et des pommes pourries
        self.apple_image = tk.PhotoImage(file='../apple_image.png')
        self.rotting_apple_image = tk.PhotoImage(file='../rotting_apple_image.png')
        self.snake_head_image = tk.PhotoImage(file='../snake_head_image.png')

        # Charger l'image d'arrière-plan
        #self.background_image = tk.PhotoImage(file='../background_image.png')

        # Premièrement, dessiner l'arrière-plan
        #self.canvas.create_image(0, 0, image=self.background_image, anchor="nw")



    def draw(self, snake, apple, rotting_apples):
        self.canvas.delete("all")
        # Redessiner l'arrière-plan en premier
        self.canvas.create_image(0, 0, image=self.background_image, anchor="nw")

        for row in range(self.grid.get_lines_count()):
            for col in range(self.grid.get_columns_count()):
                x1 = col * self.cell_size
                y1 = row * self.cell_size
                x2 = x1 + self.cell_size
                y2 = y1 + self.cell_size
                self.canvas.create_rectangle(x1, y1, x2, y2, outline="gray")

        # Dessiner le reste du corps du serpent (si nécessaire)
        for segment in snake[1:]:
            x1 = segment[1] * self.cell_size
            y1 = segment[0] * self.cell_size
            x2 = x1 + self.cell_size
            y2 = y1 + self.cell_size
            self.canvas.create_rectangle(x1, y1, x2, y2, fill="green", outline="gray")

        # Dessiner la pomme en utilisant l'image
        apple_x, apple_y = apple[1] * self.cell_size, apple[0] * self.cell_size
        self.canvas.create_image(apple_x, apple_y, image=self.apple_image, anchor="nw")

        # Dessiner la tête du serpent avec l'image
        head_x, head_y = snake[0][1] * self.cell_size, snake[0][0] * self.cell_size
        self.canvas.create_image(head_x, head_y, image=self.snake_head_image, anchor="nw")

        # Dessiner les pommes pourries en utilisant leur image
        for rotting_apple in rotting_apples:
            rotting_apple_x, rotting_apple_y = rotting_apple[1] * self.cell_size, rotting_apple[0] * self.cell_size
            self.canvas.create_image(rotting_apple_x, rotting_apple_y, image=self.rotting_apple_image, anchor="nw")

"""

"""
    def launch_snake_game(self):
        # grid_size = (self.grid.lines_count, self.grid.columns_count)
        # Détruire le bouton de démarrage pour libérer de l'espace
        # self.start_button.destroy()
        # Initialiser SnakeGame dans la même fenêtre
        game = SnakeGame(self.master, cell_size=40)
        game.start_game()
"""