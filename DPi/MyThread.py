import threading
import time

class MyThread(threading.Thread):
	
	def __init__(self, threadID, name, queue):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.name = name
		self.queue = queue
	def  run(self):
		print "starting thread " + self.name
		process_data

	def process_data(self):
		
		