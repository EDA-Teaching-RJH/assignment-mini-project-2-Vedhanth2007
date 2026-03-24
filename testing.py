import re
from log_parser import analyze_logs

parser = analyze_logs("","")

log = "[INFO] 2023-05-25 10:18:40: Password reset successful."
assert parser.is_valid_logs(log) == True
print("Accepted the valid log,Passed valid log test")

log = "abcdefg"
assert parser.is_valid_logs(log) == False
print("Rejected the invalid log,Passed invalid log test")

level = 'DEBUG'
tester = (level != "DEBUG")
assert tester == False
print("DEBUG filtered, Debug Test passed")

level = 'INFO'
tester = (level != "DEBUG")
assert tester == True
print("INFO is saved, Test passed")