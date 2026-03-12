import re

pattern = r'\[(\w+)\] (\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}): (.*)'

log_file = ["[DEBUG] 2023-05-25 10:15:32: Initializing application...",
    "[INFO] 2023-05-25 10:15:35: User 'John' logged in.",
    "[ERROR] 2023-05-25 10:15:40: Database connection failed.",
    "[DEBUG] 2023-05-25 10:15:45: Processing request...",
    "[INFO] 2023-05-25 10:15:50: Request completed successfully."]

#with open(log_file, "a") as f:
  #f.write("Now the file has more content!")

#with open(log_file) as f:
  #print(f.read())

#class log_entry:
  #def __init__(self,timestamp,msg):
    #self.timestamp = timestamp
    #self.msg = msg

  #def __repr__(self):
    #return f"{self.timestamp}, {self.msg}"

class analyze_logs:
  def log_analyze(log_file):
    checked_logs = []
    for log in log_file:
      match = re.match(pattern, log)
      if match:
        log_lvl = match.group(1)
        time = match.group(2)
        msg = match.group(3)
        if log != 'DEBUG':
          checked_logs.append({'level': log_lvl, 'timestamp': time, 'message': msg})
      else:
        print("Log entry does not match the format expected", log)
      return checked_logs

  analysis = log_analyze(log_file)
  
  for logs in analysis:
    print(analysis)