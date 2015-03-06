# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
import Queue
from Map import *
from Robot import *


robot = Robot(1,1,1,'U')
map=Map(15,20)



ArStr='100000'
print ArStr
print robot.explore(ArStr)
ArStr='000011'
print ArStr
print robot.explore(ArStr)
ArStr='000011'
print ArStr
print robot.explore(ArStr)
ArStr='001011'
print ArStr
print robot.explore(ArStr)

ArStr='110011'
print ArStr
print robot.explore(ArStr)

print "finish"
