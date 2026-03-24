import re #imported regex
from log_entry import log_entry,Errorlogs # imported log_entry and errorlogs from log_entry.py

class analyze_logs: #class that processes log files
    
    # makes a path for the input and output file
    def __init__(self,inputfile,outputfile):
        self.inputfile = inputfile
        self.outputfile = outputfile
    
    # function that parses files, filters logs and read/write to files
    def parsing(self):
        total = 0 #counts non debug logs
        error = 0 #counts error logs
        
        # open input and output files for reading and writing
        with open(self.inputfile,"r") as inf, open(self.outputfile,"w") as outf, open("Errorfile.txt", "w") as e: 
            
            #loops through each line in the input file
            for line in inf:

                # uses the regex pattern to find timestamp,level and message
                match = re.search(r'\[(\w+)\] (\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}): (.*)', line) 
                if match:
                    groups = match.groups()

                    #the logs are split into parts after they are extracted
                    timestamp = groups[1]
                    level = groups[0]
                    message = groups[2]

                    # checks if the level is "ERROR"
                    # if true , then it would write to an error log and increase the error count by one
                    if level == 'ERROR':
                        entry = Errorlogs(timestamp,level,message)
                        e.write(str(entry) + "\n")
                        error = error + 1
                    else:
                        entry = log_entry(timestamp,level,message)
                    
                    # filters out any logs that are of the level "DEBUG" and increases count of total by one
                    if level != 'DEBUG':
                        outf.write(str(entry) + "\n")
                        total = total + 1
                        
                    else:
                        pass
            # summaries how many log there are in the output file            
            outf.write("\n~~~~~LOG SUMMARY~~~~~\n")
            outf.write(f"Total logs: {total}\n")
            outf.write(f"Total error log: {error}\n")
    # validates if the log is valid
    def is_valid_logs(self,line):
        # uses regex to check the format of the log
        match = re.match(r'\[(\w+)\] (\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}): (.*)', line)
        if match:
            return True
        else:
            return False
