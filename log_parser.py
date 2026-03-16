import re

class analyze_logs:
    
  
    def __init__(self,inputfile,outputfile):
        self.inputfile = inputfile
        self.outputfile = outputfile
    
    def parsing(self):
        inf = open("self.inputfile","r")
        outf = open("self.outputfile","w")

        for line in inf:
            if re.search("/^\d{4}-\d{2}-\d{2}$/",line):