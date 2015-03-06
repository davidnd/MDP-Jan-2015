import thread
import time
import Queue

from interface import *
from pc_interface import *
from android_interface import *
from arduino_interface import *

#algo 
from Map import *
from Robot import *

class Main:
        def __init__(self):
                #Initialize Queues
                self.toAndroid = Queue.Queue(maxsize=0)
                self.toRobot = Queue.Queue(maxsize=0)
                self.toPC = Queue.Queue(maxsize=0)
                self.toAlgo = Queue.Queue(maxsize=0)
                
                #Create interface objects
                self.bt = android_interface()
                self.pc = pc_interface()
                self.robot = arduino_interface()


        def connectBT(self):
                #connect bluetooth
                connected = 0
                while connected == 0:
                        self.bt.disconnect()
                        time.sleep(1)
                        connected = self.bt.connect()

        def connectPC(self):
                #connect PC
                connected = 0
                connected = self.pc.connect()
                while connected == 0:
                        self.pc.disconnect()
                        time.sleep(1)
                        connected = self.pc.connect()

        def connectArduino(self):    
                #connect arduino
                connected = 0
                connected = self.robot.connect()
                while connected == 0:
                        time.sleep(1)
                        connected = self.robot.connect()


        #sending data to algo from queue
        def activateAlgo(self, algoQ, robotQ, androidQ):
                robot = Robot(1,1,1,'U')
                map=Map(15,20)
                while 1:
                        if not algoQ.empty():
                                val = algoQ.get_nowait()
                                #call algo
                                out = robot.explore(val)
                                #time.sleep(2)
                                
                                robotQ.put_nowait(out)
                                #androidQ.put_nowait(out)

                
        #sending data to android from queue
        def btWrite(self, androidQ):
                while 1:
                        if not androidQ.empty():
                                val = androidQ.get_nowait()
                                self.bt.writetoBT(val)                             

        #reading android value, send data to arduino (and/or pc).
        def btRead(self, robotQ, pcQ, algoQ):
                while 1:
                        val = self.bt.readfromBT()
                        if val is not None:
                                #robotQ.put_nowait(val)
                                #algoQ.put_nowait(val) #testing
                                pcQ.put_nowait(val)

        #sending data to PC from PC msg queue.
        def pcWrite(self, pcQ):
                while 1:
                        if not pcQ.empty():
                                val = pcQ.get_nowait()
                                self.pc.writetoPC(val)

        #reading data from PC, send data to arduino.
        def pcRead(self, robotQ):
           while 1:
                   val = self.pc.readfromPC()
                   #robotQ.put(val.partition("\n")[0])
                   if val is not None:
                           robotQ.put_nowait(val)

        #sending data to arduino from arduino msg queue.
        def robotWrite(self, robotQ):
           time.sleep(2)
           robotQ.put_nowait("h")
           while 1:
                  if not robotQ.empty():
                         val = robotQ.get_nowait()
                         self.robot.writetoSR(val + "\n")
                 
        #reading data from arduino to ALGO & android.
        def robotRead(self, pcQ, androidQ, algoQ):
           #time.sleep(2)
           #val = self.robot.readfromSR()
           #val = self.robot.readfromSR()
           while 1:
                   val = self.robot.readfromSR()
                   if val is not None:
                           #androidQ.put_nowait(val)
                           algoQ.put_nowait(val)
                           #pcQ.put(val)
                 
        #starting all thread.
        def startThread(self):
                try:
                        thread.start_new_thread( self.btWrite, (self.toAndroid,))
                        thread.start_new_thread( self.btRead, (self.toRobot, self.toPC, self.toAlgo))
                        thread.start_new_thread( self.pcWrite, (self.toPC,))
                        thread.start_new_thread( self.pcRead, (self.toRobot,))
                        #thread.start_new_thread( self.robotWrite, (self.toRobot,))
                        #thread.start_new_thread( self.robotRead, (self.toPC, self.toAndroid, self.toAlgo))
                        #thread.start_new_thread( self.activateAlgo, (self.toAlgo, self.toRobot, self.toAndroid))

                except Exception, e:
                        print "Unable to start thread!"
                        print "Error: %s" %str(e) 
                while 1:
                   pass
           
test = Main()
test.connectBT()
#test.connectArduino()
test.connectPC()
test.startThread()
