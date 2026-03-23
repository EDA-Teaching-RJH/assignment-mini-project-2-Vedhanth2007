import re
from log_entry import log_entry,Errorlogs

class analyze_logs:
    
  
    def __init__(self,inputfile,outputfile):
        self.inputfile = inputfile
        self.outputfile = outputfile
    
    def parsing(self):
        #clean_logs = []
        with open(self.inputfile,"r") as inf, open(self.outputfile,"w") as outf, open("Errorfile.txt", "w") as e:
        
            for line in inf:
                match = re.search(r'\[(\w+)\] (\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}): (.*)', line) 
                if match:
                    groups = match.groups()

                    timestamp = groups[1]
                    level = groups[0]
                    message = groups[2]

                    
                    if level == 'ERROR':
                        entry = Errorlogs(timestamp,level,message)
                        e.write(str(entry) + "\n")
                    else:
                        entry = log_entry(timestamp,level,message)
                    
                    
                    if level != 'DEBUG':
                        outf.write(str(entry) + "\n")
                        #clean_logs.append(str(entry))
                    else:
                        pass

        #return clean_logs
