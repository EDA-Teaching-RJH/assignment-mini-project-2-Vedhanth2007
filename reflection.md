# REFLECTION
## Overview 
In this mini project 2 assignment I chose to a log parser.This program of mine would read from a server file, parse through the logs using regular expression and write to an output file. To read and write I used file i/o. I used object oriented programming to structure the code. I not only used the lecture slides from moodle but also got help from websites like reddit,stackoverflow, w3 school, geeksforgeeks etc.

## Regular expression
I learnt how to use regex because of w3school. I used `re.search` and `re.match` to extract the info. The regex pattern I used allowed me to extract the timestamp,level and message if they matched.

## Testing
I implemented testing using `assert` statement I learnt in lecture 8, it verifies that my validation functions work as intended. I tested both a valid and invalid aswell as another conditions like DEBUG. This helps me ensure my program runs without errors.

## Libraries
From lecture 7 I learnt that libraries provide additional functionality that is not offered in base python. In my code I added the in built library `re` for regular experssions and made my own module called log_entry.py. This shows my understand of libraries.

## File I/O
In Lecture 8 I was introduced to file handling, I read and wrote to files using `with open()` and I set what mode the files are in using `'r'` and `'w'`. I applied this by reading from server log and writing to an output file and a seperate error log file. I also made the logs are formatted properly by using "\n"

## Object-Oriented Programming (OOP)
I used my knowledge of classes and inheritance from lectures 9 to apply object oriented programming. In my code I made a class called `log_entry` to represent logs one by one and I also made a child class `Errorlogs` that inherits abilities from its parent. 

## Extension
To add on top of existing abilities I made my program parse logs and if it found logs with a level of "ERROR" it would put them in a seperate output file of its own. On top of this I made my code count the total number of logs that are not of the level "DEBUG" and count the number of logs that are of level "ERROR" , then it would get written in the output file after the log have been parsed. This will be helpful because it shows statistic about the output file.

## Conclusion
Overall this project helped me learn and apply these concepts. I used concepts from lectures and other online media like youtube , w3school etc to help me with the syntax of my code.I used regex for matching patterns , File IO for storing data, assertation for testing and OOP for program structure. I had to overcome the challenge of OOP and how to use class across different python files using websites like geeksforgeeks ,w3school , stackoverflow and youtube. I also add extra functionality such data stats to prove my understanding of python and the project requirments. I was also planning to add a progress bar in my python code using the library `tqdm` but decided not to because it does not improve the functionality of the program. I was also using `__repr__` in log_entry but changed my mind because I read `__str__` is better for printing outputs.

## Video link 
I have also uploaded the video with the rest of the files incase the link does not work[Watch video here](https://drive.google.com/file/d/1RjYPAy7pLvJJfyeebt3RvctDLCimpSfB/view?usp=sharing)