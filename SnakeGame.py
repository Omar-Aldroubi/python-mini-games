import tkinter as tk
from tkinter import PhotoImage
import random
from PlanetTk import PlanetTk
import tkinter.font as font
import time
from tkmacosx import Button
try:
    import winsound
except ImportError:
    import pygame
    pygame.mixer.init()

class SnakeGame(PlanetTk):

    def __init__(self, master, grid_size=(20, 20), cell_size=20):
        super().__init__(master, cell_size)
        self.master = master
        self.grid_size = grid_size
        self.cell_size = cell_size

        self.canvas = tk.Canvas(master, width=grid_size[1] * cell_size,height=(grid_size[0] * cell_size))

        self.canvas.place(relx=0.5, rely=0.5, anchor='center')


        self.apple_image_icon = PhotoImage(file="./img/apple_image.png")
        self.apple_icon_label = tk.Label(self.master, image=self.apple_image_icon,bg="#FFFACD")

        self.apple_icon_label.place(relx=0.36, rely=0.05, anchor='center')

        self.score = 0
        self.start_time = time.time()

        self.snake = [(grid_size[0] // 2, grid_size[1] // 2)]
        self.direction = "Right"
        self.apple = None
        self.rotting_apples = []
        self.score = 0
        self.game_over = False
        self.base_speed = 0.15
        self.speed = self.base_speed
        self.apples_eaten = 0


        self.score_label = tk.Label(self.master, text=f"Score: {self.score}", font=('Helvetica', 16),bg="#FFFACD",fg="black")

        self.score_label.place(relx=0.4, rely=0.05, anchor='center')


        self.timer_label = tk.Label(self.master, text="Time: 0s", font=('Helvetica', 16),bg="#FFFACD",fg="black")

        self.timer_label.place(relx=0.5, rely=0.05, anchor='center')


        self.music_image = PhotoImage(file="./img/speaker.png")
        self.music_button = Button(self.master, image=self.music_image, command=self.toggle_music, highlightbackground='black', bg='#FFFACD', fg='black')
        self.music_button.place(relx=0.7, rely=0.05, anchor='center')


        self.music_on = False
        self.start_music()

        self.master.bind("<KeyPress>", self.change_direction)

    def update_score_and_timer(self):

        self.score_label.config(text=f"Score: {self.score}")

        elapsed_time = int(time.time() - self.start_time)
        self.timer_label.config(text=f"Time: {elapsed_time}s")

    def toggle_music(self):
        if self.music_on:
            self.stop_music()
        else:
            self.start_music()
        self.music_on = not self.music_on

    def start_music(self):
        try:
            winsound.PlaySound("./audio/AdhesiveWombat - Night Shade.wav", winsound.SND_ASYNC | winsound.SND_LOOP)
        except NameError:
            pygame.mixer.music.load("./audio/AdhesiveWombat - Night Shade.wav")
            pygame.mixer.music.play(-1)

    def stop_music(self):
        try:
            winsound.PlaySound(None, winsound.SND_ASYNC)
        except NameError:
            pygame.mixer.music.stop()

    def start_game(self):
        self.generate_apple()
        self.generate_rotting_apples()
        self.update()


    def restart_game(self):
        self.restart_button.destroy()
        self.snake = [(self.grid_size[0] // 2, self.grid_size[1] // 2)]
        self.direction = "Right"
        self.score = 0
        self.game_over = False
        self.speed = self.base_speed
        self.apples_eaten = 0
        self.generate_apple()
        self.generate_rotting_apples()
        self.update()
        self.stop_music()

    def update(self):
        myFont = font.Font(family='helvetica', size=24, weight='bold')
        if not self.game_over:
            self.move_snake()
            self.check_collision()
            self.check_apple()
            self.check_rotting_apple()
            self.update_score_and_timer()
            self.draw(self.snake, self.apple, self.rotting_apples,self.direction)
            self.master.after(int(self.speed * 1000), self.update)
        else:
            self.restart_button = tk.Button(self.master, text="Recommencer", command=self.restart_game, bg='white', fg='black', font=myFont)
            self.restart_button.place(relx=0.5, rely=0.5, width=200, height=50, anchor='center')



    def move_snake(self):
        head = self.snake[0]
        new_head = head
        if self.direction == "Up":
            new_head = (head[0] - 1, head[1])
        elif self.direction == "Down":
            new_head = (head[0] + 1, head[1])
        elif self.direction == "Left":
            new_head = (head[0], head[1] - 1)
        elif self.direction == "Right":
            new_head = (head[0], head[1] + 1)
        self.snake.insert(0, new_head)
        self.snake.pop()

    def check_collision(self):
        head = self.snake[0]
        if head[0] < 0 or head[0] >= self.grid_size[0] or head[1] < 0 or head[1] >= self.grid_size[1] or head in self.snake[1:]:
            self.game_over = True

    def generate_apple(self):
        self.apple = (random.randint(0, self.grid_size[0] - 1), random.randint(0, self.grid_size[1] - 1))
        while self.apple in self.snake or self.apple in self.rotting_apples:
            self.apple = (random.randint(0, self.grid_size[0] - 1), random.randint(0, self.grid_size[1] - 1))

    def generate_rotting_apples(self):
        count = random.randint(2, 4)
        self.rotting_apples = []
        for _ in range(count):
            rotting_apple = (random.randint(0, self.grid_size[0] - 1), random.randint(0, self.grid_size[1] - 1))
            while rotting_apple in self.snake or rotting_apple == self.apple or rotting_apple in self.rotting_apples:
                rotting_apple = (random.randint(0, self.grid_size[0] - 1), random.randint(0, self.grid_size[1] - 1))
            self.rotting_apples.append(rotting_apple)

    def check_apple(self):
        head = self.snake[0]
        if head == self.apple:
            self.score += 1
            self.apples_eaten += 1
            if self.apples_eaten % 5 == 0:
                self.speed *= 0.9
            self.snake.append(self.snake[-1])
            self.generate_apple()
            self.generate_rotting_apples()

    def check_rotting_apple(self):
        head = self.snake[0]
        if head in self.rotting_apples:
            self.game_over = True

    def change_direction(self, event):
        if event.keysym in ["Up", "Down", "Left", "Right"]:
            if (event.keysym == "Up" and self.direction != "Down") or \
               (event.keysym == "Down" and self.direction != "Up") or \
               (event.keysym == "Left" and self.direction != "Right") or \
               (event.keysym == "Right" and self.direction != "Left"):
                self.direction = event.keysym


