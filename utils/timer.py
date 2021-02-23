import datetime as dt

class timer():
	def __init__(self):
		self.start = None

	def start(self):
		self.start = dt.datetime.now()

	def stop(self):
		end_dt = dt.datetime.now()
		print('Time taken: %s' % (end_dt - self.start_dt))