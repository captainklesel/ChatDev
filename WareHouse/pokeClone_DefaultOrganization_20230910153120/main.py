'''
This is the main file of the Pokemon style adventure game.
'''
import tkinter as tk
from game import Game
def main():
    root = tk.Tk()
    root.title("Pokemon Adventure Game")
    game = Game(root)
    game.start()
    root.mainloop()
if __name__ == "__main__":
    main()