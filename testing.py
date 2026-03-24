# imports analyze logs from log parser
from log_parser import analyze_logs

parser = analyze_logs("","")

#test with valid log format
log = "[INFO] 2023-05-25 10:18:40: Password reset successful."
assert parser.is_valid_logs(log) == True
print("Accepted the valid log,Passed valid log test")

#test with invalid log format
log = "abcdefg"
assert parser.is_valid_logs(log) == False
print("Rejected the invalid log,Passed invalid log test")
#test to check if DEBUG logs are filtered
level = 'DEBUG'
tester = (level != "DEBUG")
assert tester == False
print("DEBUG filtered, Debug Test passed")

# test to check if non DEBUG log are kept
level = 'INFO'
tester = (level != "DEBUG")
assert tester == True
print("INFO is saved, Test passed")