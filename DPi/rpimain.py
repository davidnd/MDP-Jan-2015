import threading
import time
import Queue

import Robot 
import AnduinoConnector
import AndroidConnector
import PCConnector

class Main():
	"""docstring for Main"""
	def __init__(self):
		self.AndroidQ = Queue.Queue(maxsize = 0)
		self.PCQ = Queue.Queue(maxsize = 0)
		self.AlgoQ = Queue.Queue(maxsize = 0)
		self.robot = Robot()
		self.androidConnector = AndroidConnector()
		self.pcConnector = PCConnector()
		self.arduinoConnector = AndroidConnector()
		