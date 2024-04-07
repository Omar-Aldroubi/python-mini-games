
class Element:
    class Snake:
        def __init__(self, grid_size, cell_size):
            self.grid_size = grid_size
            self.cell_size = cell_size
            self.snake_body = [(grid_size[0] // 2, grid_size[1] // 2)]
            self.direction = "Right"
            self.apple = self.generate_apple()
            self.rotting_apples = self.generate_rotting_apples()

        def move_snake(self):
            head_x, head_y = self.snake_body[0]
            if self.direction == "Right":
                head_y += 1
            elif self.direction == "Left":
                head_y -= 1
            elif self.direction == "Up":
                head_x -= 1
            elif self.direction == "Down":
                head_x += 1
            new_head = (head_x, head_y)
            self.snake_body.insert(0, new_head)
            self.snake_body.pop()

        def generate_apple(self):
            import random
            return (random.randint(0, self.grid_size[0] - 1), random.randint(0, self.grid_size[1] - 1))

        def generate_rotting_apples(self, count=3):
            import random
            return [(random.randint(0, self.grid_size[0] - 1), random.randint(0, self.grid_size[1] - 1)) for _ in
                    range(count)]



    class Turmite:
        def __init__(self, grid_size, cell_size):
            self.grid_size = grid_size
            self.cell_size = cell_size
            self.position = (grid_size[0] // 2, grid_size[1] // 2)
            self.direction = 0
            self.state = [[0 for _ in range(grid_size[1])] for _ in range(grid_size[0])]

        def move_turmite(self):

            pass

        def update_state(self):

            pass


    class Conway:
        class Conway:
            def __init__(self, master, planet_tk, grid_size=(20, 20), cell_size=20):
                self.master = master
                self.planet_tk = planet_tk
                self.conway = Element.Conway(grid_size)

            def start_game(self):
                self.update()

            def update(self):
                self.conway.update_grid()
                self.planet_tk.draw_conway(self.conway)
                self.master.after(100, self.update)