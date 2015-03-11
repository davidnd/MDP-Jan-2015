# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
from Cell import *
class Map:
    width = 15
    height = 20
    map1='11'
    map2=''

    def __init__ (self, width, height):
        self.grid = [[0 for x in range(width)] for x in range(height)] 
        for i in range(0,height):
            for j in range (0, width):
                self.grid[i][j] = Cell()
    
    def convertMap(self):
        for i in range (0, Map.height):
            for j in range (0, Map.width):
                if (self.grid[i][j].status != 0):
                    self.map1 += "1"
                    if (self.grid[i][j].status == 1):
                        self.map2 += "1"
                    else:
                        self.map2 += "0"
                else:
                    self.map1 += "0"
        self.map1 += "11"
        while (len(self.map2) % 8 != 0):
            self.map2 += "0"

    def convertToHex(self,s):
        hex = ""
        i=0
        while (i<len(s)):
            i+=4
            temp = s[i,i+4]
            print 'enter'
            if (temp =='0000'):
                hex += "0"
                print 'check 0000'
                continue
            elif (temp =="0001"):
                hex += "1";
                continue
            elif (temp =="0010"):
                hex += "2";
                break
            elif (temp =="0011"):
                hex += "3";
                break
            elif (temp =="0100"):
                hex += "4";
                break
            elif (temp =="0101"):
                hex += "5";
                break
            elif (temp =="0110"):
                hex += "6";
                break
            elif (temp =="0111"):
                hex += "7";
                break
            elif (temp =="1000"):
                hex += "8";
                break
            elif (temp =="1001"):
                hex += "9";
                break
            elif (temp =="1010"):
                hex += "A";
                break
            elif (temp =="1011"):
                hex += "B";
                break
            elif (temp =="1100"):
                hex += "C";
                break
            elif (temp =="1101"):
                hex += "D";
                break
            elif (temp =="1110"):
                hex += "E";
                break
            elif (temp =="1111"):
                hex += "F";
                break
            else:
                break
        return hex