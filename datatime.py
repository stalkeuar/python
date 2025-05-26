import sys
import datetime

def log(message):
    timestamp = datetime.datetime.now()
    sys.stderr.write("[" + str(timestamp) + "]" + " " + message + "\n")
    
log('Test log message')
