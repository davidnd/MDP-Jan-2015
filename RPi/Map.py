# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
from Cell import *
class Map:
    width = 15
    height = 20

    def __init__ (self, width, height):
        self.grid = [[0 for x in range(width)] for x in range(height)] 
        for i in range(0,height):
            for j in range (0, width):
                self.grid[i][j] = Cell()
