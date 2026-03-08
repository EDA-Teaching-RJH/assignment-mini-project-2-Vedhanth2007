import re

def check_ip():
    pattern = ("r^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$")
    inp = input("Enter ip")
    p4 = re.compile(pattern)
    if re.search(p4,inp):
        print("Valid IP")
    else:
        print("Invalid IP")