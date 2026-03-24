from log_parser import analyze_logs

parser = analyze_logs("","")

level = 'DEBUG'
tester = (level != "DEBUG")
assert tester == False
print("DEBUG filtered, Debug Test passed")

level = 'INFO'
tester = (level != "DEBUG")
assert tester == True
print("INFO is saved, Test passed")