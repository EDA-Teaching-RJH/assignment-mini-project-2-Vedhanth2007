import re
from log_entry import log_entry # check if this the right way to import

class analyze_logs:
    
  
    def __init__(self,inputfile,outputfile):
        self.inputfile = inputfile
        self.outputfile = outputfile
    
    def parsing(self):
        with open(self.inputfile,"r") as inf, open(self.outputfile,"w") as outf:
        
            for line in inf:
                match = re.match(r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (\w+) (\w+)', line) # can use re.search check how to use them
                if match:
                    groups = match.groups()

                    timestamp = groups[0]
                    level = groups[1]
                    message = groups[2]

                    outf.write(timestamp)
                    outf.write(level)
                    outf.write(message)