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
            print "Current X = ", self.X, "Y = ", self.Y
            try:
                isBlockedLeft = self.checkLeftSide(ArStr)
                isBlockedFront = self.checkTopSide(ArStr)
                isBlockedRight = self.checkRightSide(ArStr)
                if (not isBlockedRight):
                    print("Turn right")
                    self.turnRight()
                    self.moveForward(1)
                    return '21'
                elif (not isBlockedFront):
                    print("Move Forward");
                    moved = True
                    self.moveForward(1)
                    return '1'
                elif (not isBlockedLeft):
                    print("turn left");
                    self.turnLeft();
                    self.moveForward(1)
                    return '31'
                else:
                    print("Turn around")
                    self.turnAround()
                    return '4'
            except ValueError as e:
                print(e.Message)
                print(e)
    
    def checkLeftSide(self, ArStr):
        isBlocked = False
        if self.Dir == 'R':
            if(self.Y + self.Range + 1 >= self.Memory.height):
                return True;
        if self.Dir == 'U':
            if(self.X - self.Range - 1 < 0):
                return True;
        if self.Dir == 'L':
            if(self.Y - self.Range - 1 < 0):
                return True;
        if self.Dir == 'D':
            if(self.X + self.Range + 1 >= self.Memory.width):
                return True;

        #x = self.X - self.Range - 1
        if (ArStr[0] == '1'):
            isBlocked = True
            "explored and has obstacle"
            #self.Memory.grid[self.Y][x].Status = 1
            
            if self.Dir =='R':
                self.Memory.grid[self.Y+1][self.X+2].status=1
            elif self.Dir=='U':
                self.Memory.grid[self.Y+1][self.X-2].status=1
            elif self.Dir=='L':
                self.Memory.grid[self.Y-2][self.X-1].status = 1
            else:
                self.Memory.grid[self.Y-1][self.X+2].status=1
        #elif (ArStr[0] == '2'):
            "map second block to have obstacle"
            #self.Memory.grid[][]
        else:
            "empty cell"
            if self.Dir =='R':
                self.Memory.grid[self.Y+1][self.X+2].status=2
            elif self.Dir=='U':
                self.Memory.grid[self.Y+1][self.X-2].status=2
            elif self.Dir=='L':
                self.Memory.grid[self.Y-2][self.X-1].status = 2
            else:
                self.Memory.grid[self.Y-1][self.X+2].status=2
            #self.Memory.grid[self.Y][x].Status = 2
        print "Left", isBlocked
        return isBlocked
    
    def checkTopSide(self, ArStr):
        isBlocked = False
        #if (self.Y + self.Range + 1 >= self.Env.Grid.GetLength(0))
        #    return True;
        # y = self.Y + self.Range + 1
        if self.Dir == 'R':
            if(self.X + self.Range + 1 >= self.Memory.width):
                return True;
        if self.Dir == 'U':
            if(self.Y + self.Range + 1 >= self.Memory.height):
                return True;
        if self.Dir == 'L':
            if(self.X - self.Range - 1 < 0):
                return True;
        if self.Dir == 'D':
            if(self.Y - self.Range - 1 <0):
                return True;

        for i in range(1,4):
            if (ArStr[i]=='1'):
                isBlocked = True
                "explored and has obstacle"
                if self.Dir =='R':
                    self.Memory.grid[self.Y-i+2][self.X+2].status=1
                elif self.Dir=='U':
                    self.Memory.grid[self.Y+2][self.X+i-2].status=1
                elif self.Dir=='L':
                    self.Memory.grid[self.Y+i-2][self.X-2].status = 1
                else:
                    self.Memory.grid[self.Y-2][self.X-i+2].status=1
            else:
                "empty cell"
                if self.Dir =='R':
                    self.Memory.grid[self.Y-i+2][self.X+2].status=2
                elif self.Dir=='U':
                    self.Memory.grid[self.Y+2][self.X+i-2].status=2
                elif self.Dir=='L':
                    self.Memory.grid[self.Y+i-2][self.X-2].status = 2
                else:
                    self.Memory.grid[self.Y-2][self.X-i+2].status=2
        print "TOP", isBlocked
        return isBlocked


    def checkRightSide(self, ArStr):
        isBlocked = False
        if self.Dir == 'R':
            if(self.Y - self.Range - 1 < 0):
                return True;
        if self.Dir == 'U':
            if(self.X + self.Range + 1 >= self.Memory.width):
                return True;
        if self.Dir == 'L':
            if(self.Y + self.Range + 1 >= self.Memory.height):
                return True;
        if self.Dir == 'D':
            if(self.X - self.Range - 1 < 0):
                return True;
        for i in range(4,7):
            if (ArStr[i] == '1'):
                isBlocked = True
                "explored and has obstacle"
                if self.Dir =='R':
                    self.Memory.grid[self.Y-2][self.X-i+5].status=1
                elif self.Dir=='U':
                    self.Memory.grid[self.Y-i+5][self.X+2].status=1
                elif self.Dir=='L':
                    self.Memory.grid[self.Y+2][self.X+i-5].status=1
                else:
                    self.Memory.grid[self.Y+i-5][self.X-2].status = 1
            else:
                "empty cell"
                if self.Dir=='R':
                    self.Memory.grid[self.Y-2][self.X-i+5].status = 2
                elif self.Dir=='U':
                    self.Memory.grid[self.Y-i+5][self.X+2].status = 2
                elif self.Dir=='L':
                    self.Memory.grid[self.Y+2][self.X+i-5].status = 2
                else:
                    self.Memory.grid[self.Y+i-5][self.X-2].status = 2
        print "RIGHT", isBlocked
        return isBlocked

