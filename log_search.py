import os
import time

# Python script that will go through all .log files in a directory and 
# find a specifc search term. Can also specify a date and/or hour to
# narrow the search. Date and hour uses YYYY-MM-DD and HH format 
# (2017-05-01 and/or 03). When specifying hour, it searches starting at
# that hour to the end of the file

searchTerm = raw_input('Search term: ')
logDate    = raw_input('Day (enter for today): ') or time.strftime("%Y-%m-%d")

hourDescision = raw_input('Include hour? (y/N) ').lower()
logHour       = 'n'

if hourDescision == 'y':
    logHour = raw_input('Hour: ') + ':'

currentDirectory = os.getcwd()

# get .log files of current directory
files = [f for f in os.listdir(currentDirectory) if f.endswith('.log')]

for filename in files:
    with open(currentDirectory + '/' + filename) as currentFile:
        # loop through lines
        for line in currentFile: 
            if hourDescision == 'y':    
                logDateAndHour = logDate + ' ' + logHour
                # find specific date hour first
                if (logDateAndHour in line):
                    for line in currentFile:
                        # continue and find search term
                        if (searchTerm in line):
                            print(filename.split('.')[0])
                            break
                    break
            else:
                # find specific date first
                if (logDate in line):
                    for line in currentFile:
                        # continue and find search term
                        if (searchTerm in line):
                            print(filename.split('.')[0])
                            break
                    break