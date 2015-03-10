# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
import Queue
from Map import *
from Robot import *


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