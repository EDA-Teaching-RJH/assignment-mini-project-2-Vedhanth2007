import re
from log_entry import log_entry # check if this the right way to import

class analyze_logs:
    
  
    def __init__(self,inputfile,outputfile):
        self.inputfile = inputfile
        self.outputfile = outputfile
    
    def parsing(self):
        clean_logs = []
        with open(self.inputfile,"r") as inf, open(self.outputfile,"w") as outf:
        
            for line in inf:
                match = re.search(r'\[(\w+)\] (\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}): (.*)', line) # can use re.search check how to use them
                if match:
                    groups = match.groups()

                    timestamp = groups[1]
                    level = groups[0]
                    message = groups[2]

                    #outf.write(timestamp)
                    #outf.write(level)
                    #outf.write(message)
                    #outf.write(f"{timestamp},{level},{message}\n")

                    if level != 'DEBUG':
                        outf.write(f"{timestamp},{level},{message}\n")
                        clean_logs.append({'level': level, 'timestamp': timestamp, 'message': message})
        return clean_logs