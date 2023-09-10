'''
This file contains the Tile class which represents a tile on the game map.
'''
class Tile:
    def __init__(self, position, is_obstacle=False):
        self.position = position
        self.is_obstacle = is_obstacle
    def set_obstacle(self, is_obstacle):
        # Set whether the tile is an obstacle or not
        self.is_obstacle = is_obstacle
    def is_tile_obstacle(self):
        # Check if the tile is an obstacle
        return self.is_obstacle