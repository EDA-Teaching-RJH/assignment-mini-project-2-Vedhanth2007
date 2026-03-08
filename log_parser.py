import re

#def check_ip():
    #pattern = 
    #inp = input("Enter ip")
    #p4 = re.compile(pattern)
    #if re.search(p4,inp):
        #print("Valid IP")
    #else:
        #print("Invalid IP")

log_file = "server.log.txt"

with open(log_file, "a") as f:
  f.write("Now the file has more content!")

with open(log_file) as f:
  print(f.read())