'''    
        def updateMap(self, ArStr):
            for i in range (self.X-1, self.X+2):
                for j in range (self.Y-1, self.Y+2):
                    self.Memory.grid[i][j] = 2
            if self.Dir == 'U':
                self.Memory.grid[]

        public bool checkBottomSide()
        {
            bool isBlocked = False;
            if (this.Y - this.Range - 1 < 0)
                return True;
            int y = this.Y - this.Range - 1;
            for (int i = this.X - this.Range; i <= this.X + this.Range; i++)
            {
                if (this.Env.Grid[y, i].Status == 1)
                {
                    isBlocked = True;
                    //explored and has obstacle
                    this.Memory.Grid[y, i].Status = 1;
                }
                else
                {
                    //empty cell
                    this.Memory.Grid[y, i].Status = 2;
                }
            }
            return isBlocked;
        }
        '''

'''
    def scanFront(self,ArInQ):
        if self.Dir== 'R':
            return self.checkRightSide(ArInQ);
        elif self.Dir== 'L':
            return self.checkLeftSide(ArInQ);
        elif self.Dir== 'U':
            return self.checkTopSide(ArInQ);
        #elif self.Dir== 'D':
         #   return self.checkBottomSide(ArInQ);
        else:
            return True;

    def scanLeft(self,ArInQ):
        if self.Dir== 'R':
            return self.checkTopSide(ArInQ);
        #elif self.Dir== 'L':
         #   return self.checkBottomSide(ArInQ);
        elif self.Dir== 'U':
            return self.checkLeftSide(ArInQ);
        elif self.Dir== 'D':
            return self.checkRightSide(ArInQ);
        else:
            return True

    def scanRight(self,ArInQ):
       # if self.Dir == 'R':
        #    return self.checkBottomSide(ArInQ);
        if self.Dir== 'L':
            return self.checkTopSide(ArInQ);
        elif self.Dir== 'U':
            return self.checkRightSide(ArInQ);
        elif self.Dir== 'D':
            return self.checkLeftSide(ArInQ);
        else:
            return True


    def mapLeft(self):
        if self.Dir == 'R':
            self.Memory.grid[self.X][self.Y]
        if self.Dir== 'L':
            return self.checkTopSide(ArInQ);
        elif self.Dir== 'U':
            return self.checkRightSide(ArInQ);
        elif self.Dir== 'D':
            return self.checkLeftSide(ArInQ);
        else:
            return True
'''