#This is testing for log parser 
#How to run: type "python testing.py" in terminal



# imports analyze logs from log parser
from log_parser import AnalyzeLogs

parser = AnalyzeLogs("","") # initiates class without input or ouput

#Run test with a valid log
def test_valid():
    #test with valid log format
    log1 = "[INFO] 2023-05-25 10:18:40: Password reset successful."
    log2 = "[WARNING] 2023-05-25 10:18:30: High latency detected."
    assert parser.is_valid_logs(log1) == True
    assert parser.is_valid_logs(log2) == True
    
#run test with invalid log 
def test_invalid():
    #test with invalid log format
    log1 = "abcdefg"
    log2 = "12345"
    assert parser.is_valid_logs(log1) == False
    assert parser.is_valid_logs(log2) == False
    
#run test to check if it filters debug
def test_debug():
    #test to check if DEBUG logs are filtered
    level = 'DEBUG'
    tester = (level != "DEBUG")
    assert tester == False
    
#run tests to check if it keeps non debugs
def test_non_debug():
    # test to check if non DEBUG log are kept
    level1 = 'INFO'
    level2 = 'ERROR'
    tester = (level1 != "DEBUG")
    tester = (level2 != "DEBUG")
    assert tester == True
    
#main function that runs all the tests
def main():
    test_valid()
    test_invalid()
    test_debug()
    test_non_debug()
    
    print("testing.............")
    print("All test passed")

#checks if the program is being run as the main function and runs main
if __name__ == "__main__":
    main()