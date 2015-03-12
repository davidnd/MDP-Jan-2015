# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
import Queue
from Map import *
from Robot import *


robot = Robot(1,1,1,'U')
map=Map(15,20)


'''
ArStr='1000000'
print ArStr
print robot.explore(ArStr)
ArStr='0000111'
print ArStr
print robot.explore(ArStr)
ArStr='0000111'
print ArStr
print robot.explore(ArStr)
ArStr='0111111'
print ArStr
print robot.explore(ArStr)

ArStr='0000111'
print ArStr
print robot.explore(ArStr)

ArStr='0000011'
print ArStr
print robot.explore(ArStr)

ArStr='0000001'
print ArStr
print robot.explore(ArStr)

print "finish"

while True:
	ArStr = raw_input("Next sensor data: ")
	robot.explore(ArStr)
'''
robot.generateMapStr()
print robot.mapStr