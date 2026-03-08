import re

pattern = 

log_file = "server.log.txt"

with open(log_file, "a") as f:
  f.write("Now the file has more content!")

with open(log_file) as f:
  print(f.read())

class log_entry:
  def __init__(self,timestamp,msg):
    self.timestamp = timestamp
    self.msg = msg

  def __repr__(self):
    return f"{self.timestamp}, {self.msg}"

class analyze_logs:
  checked_logs = []
  for log in #####:
    match = re.match()