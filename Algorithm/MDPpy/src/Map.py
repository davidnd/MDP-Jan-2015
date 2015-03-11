# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
from Cell import *
class Map:

    def __init__ (self, w, h):
    	self.width = w
    	self.height = h
        self.grid = [[0 for x in range(self.height)] for x in range(self.width)]
        self.grid[0][0] = 2
        self.grid[0][1] = 2
        self.grid[0][2] = 2
        self.grid[1][0] = 2
        self.grid[1][1] = 2
        self.grid[1][2] = 2
        self.grid[2][0] = 2
        self.grid[2][1] = 2
        self.grid[2][2] = 2
