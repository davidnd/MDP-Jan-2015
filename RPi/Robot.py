# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "Yiko"
__date__ = "$2-Mar-2015 10:34:11 AM$"

from Map import *
from Node import *
from Cell import *

class Robot:
    
    def __init__(self):
        self.X = 1
        self.Y = 1
        self.Range = 1
        self.Dir = 'U'
        "empty memory for robot"
        self.Memory = Map(15,20)
        self.XGoal = 13
        self.YGoal = 18
        self.XStart = 1
        self.YStart = 1
        self.turnedRight = False
        self.turnedAround = False
        self.turnedLeft = False
        self.StartNode = Node(self.XStart, self.YStart)
        self.GoalNode = Node(self.XGoal, self.YGoal)
        "self.ShortestPath = Node[]"
        self.enteredGoal=False
        self.mapStr = ''
        self.androidMapStr=''

    def __init__(self, x, y, r, d):
        self.X = x
        self.Y = y
        self.turnedRight = False
        self.turnedAround = False
        self.turnedLeft = False
        self.Range = r
        self.Dir = d
        self.lastDir = ''
        "empty memory for robot"
        self.Memory = Map(15,20)
        self.XGoal = 13
        self.YGoal = 18
        self.XStart = 1
        self.YStart = 1
        self.StartNode = Node(self.XStart, self.YStart)
        self.GoalNode = Node(self.XGoal, self.YGoal)
        "self.ShortestPath = Node[]"
        self.enteredGoal=False
        self.mapStr=''
        self.androidMapStr=''

    def turnLeft(self):
        if self.Dir=='U':
            self.Dir = 'L'
            self.lastDir = 'U' 
            turnedLeft = True
        elif self.Dir=='D':
            self.Dir = 'R'
            self.lastDir = 'D' 
            turnedLeft = True
            
        elif self.Dir== 'R':
            self.Dir = 'U'
            self.lastDir = 'R' 
            turnedLeft = True
            
        elif self.Dir== 'L':
            self.Dir = 'D'
            self.lastDir = 'L' 
            turnedLeft = True
            
 
                
    def turnRight(self):  
        if self.Dir== 'U':
            self.Dir = 'R'
            self.lastDir = 'U'
            self.turnedRight = True
            
        elif self.Dir== 'D':
            self.Dir = 'L'
            self.lastDir = 'D' 
            self.turnedRight = True
            
        elif self.Dir== 'R':
            self.Dir = 'D'
            self.lastDir = 'R' 
            self.turnedRight = True
            
        elif self.Dir== 'L':
            self.Dir = 'U'
            self.lastDir = 'L' 
            self.turnedRight = True

    def moveForward(self,dis):
        if self.Dir== 'U':
            self.Y+=dis

        elif self.Dir== 'D':
            self.Y-=dis
            
        elif self.Dir== 'R':
            self.X+=dis
            
        elif self.Dir== 'L':
            self.X-=dis
            
 


    def turnAround(self):
        if self.Dir == 'U':
            self.Dir = 'D'
            self.lastDir = 'U'
            self.turnedAround = True
            
        elif self.Dir== 'D':
            self.Dir = 'U'
            self.lastDir = 'D' 
            self.turnedAround = True
            
        elif self.Dir== 'R':
            self.Dir = 'L'
            self.lastDir = 'R'
            self.turnedAround = True

        elif self.Dir== 'L':
            self.Dir = 'R'
            self.lastDir = 'L'
            self.turnedAround = True
            
    def explore(self,ArStr):
        print "Current X= ", self.X, " Current Y = ", self.Y
        try:
            isBlockedLeft = self.checkLeftSide(ArStr)
            isBlockedFront = self.checkTopSide(ArStr)
            isBlockedRight = self.checkRightSide(ArStr)
            if ((self.X == 12 or self.X==13 )and (self.Y==17 or self.Y==18)):
                self.enteredGoal = True
            if (self.X == 1 and self.Y == 1 and self.enteredGoal == True):
                return 'F'
            if (not isBlockedRight and  not self.turnedRight):
                print("Turn right")
                self.turnRight()
                self.generateMapStr()
                print self.Dir
                return "2"
            elif (not isBlockedFront):
                print("Move Forward")
                self.moveForward(1)
                self.generateMapStr()
                print self.Dir
                self.turnedRight = False
                return "1"
            elif (not isBlockedLeft):
                print("turn left")
                self.turnedRight = False
                self.turnLeft()
                self.generateMapStr()
                print self.Dir
                return "3"
            else:
                print("Turn around")
                self.turnAround()
                self.generateMapStr()
                print self.Dir
                self.turnedRight = False
                return "4"
        except ValueError as e:
            print(e.Message)
            print(e)
        print 
    
    def checkLeftSide(self, ArStr):
        isBlocked = False
        if self.Dir == 'R':
            isBlocked = self.checkTop()
        if self.Dir == 'U':
            isBlocked = self.checkLeft()
        if self.Dir == 'L':
            isBlocked = self.checkBottom()
        if self.Dir == 'D':
            isBlocked = self.checkRight()
        #x = self.X - self.Range - 1
        if (isBlocked):
            return True
        if (ArStr[0] == '1'):
            isBlocked = True
            #explored and has obstacle
            self.updateMap(0, 1)
        else:
            #empty cell
            self.updateMap(0, 2)
        print "Left", isBlocked
        return isBlocked
    
    def checkTopSide(self, ArStr):
        isBlocked = False
        if self.Dir == 'R':
            isBlocked = self.checkRight()
        if self.Dir == 'U':
            isBlocked = self.checkTop()
        if self.Dir == 'L':
            isBlocked = self.checkLeft()
        if self.Dir == 'D':
            isBlocked = self.checkBottom()
        if (isBlocked):
            return True
        for i in range(1,4):
            if (ArStr[i]=='1'):
                isBlocked = True
                #explored and has obstacle 
                self.updateMap(i, 1)
            else:
                #empty 
                self.updateMap(i, 2)
        print "TOP", isBlocked
        return isBlocked

    def checkRightSide(self, ArStr):
        isBlocked = False
        if self.Dir == 'R':
            isBlocked = self.checkBottom()
        if self.Dir == 'U':
            isBlocked = self.checkRight()
        if self.Dir == 'L':
            isBlocked = self.checkTop()
        if self.Dir == 'D':
            isBlocked = self.checkLeft()
        if (isBlocked):
            return True
        for i in range(4,7):
            if (ArStr[i] == '1'):
                isBlocked = True
                #explored and has obstacle 
                self.updateMap(i, 1)
            else:
                #empty
                self.updateMap(i, 2)
        print "RIGHT ", isBlocked
        return isBlocked

    #not done
    def updateMap(self, pos, val):
        if(self.Dir == 'U'):
            if(pos == 0):
                self.Memory.grid[self.X - 2][self.Y + 1] = val
            if(pos == 1):
                self.Memory.grid[self.X - 1][self.Y + 2] = val
            if(pos == 2):
                self.Memory.grid[self.X][self.Y + 2] = val
            if(pos == 3):
                self.Memory.grid[self.X + 1][self.Y + 2] = val
            if(pos == 4):
                self.Memory.grid[self.X + 2][self.Y + 1] = val
            if(pos == 5):
                self.Memory.grid[self.X + 2][self.Y] = val
            if(pos == 6):
                self.Memory.grid[self.X + 2][self.Y - 1] = val
        elif(self.Dir == 'R'):
            if(pos == 0):
                self.Memory.grid[self.X + 1][self.Y + 2] = val
            if(pos == 1):
                self.Memory.grid[self.X + 2][self.Y + 1] = val
            if(pos == 2):
                self.Memory.grid[self.X + 2][self.Y] = val
            if(pos == 3):
                self.Memory.grid[self.X + 2][self.Y - 1] = val
            if(pos == 4):
                self.Memory.grid[self.X + 1][self.Y - 2] = val
            if(pos == 5):
                self.Memory.grid[self.X][self.Y - 2] = val
            if(pos == 6):
                self.Memory.grid[self.X - 1][self.Y - 2] = val
        elif(self.Dir == 'D'):
            if(pos == 0):
                self.Memory.grid[self.X + 2][self.Y - 1] = val
            if(pos == 1):
                self.Memory.grid[self.X + 1][self.Y - 2] = val
            if(pos == 2):
                self.Memory.grid[self.X][self.Y - 2] = val
            if(pos == 3):
                self.Memory.grid[self.X - 1][self.Y - 2] = val
            if(pos == 4):
                self.Memory.grid[self.X - 2][self.Y - 1] = val
            if(pos == 5):
                self.Memory.grid[self.X - 2][self.Y] = val
            if(pos == 6):
                self.Memory.grid[self.X - 2][self.Y + 1] = val
        elif(self.Dir == 'L'):
            if(pos == 0):
                self.Memory.grid[self.X - 1][self.Y - 2] = val
            if(pos == 1):
                self.Memory.grid[self.X - 2][self.Y - 1] = val
            if(pos == 2):
                self.Memory.grid[self.X - 2][self.Y] = val
            if(pos == 3):
                self.Memory.grid[self.X - 2][self.Y + 1] = val
            if(pos == 4):
                self.Memory.grid[self.X - 1][self.Y + 2] = val
            if(pos == 5):
                self.Memory.grid[self.X][self.Y + 2] = val
            if(pos == 6):
                self.Memory.grid[self.X + 1][self.Y + 2] = val

    def checkTop(self):
        if(self.Y + self.Range + 1 >= self.Memory.height):
            return True
        if(self.Memory.grid[self.X -1][self.Y + 2] == 1):
            return True
        if(self.Memory.grid[self.X][self.Y + 2] == 1):
            return True
        if(self.Memory.grid[self.X + 1][self.Y + 2] == 1):
            return True
        return False
    def checkLeft(self):
        if(self.X - self.Range - 1 < 0):
            return True
        if(self.Memory.grid[self.X - 2][self.Y + 1] == 1):
            return True
        if(self.Memory.grid[self.X - 2][self.Y] == 1):
            return True
        if(self.Memory.grid[self.X - 2][self.Y -1 ] == 1):
            return True
        return False
    def checkRight(self):
        if(self.X + self.Range + 1 >= self.Memory.width):
            return True
        if(self.Memory.grid[self.X + 2][self.Y + 1] == 1):
            return True
        if(self.Memory.grid[self.X+2][self.Y] == 1):
            return True
        if(self.Memory.grid[self.X + 2][self.Y -1] == 1):
            return True
        return False
    def checkBottom(self):
        if(self.Y - self.Range - 1 >= self.Memory.height):
            return True
        if(self.Memory.grid[self.X -1][self.Y - 2] == 1):
            return True
        if(self.Memory.grid[self.X][self.Y - 2] == 1):
            return True
        if(self.Memory.grid[self.X + 1][self.Y - 2] == 1):
            return True
        return False

    def generateMapStr(self):
        # first 5 characters: direction + current center position
        if (self.X < 10):
            x = '0'+ str(self.X)
        else:
            x = str(self.X)
        if (self.Y < 10):
            y = '0'+ str(self.Y)
        else:
            y = str(self.Y) 
        self.mapStr = self.Dir + x + y
        
        # iterate the map to add value to mapStr
        for i in range (20):
            for j in range (15):
                self.mapStr += str(self.Memory.grid[j][i])
        if (self.X == 1 and self.Y == 1 and self.enteredGoal):
            self.mapStr += 'F'
        
    def generateAndroidMapStr(self):
        # first 9 characters: GRID + direction + current center position
        if (self.X < 9):
            x = '0'+ str(self.X+1)
        else:
            x = str(self.X+1)
        if (self.Y < 9):
            y = '0'+ str(self.Y+1)
        else:
            y = str(self.Y+1) 
        self.androidMapStr = 'GRID' + self.Dir + x + y
        
        # iterate the map to add value to androidMapStr
        for i in range (15):
            for j in range (20):
                self.androidMapStr += str(self.Memory.grid[i][j])
        if (self.X == 1 and self.Y == 1 and self.enteredGoal):
            self.androidMapStr += 'F'
        else:
            self.androidMapStr += 'P'
        
    def startZoneRealign(self):
        if self.Dir == 'D':
            self.turnAround()
            return '4'
        elif self.Dir == 'L':
            self.turnRight()
            return '2'
        elif self.Dir == 'R':
            self.turnLeft()
            return '3'
        else:
            return
        
          
    def fastestPathDecoder(self, pcStr):
        pathCommand = ''
        for i in range (len(pcStr)):
            if pcStr[i] == 'M':
                pathCommand += '1'
            elif pcStr[i] == 'R':
                pathCommand += '2'
            elif pcStr[i] == 'L':
                pathCommand += '3'
        return pathCommand
    
    #not done
    def fastestRun(self, i, arStr):
            
        return pathCommand[i]