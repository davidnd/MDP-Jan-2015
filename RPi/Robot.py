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
        self.reposFront = False
        self.reposRight = False
        self.reposLeft = False
        self.resetError = False
        self.isWall = False
        self.threeObsHead = False
        self.threeObs = False
        self.androidMapStr=''
        self.pathCommand = ''
        self.lastCorner = 0
        self.justRF = False
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
        print "Dir = ", self.Dir
        try:
            isBlockedLeft = self.checkLeftSide(ArStr)
            isBlockedFront = self.checkTopSide(ArStr)
            isBlockedRight = self.checkRightSide(ArStr)
            if ((self.X == 12 or self.X==13 )and (self.Y==17 or self.Y==18)):
                self.enteredGoal = True
            if (self.X == 1 and self.Y == 1 and self.enteredGoal == True):
                self.generateMapStr()
                self.generateAndroidMapStr()
                return 'F'
            #repos front call
            print 'ReposFront \t\t\t', self.reposFront
            print 'ReposRight \t\t\t', self.reposRight
            print 'ReposLeft \t\t\t', self.reposLeft
            if(self.reposFront and self.reposRight and self.lastCorner == 0):
                print 'Reseting error...'
                self.lastCorner = 1
                self.generateMapStr()
                self.generateAndroidMapStr()
                self.printMemory()
                self.reset()
                return '7'
            if(self.lastCorner == 1):
                print 'Realigning front...'
                self.lastCorner = 2
                self.printMemory()
                self.reset()
                return '5'
            if(self.lastCorner == 2):
                print 'Turn left'
                self.lastCorner = 0
                self.turnLeft()
                self.printMemory()
                self.reset()
                return '3'
            if(self.reposFront and not self.justRF):
                print "Realigning front, not at corner... "
                self.justRF = True
                self.reset()
                #in case there are some changes
                self.generateMapStr();
                self.generateAndroidMapStr()
                self.printMemory()
                return '5'
            else:
                self.justRF = False

            # not using for now
            if(self.resetError):
                print "Resetting error, not at corner..."
                self.reset()
                #in case there are some changes
                self.generateMapStr();
                self.generateAndroidMapStr()
                self.printMemory()
                return '7'

            if (not isBlockedRight and  not self.turnedRight):
                print("Turn right")
                self.turnRight()
                self.generateMapStr()
                self.generateAndroidMapStr()
                self.printMemory()
                self.reset()
                return "2"
            elif (not isBlockedFront):
                print("Move Forward")
                self.moveForward(1)
                self.generateMapStr()
                self.generateAndroidMapStr()
                self.printMemory()
                self.turnedRight = False
                self.reset()
                return "1"
            elif (not isBlockedLeft):
                print("Turn left")
                self.turnedRight = False
                self.turnLeft()
                self.generateMapStr()
                self.generateAndroidMapStr()
                self.printMemory()
                self.reset()
                return "3"
            else:
                # should turn left here in case it detects wrong obs
                print("Turn left")
                self.turnLeft()
                self.generateMapStr()
                self.generateAndroidMapStr()
                self.printMemory()
                self.reset()
                self.turnedRight = False
                return "3"
        except ValueError as e:
            print(e.Message)
            print(e)
        print 
    def reset(self):
        self.isWall = False
        self.threeObs = False
        self.reposFront = False
        self.reposLeft = False
        self.reposRight = False
        self.resetError = False
    
    def checkLeftSide(self, ArStr):
        print "checking left side"

        isBlocked = False
        if self.Dir == 'R':
            isBlocked = self.checkTop()
        if self.Dir == 'U':
            isBlocked = self.checkLeft()
        if self.Dir == 'L':
            isBlocked = self.checkBottom()
        if self.Dir == 'D':
            isBlocked = self.checkRight()

        if(not self.isWall):
            if(ArStr[0] == '1'):
                self.updateMap(0, 1)
                isBlocked = True
            else:
                self.updateMap(0, 2)
        if(self.isWall or self.threeObs):
            self.reposLeft = True
            isBlocked = True
        self.isWall = False
        self.threeObs = False
        print "LEFT \t\t\t", isBlocked
        if(isBlocked):
            return True
        return isBlocked
    
    def checkTopSide(self, ArStr):
        print "checking top side"
        isBlocked = False
        if self.Dir == 'R':
            isBlocked = self.checkRight()
        if self.Dir == 'U':
            isBlocked = self.checkTop()
        if self.Dir == 'L':
            isBlocked = self.checkLeft()
        if self.Dir == 'D':
            isBlocked = self.checkBottom()
        if (self.isWall or self.threeObs):
            print 'setting repost front true'
            self.reposFront = True
        if(not self.isWall):
            for i in range(1,4):
                if (ArStr[i]=='1'):
                    self.updateMap(i, 1)
                    isBlocked = True
                else:
                    self.updateMap(i, 2)
        self.isWall = False
        self.threeObs = False        
        print "TOP \t\t\t", isBlocked
        return isBlocked

    def checkRightSide(self, ArStr):
        print "checking right side"
        
        isBlocked = False
        if self.Dir == 'R':
            isBlocked = self.checkBottom()
        if self.Dir == 'U':
            isBlocked = self.checkRight()
        if self.Dir == 'L':
            isBlocked = self.checkTop()
        if self.Dir == 'D':
            isBlocked = self.checkLeft()

        if(not self.isWall):
            if(ArStr[4] == '1'):
                self.updateMap(4, 1)
                isBlocked = True
            else:
                self.updateMap(4, 2)
            if(ArStr[6] == '1'):
                self.updateMap(6, 1)
                isBlocked = True
            else:
                self.updateMap(6, 2)

        if(self.isWall or self.threeObs):
            self.reposRight = True
        self.isWall = False
        self.threeObs = False

        print "RIGHT \t\t\t", isBlocked
        return isBlocked

    def updateMap(self, pos, val):
        if(self.Dir == 'U'):
            if(pos == 0):
                self.Memory.grid[self.Y + 1][self.X -2] = val
            if(pos == 1):
                self.Memory.grid[self.Y + 2][self.X - 1] = val
            if(pos == 2):
                self.Memory.grid[self.Y + 2][self.X] = val
            if(pos == 3):
                self.Memory.grid[self.Y + 2][self.X + 1] = val
            if(pos == 4):
                self.Memory.grid[self.Y + 1][self.X + 2] = val
            if(pos == 5):
                self.Memory.grid[self.Y][self.X + 2] = val
            if(pos == 6):
                self.Memory.grid[self.Y-1][self.X + 2] = val
        elif(self.Dir == 'R'):
            if(pos == 0):
                self.Memory.grid[self.Y+2][self.X + 1] = val
            if(pos == 1):
                self.Memory.grid[self.Y+1][self.X + 2] = val
            if(pos == 2):
                self.Memory.grid[self.Y][self.X+2] = val
            if(pos == 3):
                self.Memory.grid[self.Y-1][self.X +2] = val
            if(pos == 4):
                self.Memory.grid[self.Y-2][self.X+1] = val
            if(pos == 5):
                self.Memory.grid[self.Y-2][self.X] = val
            if(pos == 6):
                self.Memory.grid[self.Y-2][self.X-1] = val
        elif(self.Dir == 'D'):
            if(pos == 0):
                self.Memory.grid[self.Y-1][self.X +2] = val
            if(pos == 1):
                self.Memory.grid[self.Y-2][self.X+1] = val
            if(pos == 2):
                self.Memory.grid[self.Y-2][self.X] = val
            if(pos == 3):
                self.Memory.grid[self.Y-2][self.X-1] = val
            if(pos == 4):
                self.Memory.grid[self.Y-1][self.X- 2] = val
            if(pos == 5):
                self.Memory.grid[self.Y][self.X-2] = val
            if(pos == 6):
                self.Memory.grid[self.Y+1][self.X -2] = val
        elif(self.Dir == 'L'):
            if(pos == 0):
                self.Memory.grid[self.Y-2][self.X - 1] = val
            if(pos == 1):
                self.Memory.grid[self.Y-1][self.X - 2] = val
            if(pos == 2):
                self.Memory.grid[self.Y][self.X-2] = val
            if(pos == 3):
                self.Memory.grid[self.Y+1][self.X - 2] = val
            if(pos == 4):
                self.Memory.grid[self.Y+2][self.X - 1] = val
            if(pos == 5):
                self.Memory.grid[self.Y+2][self.X] = val
            if(pos == 6):
                self.Memory.grid[self.Y+2][self.X + 1] = val

    def checkTop(self):
        temp1 = False
        temp2 = False
        temp3 = False
        isBlocked = False
        # wall
        if(self.Y + self.Range + 1 >= self.Memory.height):
            self.threeObs = True
            self.isWall = True
            return True
        if(self.Memory.grid[self.Y + 2][self.X -1] == 1):
            isBlocked = True
            temp1 = True
        
        if(self.Memory.grid[self.Y + 2][self.X] == 1):
            isBlocked = True
            temp2 = True
        
        if(self.Memory.grid[self.Y + 2][self.X + 1]== 1):
            isBlocked = True
            temp3 = True

        #3 obstacles on top side
        if(temp1 and temp2 and temp3):
            self.threeObs = True
        else:
            self.threeObs = False
        return isBlocked

    def checkLeft(self):
        temp1 = False
        temp2 = False
        temp3 = False
        isBlocked = False
        # wall
        if(self.X - self.Range - 1 < 0):
            self.isWall = True
            self.threeObs = True
            return True
        
        if(self.Memory.grid[self.Y + 1][self.X - 2] == 1):
            isBlocked = True
            temp1 = True
        
        if(self.Memory.grid[self.Y][self.X - 2] == 1):
            isBlocked = True
            temp2 = True
        
        if(self.Memory.grid[self.Y -1 ][self.X - 2]== 1):
            isBlocked = True
            temp3 = True

        if(temp1 and temp2 and temp3):
            self.threeObs = True
        else:
            self.threeObs = False
        return isBlocked
    def checkRight(self):
        isBlocked = False
        temp1 = False
        temp2 = False
        temp3 = False
        if(self.X + self.Range + 1 >= self.Memory.width):
            self.isWall = True
            self.threeObs = True
            return True
        if(self.Memory.grid[self.Y + 1][self.X + 2] == 1):
            isBlocked = True
            temp1 = True
        if(self.Memory.grid[self.Y][self.X+2] == 1):
            isBlocked = True
            temp2 = True
        if(self.Memory.grid[self.Y -1][self.X + 2] == 1):
            isBlocked = True
            temp3 = True
        if(temp1 and temp2 and temp3):
            self.threeObs = True
        else:
            self.threeObs = False
        return isBlocked
    def checkBottom(self):
        temp1 = False
        temp2 = False
        temp3 = False
        isBlocked = False
        if(self.Y - self.Range - 1 < 0):
            self.isWall = True
            self.threeObs = True
            return True

        if(self.Memory.grid[self.Y-2][self.X - 1] == 1):
            isBlocked = True
            temp1 = True
        if(self.Memory.grid[self.Y - 2][self.X] == 1):
            isBlocked = True
            temp2 = True
        if(self.Memory.grid[self.Y - 2][self.X + 1]== 1):
            isBlocked = True
            temp3 = True
        if(temp1 and temp2 and temp3):
            self.threeObs = True
        else:
            self.threeObs = False
        return isBlocked

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
                self.mapStr += str(self.Memory.grid[i][j])
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
        self.androidMapStr = 'GRID' + self.Dir + y + x
        
        # iterate the map to add value to androidMapStr
        for i in range (15):
            for j in range (20):
                self.androidMapStr += str(self.Memory.grid[j][i])
        if (self.X == 1 and self.Y == 1 and self.enteredGoal):
            self.androidMapStr += 'F'
        else:
            self.androidMapStr += 'P'
        
    def startZoneRealign(self):
        if self.Dir == 'D':
            self.turnAround()
            self.generateMapStr()
            self.generateAndroidMapStr()
            return '4'
        elif self.Dir == 'L':
            self.turnRight()
            self.generateMapStr()
            self.generateAndroidMapStr()
            return '2'
        elif self.Dir == 'R':
            self.turnLeft()
            self.generateMapStr()
            self.generateAndroidMapStr()
            return '3'
        else:
            return
        
          
    def fastestPathDecoder(self, pcStr):
        pcStr = pcStr[1:len(pcStr)]
        for i in range (len(pcStr)):
            if pcStr[i] == 'M':
                self.pathCommand += '1'
            elif pcStr[i] == 'R':
                self.pathCommand += '2'
            elif pcStr[i] == 'L':
                self.pathCommand += '3'
            else:
                return
    
    #not done
    def fastestRun(self, i, arStr):
        if (self.pathCommand[i] == '1'):
            self.moveForward(1)
        elif (self.pathCommand[i] == '2'):
            self.turnRight()
        elif (self.pathCommand[i] == '3'):
            self.turnLeft()
        else:
            return
        self.generateMapStr()
        self.generateAndroidMapStr() 
        print "currrent position: X = ", self.X, "Y = ", self.Y, "Direction: ", self.Dir
        return self.pathCommand[i]

    def printMemory(self):
        for i in range(20):
            for j in range (15):
                if(self.X == j and self.Y == 19-i):
                    print 'X', ' ',
                else:
                    print self.Memory.grid[19-i][j], ' ',
            print 

