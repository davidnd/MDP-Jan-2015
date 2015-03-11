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
       self.X = 1;
       self.Y = 1;
       self.Range = 1;
       self.Dir = 'U';
       "empty memory for robot"
       self.Memory = Map(15,20);
       self.XGoal = 13;
       self.YGoal = 18;
       self.XStart = 1;
       self.YStart = 1;
       self.StartNode = Node(self.XStart, self.YStart)
       self.GoalNode = Node(self.XGoal, self.YGoal)
       "self.ShortestPath = Node[]"
       self.VirtualMap = Map(15,20)
    
    def __init__(self, x, y, r, d):
        self.X = x
        self.Y = y
        self.Range = r
        self.Dir = d
        "empty memory for robot"
        self.Memory = Map(15,20)
        self.XGoal = 13
        self.YGoal = 18
        self.XStart = 1
        self.YStart = 1
        self.StartNode = Node(self.XStart, self.YStart)
        self.GoalNode = Node(self.XGoal, self.YGoal)
        "self.ShortestPath = Node[]"
        self.VirtualMap = Map(15,20)
        self.enteredGoal=True
    

   
    


    def turnLeft(self):
        if self.Dir=='U':
            self.Dir = 'L'
          
        elif self.Dir=='D':
            self.Dir = 'R'
            
        elif self.Dir== 'R':
            self.Dir = 'U'
            
        elif self.Dir== 'L':
            self.Dir = 'D'
            
 
                
    def turnRight(self):  
        if self.Dir== 'U':
            self.Dir = 'R'
            
        elif self.Dir== 'D':
            self.Dir = 'L'
            
        elif self.Dir== 'R':
            self.Dir = 'D'
            
        elif self.Dir== 'L':
            self.Dir = 'U'


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
            
        elif self.Dir== 'D':
            self.Dir = 'U'
            
        elif self.Dir== 'R':
            self.Dir = 'L'
            
        elif self.Dir== 'L':
            self.Dir = 'R'
            
            

    def explore(self,ArStr):
        moved = False
        while  ((self.X != 1 or self.Y != 1) or (not moved)):
            print "Current X = {0}, Y = {1}", self.X, self.Y
            try:
                isBlockedLeft = self.checkLeftSide(ArStr)
                isBlockedFront = self.checkTopSide(ArStr)
                isBlockedRight = self.checkRightSide(ArStr)
                if (not isBlockedRight):
                    print("Turn right")
                    self.turnRight()
                    return '2'
                elif (not isBlockedFront):
                    print("Move Forward");
                    moved = True
                    self.moveForward(1)
                    return '1'
                elif (not isBlockedLeft):
                    print("turn left");
                    self.turnLeft();
                    return '3'
                else:
                    print("Turn around")
                    self.turnAround()
                    return '4'
            except ValueError as e:
                print(e.Message)
                print(e)
    
    def checkLeftSide(self, ArStr):
        # left here
        isBlocked = False
  

        #x = self.X - self.Range - 1
        if (ArStr[0] == '1'):
            isBlocked = True
            "explored and has obstacle"
            #self.Memory.grid[self.Y][x].Status = 1
        elif (ArStr[0] == '2'):
            "map second block to have obstacle"
            #self.Memory.grid[][]
        else:
            "empty cell"
            #self.Memory.grid[self.Y][x].Status = 2
        print "Left", isBlocked
        return isBlocked
    
    def checkTopSide(self, ArStr):
        isBlocked = False
        #if (self.Y + self.Range + 1 >= self.Env.Grid.GetLength(0))
        #    return True;
        # y = self.Y + self.Range + 1
     

        for i in range(1,4):
            if (ArStr[i]=='1'):
                isBlocked = True
                "explored and has obstacle"
                #self.Memory.grid[y][i].Status = 1
            else:
                "empty cell"
                #self.Memory.grid[y][i].Status = 2
        print "TOP", isBlocked
        return isBlocked


    def checkRightSide(self, ArStr):
        isBlocked = False
       # if (this.X + this.Range + 1 >= this.Env.Grid.GetLength(1))
        #    return True;
        #x = self.X + self.Range + 1

        for i in range(4,6):
            if (ArStr[i] == '1'):
                isBlocked = True
                "explored and has obstacle"
                #self.Memory.grid[self.Y][x].Status = 1
            else:
                "empty cell"
                #self.Memory.grid[self.Y][x].Status = 2
        print "RIGHT", isBlocked
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
        mapStr = self.Dir + x + y
        
        # iterate the map to add value to mapStr
        for i in range (20):
            for j in range (15):
                mapStr += str(self.Memory.grid[i][j].status)
        if (self.X == 1 and self.Y == 1 and self.enteredGoal):
            mapStr += 'F'
        return mapStr