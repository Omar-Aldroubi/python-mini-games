
import tkinter as tk
from tkinter import *
import tkinter.font as font
from tkmacosx import Button
from SnakeGame import SnakeGame
from TurmiteGame import TurmiteGame
from PlanetTk import PlanetTk
from ConwayGame import ConwayGame


class MyApp:
    def __init__(self, master):
        self.master = master
        self.master.title("MyApp")
        self.master.geometry("1200x1000")
        self.master.configure(bg='#FFFACD')
        self.planet_tk = PlanetTk(self.master)

        self.create_menu_buttons()


    def create_menu_buttons(self):
        myFont = font.Font(family='helvetica', size=24, weight='bold')

        self.b_conway_game = Button(self.master, text="Conway", command=self.launch_conway_game,highlightbackground='black', bg='#77B5FE', fg='black', font=myFont )
        self.b_conway_game.place(relx=0.2, rely=0.3, width=200, height=50)

        self.b_turmite_game = Button(self.master, text="Turmites", command=self.launch_turmite_game,highlightbackground='black', bg='orange', fg='black', font=myFont)
        self.b_turmite_game.place(relx=0.4, rely=0.3, width=200, height=50)

        self.b_snake_game = Button(self.master, text="Snake", command=self.launch_snake_game,highlightbackground='black', bg='green', fg='black', font=myFont)
        self.b_snake_game.place(relx=0.6, rely=0.3, width=200, height=50)

        self.quit_button = Button(self.master, text="Quitter", command=self.quit_app,highlightbackground='black', bg='grey', fg='black', font=myFont)
        self.quit_button.place(relx=0.4, rely=0.6, width=200, height=50)

    def create_back_button(self):
        myFont = font.Font(family='helvetica', size=24, weight='bold')
        self.back_button = Button(self.master, text="Retour", command=self.show_menu, bg='grey', fg='black', font=myFont)
        self.back_button.place(relx=0.5, rely=0.95, width=200, height=50, anchor='center')

    def show_menu(self):
        for widget in self.master.winfo_children():
            widget.destroy()
        self.create_menu_buttons()

    def launch_conway_game(self):
        self.b_conway_game.destroy()
        self.b_turmite_game.destroy()
        self.b_snake_game.destroy()
        self.quit_button.destroy()

        # Assuming PlanetTk and ConwayGame are initialized correctly
        cGame = ConwayGame(self.master, self.planet_tk)
        cGame.start_game()
        self.create_back_button()

    def launch_snake_game(self):
        self.b_conway_game.destroy()
        self.b_turmite_game.destroy()
        self.b_snake_game.destroy()
        self.quit_button.destroy()

        sGame = SnakeGame(self.master, cell_size=40)
        sGame.start_game()
        self.create_back_button()

    def launch_turmite_game(self):
        self.b_conway_game.destroy()
        self.b_turmite_game.destroy()
        self.b_snake_game.destroy()
        self.quit_button.destroy()

        tGame = TurmiteGame(self.master, self.planet_tk, cell_size=40)
        tGame.start_game()
        self.create_back_button()

    def quit_app(self):
        self.master.quit()


if __name__ == "__main__":
    root = tk.Tk()
    app = MyApp(root)
    root.mainloop()

