import datetime as dt

class timer():
	def __init__(self):
		self.start = None

	def start(self):
		self.start = dt.datetime.now()

	def stop(self):
		self.end = dt.datetime.now()
		self.duration = self.end - self.start

	def pretty_print():
		print('Time taken: {}'.format(self.duration))