from log_parser import analyze_logs

def main():
    inputfile = "server.log.txt"
    outputfile = "Parsedfile.txt"

    parser = analyze_logs(inputfile,outputfile)
    parser.parsing()

if __name__ == "__main__":
    main()