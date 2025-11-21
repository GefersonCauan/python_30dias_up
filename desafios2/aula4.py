# criar umjogo de minas com  pyhon jogo deverar ter um quadro quadrado, um icone pra passar por cima do quadrados 
# quando o icone  pasaar em cima de uma bomba o jogo acaba, as bombas deverao ser aleatorias, todo novo jogo devera ter uma nova posiçao de bombas
import random
import tkinter as tk

class Minesweeper:
    def __init__(self, master, size=10, bombs=10):
        self.master = master
        self.size = size
        self.bombs = bombs
        self.buttons = {}
        self.create_widgets()
        self.place_bombs()
        self.game_over = False

    def create_widgets(self):
        for x in range(self.size):
            for y in range(self.size):
                button = tk.Button(self.master, text='', width=3, height=1,)
                button.grid(row=x, column=y)
                button.bind('<Enter>', lambda e, x=x, y=y: self.on_hover(x, y))
                self.buttons[(x, y)] = button

    def place_bombs(self):
        self.bomb_positions = set()
        while len(self.bomb_positions) < self.bombs:
            x = random.randint(0, self.size - 1)
            y = random.randint(0, self.size - 1)
            self.bomb_positions.add((x, y))

    def on_hover(self, x, y):
        if self.game_over:
            return
        if (x, y) in self.bomb_positions:
            self.buttons[(x, y)].config(text='💣', bg='red')
            self.game_over = True
            self.reveal_bombs()
        else:
            self.buttons[(x, y)].config(text='✔', bg='green')

    def reveal_bombs(self):
        for (x, y) in self.bomb_positions:
            self.buttons[(x, y)].config(text='💣', bg='red')
            tk.messagebox.showinfo("Game Over", "voçe pisou em uma bomba!")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Minesweeper")
    game = Minesweeper(root, size=10, bombs=10)
    root.mainloop()