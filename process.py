log_file = open("um-server-01.txt") #opens file to be edited


def sales_reports(log_file): #defines functioin name
    for line in log_file: #loops through the file
        line = line.rstrip() #removes whitespace from text
        day = line[0:3] #selects the portion of the line that makes day a varaiable
        if day == "Mon": # selects what day it is
            print(line) # prints the line


sales_reports(log_file) # runs the sales_report function on the log_file
