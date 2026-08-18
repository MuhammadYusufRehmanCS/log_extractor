import csv
from pathlib import Path
from datetime import datetime


errors = ["ERROR", "error", "Error", "CRITICAL", "critical", "Critical", "FATAL", "fatal", "Fatal",
           "EXCEPTION", "exception", "Exception", "info", "INFO", "Info", "WARNING", "warning", "Warning",
             "DEBUG", "debug", "Debug"]
status = ["404", "500", "502", "503", "504", "401", "403", "400", "422", "429"]

log_file = Path('.log')

with open('log_errors.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(["Timestamp", "Error Level", "Message", "Status Code"])
    if log_file.exists():
        with open(log_file, 'r') as file:
            for line in file:
                line = line.strip()
                parts = line.split(" ")
                timestamp = parts[0] # "2026-08-16T14:23:05.901Z"
                error = parts[1] # "ERROR"
                error = error.strip("[]")
                message = " ".join(parts[5:]) # "Message" failure to get message content as we use split
                message = message.replace('msg=', '')
                formatted_message = message.replace('"', '')
                status_code = parts[4] # "404"
                status_code = status_code.replace("status=", "")
                csvwriter.writerow([timestamp, error, formatted_message, status_code])
        
    else:
        print("Log file not found.")
        csvwriter.writerow(['Timestamp', 'Error', 'Message', 'Status Code']) 
    