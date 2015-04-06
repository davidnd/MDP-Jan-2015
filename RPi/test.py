# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
import Queue
from Map import *
from Robot import *


robot = Robot(1,1,1,'U')
map=Map(15,20)
map.grid = [[0,0,0,0,0,0,0,0,0,0,1,1,0,0,0],
		[0,0,0,0,0,0,0,0,0,0,1,1,0,0,0],
		[0,0,0,0,0,0,0,0,0,0,1,1,0,0,0],
		[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
		[0,0,0,0,1,0,0,0,0,0,0,0,0,0,0],
		[0,0,0,1,1,1,0,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0,0,0,0,0,1,1,1],
		[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
		[0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],
		[0,0,1,0,0,0,0,0,0,0,0,1,0,0,0],
		[0,0,1,1,1,1,0,0,0,0,0,1,0,0,0],
		[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0,0,1,0,0,0,0,0],
		[0,0,0,0,0,0,0,0,0,1,0,0,0,0,0],
		[0,0,0,1,0,0,0,0,0,0,0,0,0,0,1],
		[0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,1,1,1,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,1,0,0,0,0,0,0,0]]
for i in range(20):
	for j in range(15):
		if(map.grid[i][j] == 0):
			map.grid[i][j] = 2
robot.Memory = map
robot.fastestPathCompute()
print robot.fastestRun('A')
print robot.fastestRun('A')
print robot.fastestRun('A')
print robot.fastestRun('A')
print robot.fastestRun('A')

