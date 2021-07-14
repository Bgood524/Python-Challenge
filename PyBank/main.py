#Print the budget data csv file
import os
import csv
from typing import Counter

csvpath = os.path.join('Resources', 'budget_data.csv')
print(csvpath)

month = []


with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    months = 0
    NetTotal = 0
    for row in csvreader:
        
    

        
#Total number of months
        months+=1
        print(months)
#Total Profit/Losses
