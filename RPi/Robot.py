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
                return 'F'
            #repos front call
            if(self.reposFront):
                print "Realigning front"
                self.isWall = False
                self.reposLeft = False
                self.reposRight = False
                self.resetError = False
                #in case there are some changes
                self.generateMapStr();
                self.generateAndroidMapStr()
                self.printMemory()
                return '5'
            if(self.resetError):
                print "Resetting error"
                self.isWall = False
                self.reposFront = False
                self.reposLeft = False
                self.reposRight = False
                self.resetError = False
                #in case there are some changes
                self.generateMapStr();
                self.generateAndroidMapStr()
                self.printMemory()
                return '7'
            '''
            if(self.reposFront):
                self.isWall = False
                self.reposFront = False
                self.reposLeft = False
                self.reposRight = False
                self.resetError = False
                #in case there are some changes
                generateMapStr();
                return '5'
            '''
            #for safety
            if(self.isWall):
                self.isWall = False
            if (not isBlockedRight and  not self.turnedRight):
                print("Turn right")
                self.turnRight()
                self.generateMapStr()
                self.generateAndroidMapStr()
                self.printMemory()
                return "2"
            elif (not isBlockedFront):
                print("Move Forward")
                self.moveForward(1)
                self.generateMapStr()
                self.generateAndroidMapStr()
                self.printMemory()
                self.turnedRight = False
                return "1"
            elif (not isBlockedLeft):
                print("turn left")
                self.turnedRight = False
                self.turnLeft()
                self.generateMapStr()
                self.generateAndroidMapStr()
                self.printMemory()
                return "3"
            else:
                print("Turn around")
                self.turnAround()
                self.generateMapStr()
                self.generateAndroidMapStr()
                self.printMemory()
                self.turnedRight = False
                return "4"
        except ValueError as e:
            print(e.Message)
            print(e)
        print 
    
    def checkLeftSide(self, ArStr):
        print "checking left side"
        isBlocked = False
        memoryBlock = False
        if self.Dir == 'R':
            memoryBlock = self.checkTop()
        if self.Dir == 'U':
            memoryBlock = self.checkLeft()
        if self.Dir == 'L':
            memoryBlock = self.checkBottom()
        if self.Dir == 'D':
            memoryBlock = self.checkRight()
        #x = self.X - self.Range - 1

        #rarely used, called by arduino
        if(memoryBlock and self.isWall):
            self.reposLeft = True
            self.isWall = False
            return True
        #rarely used
        #dont update map for safety if robot return 0 but actually 1 for sure 
        if(self.threeObs):
            self.reposLeft = True
            self.threeObs = False
            return True
        if (ArStr[0] == '1'):
            isBlocked = True
            #explored and has obstacle
            self.updateMap(0, 1)
        else:
            #empty cell
            self.updateMap(0, 2)
        print "Left", isBlocked
        if(memoryBlock):
            return True
        return isBlocked
    
    def checkTopSide(self, ArStr):
        print "checking top side"
        isBlocked = False
        #try to repos
        memoryBlock = False
        if self.Dir == 'R':
            memoryBlock = self.checkRight()
        if self.Dir == 'U':
            memoryBlock = self.checkTop()
        if self.Dir == 'L':
            memoryBlock = self.checkLeft()
        if self.Dir == 'D':
            memoryBlock = self.checkBottom()
        #put memoryBlock in condition for safety
        if (memoryBlock and self.isWall):
            if(self.reposFront):
                self.reposFront = False
            else:
                print "require realign front when memory blocked or is wall"
                self.reposFront = True
            self.isWall = False
            return True
        # three obstacles then dont care the readings
        if(self.threeObs):
            if(self.reposFront):
                self.reposFront = False
            else:
                print "require realign front. Three obs in front"
                self.reposFront = True
            self.threeObs = False
            return True
        #all obstacles based on readings
        allObj = False
        for i in range(1,4):
            if (ArStr[i]=='1'):
                isBlocked = True
                allObj = True
                #explored and has obstacle 
                self.updateMap(i, 1)
            else:
                #empty 
                allObj = False
                self.updateMap(i, 2)
        #detect 3 obstacles ahead, repos front
        if(allObj):
            if(self.reposFront):
                self.reposFront = False
            else:
                self.reposFront = True
        
        print "TOP ", isBlocked
        if(memoryBlock):
            return True
        return isBlocked

    def checkRightSide(self, ArStr):
        print "checking right side"
        isBlocked = False
        memoryBlock = False
        if self.Dir == 'R':
            memoryBlock = self.checkBottom()
        if self.Dir == 'U':
            memoryBlock = self.checkRight()
        if self.Dir == 'L':
            memoryBlock = self.checkTop()
        if self.Dir == 'D':
            memoryBlock = self.checkLeft()
        if(memoryBlock and self.isWall):
            print 'hello'
            self.reposRight = True
            self.isWall = False
            return True
        allObsSensor = False    
        for i in range(4,7):
            if (ArStr[i] == '1'):
                isBlocked = True
                allObsSensor = True
                #explored and has obstacle
                if(self.threeObs):
                    continue 
                self.updateMap(i, 1)
            else:
                #empty
                allObsSensor = False
                if(self.threeObs or i == 5):
                    print 'i = 5 or 3 obs'
                    continue
                self.updateMap(i, 2)
        # reset error when reading from robot conflict with the memory
        if (allObsSensor == False and self.threeObs == True):
            self.resetError = True
            self.threeObs = False
            print "check right side, readings not 3 obs but memory has 3 obs"
        print "RIGHT ", isBlocked
        if(memoryBlock):
            return True
        return isBlocked

    #not done
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
        if(self.Y + self.Range + 1 >= self.Memory.height):
            print "1"
            self.threeObs = True
            self.isWall = True
            return True
        if(self.Memory.grid[self.Y + 2][self.X -1] == 1):
            print "2"
            isBlocked = True
            temp1 = True
        
        if(self.Memory.grid[self.Y + 2][self.X] == 1):
            print "3"
            isBlocked = True
            temp2 = True
        
        if(self.Memory.grid[self.Y + 2][self.X + 1]== 1):
            print "4" 
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
        self.androidMapStr = 'GRID' + self.Dir + x + y
        
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
            return '4'
        elif self.Dir == 'L':
            self.turnRight()
            return '2'
        elif self.Dir == 'R':
            self.turnLeft()
            return '3'
        else:
            return

    def printMemory(self):
        for i in range(20):
            for j in range (15):
                print self.Memory.grid[19-i][j], ' ',
            print 
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
    def fastestRun(self, i, arStr):
       return pathCommand[i]