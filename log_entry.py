# class for log_entry
class log_entry:
    # initalises a log entry and puts them into different attributes
    def __init__(self,timestamp,level,message):
        self.timestamp = timestamp
        self.level = level 
        self.message = message
    # returns log entry as a readable line
    def __str__(self):
        return f"{self.timestamp},{self.level},{self.message}"
# child class of log entry
class Errorlogs(log_entry):
    def is_error(self):
        if self.level == "ERROR": # checks if the level is an "ERROR"
            return True
        else:
            return False