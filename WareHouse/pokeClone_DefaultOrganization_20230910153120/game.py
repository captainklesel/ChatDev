'''
This file contains the Game class which manages the game logic.
'''
import tkinter as tk
from player import Player
from map import Map
class Game:
    def __init__(self, root):
        self.root = root
        self.player = Player()
        self.map = Map()
    def start(self):
        self.create_widgets()
    def create_widgets(self):
        # Create game canvas
        self.canvas = tk.Canvas(self.root, width=800, height=600)
        self.canvas.pack()
        # Bind arrow key events
        self.root.bind("<KeyPress>", self.handle_keypress)
        # Start the game loop
        self.update()
    def update(self):
        # Update player position and redraw the map
        self.player.update()
        self.map.draw(self.canvas, self.player.position)
        # Check for collision with objects on the map
        if self.map.check_collision(self.player.position):
            self.handle_collision()
        # Repeat the update after a delay
        self.root.after(100, self.update)
    def handle_keypress(self, event):
        # Handle arrow key events to move the player
        if event.keysym == "Up":
            self.player.move("up")
        elif event.keysym == "Down":
            self.player.move("down")
        elif event.keysym == "Left":
            self.player.move("left")
        elif event.keysym == "Right":
            self.player.move("right")
    def handle_collision(self):
        # Handle collision with objects on the map
        pass