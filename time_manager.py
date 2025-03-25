import time

class TimeManager:
    def __init__(self, time_limit):
        self.start_time = time.time()
        self.time_limit = time_limit 

    def check_time_remaining(self):
        elapsed_time = time.time() - self.start_time
        return self.time_limit - elapsed_time 

    def is_time_expired(self):
        return self.check_time_remaining() <= 0