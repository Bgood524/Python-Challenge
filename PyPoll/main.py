import os
import csv

csvpath = os.path.join('Resources','election_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter =",")
    print(csvreader)

    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    
    candidates = []


    
    for row in csvreader:
        candidate = row[2]
        candidates.append(candidate)