from log_parser import analyze_logs #imports analyze_logs from log_parser.py

def main(): #main function that runs the program
    # input and output file are stored
    inputfile = "server.log.txt"
    outputfile = "Parsedfile.txt"

    # instance for analyze_logs
    parser = analyze_logs(inputfile,outputfile)
    parser.parsing() # calls the parsing function in log_parser

if __name__ == "__main__": # checks if the program is running as the main one
    main()