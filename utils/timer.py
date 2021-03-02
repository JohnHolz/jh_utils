from datetime.datetime import now()

class Timer():    
    def __init__(self, start_now = False):
        if start_now:
            self.start()

    def start(self):
        if hasattr(x,'start_time'):
            print('Started at: {}'.format(self.start_time))
        else:
            self.start_time = dt.now()
    
    def stop(self):
        if hasattr(x,'stop_time'):
            print('Stopped at: {}'.format(self.stop_time))
        else:
            self.stop_time = dt.now()
            self.duration = self.stop_time - self.start_time