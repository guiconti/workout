# 359. Logger Rate Limiter
# Easy

# 333

# 84

# Add to List

# Share
# Design a logger system that receive stream of messages along with its timestamps, each message should be printed if and only if it is not printed in the last 10 seconds.

# Given a message and a timestamp (in seconds granularity), return true if the message should be printed in the given timestamp, otherwise returns false.

# It is possible that several messages arrive roughly at the same time.

class Logger:
  def __init__(self):
    self.hashmap = {}
    self.minimumIntervalBetweenLogs = 10
        
  def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
    if not message in self.hashmap or timestamp - self.hashmap[message] >= self.minimumIntervalBetweenLogs:
      self.hashmap[message] = timestamp
      return True
    return False

# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)