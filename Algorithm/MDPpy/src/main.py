# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
import Queue
from Map import *
from Robot import *
import sys


robot = Robot(1,1,1,'U')
map=Map(15,20)


ArStr='1000000'
print robot.explore(ArStr)
ArStr='0000111'
print robot.explore(ArStr)
ArStr='0000111'
print robot.explore(ArStr)
ArStr='0010111'
print robot.explore(ArStr)
ArStr='0000001'
print robot.explore(ArStr)
ArStr='0000000'
print robot.explore(ArStr)
ArStr='0000010'
print robot.explore(ArStr)
ArStr='0000001'
print robot.explore(ArStr)
ArStr='0000000'
print robot.explore(ArStr)

print "finish"

for i in range (0,20):
    for j in range (15):
        print robot.Memory.grid[i][j].status

robot.Memory.convertMap()
print robot.Memory.map1
print robot.Memory.map2
#print robot.Memory.convertToHex(robot.Memory.map1)

a= "000222200000000000221222000000000222222200000222000222200000002222222200000000222000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000";
print sys.getsizeof(a)
