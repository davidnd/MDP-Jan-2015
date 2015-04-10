import sys
import thread
import time
import threading
import serial
import os

 
class ArduinoConnector(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.queue = queue
        
		self.ser = serial.Serial()
		self.baudrate = 115200
		self.ser = None
	
	def connect(self):
		try:
			print "Trying to connect Arduino..."
			self.ser = serial.Serial('/dev/ttyACM0',self.baudrate, timeout = 2)
			if (self.ser != None):
				print "Connected to Arduino."
				return 1
		except Exception, e:
			print "Error@Arduino Connection: %s" %str(e)
			return 0
 
	def disconnect(self):
		self.ser.close()
 
	def readfromSR(self):
		try:
			msg = self.ser.readline()
			if msg != "":
				print "Read from Arduino: %s" %(msg)
				return msg
		except Exception, e:
				print "Error@Arduino Read: %s" %str(e)
	
		#ser.flushInput()
 
	def writetoSR(self,msg):
		try:
			self.ser.write(msg)
			print "Write to Arduino: %s" %(msg)
		except Exception, e:
				print "Error@Arduino Write: %s" %str(e)
		 
