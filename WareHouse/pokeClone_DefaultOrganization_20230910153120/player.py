'''
This file contains the Player class which represents the player character.
'''
class Player:
    def __init__(self):
        self.position = (0, 0)
    def move(self, direction):
        # Update player position based on the direction
        if direction == "up":
            self.position = (self.position[0], self.position[1] - 1)
        elif direction == "down":
            self.position = (self.position[0], self.position[1] + 1)
        elif direction == "left":
            self.position = (self.position[0] - 1, self.position[1])
        elif direction == "right":
            self.position = (self.position[0] + 1, self.position[1])
    def update(self):
        # Update player state
        pass