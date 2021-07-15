#Print the budget data csv file
import os
import csv
from typing import Counter

csvpath = os.path.join('Resources', 'budget_data.csv')
print(csvpath)




with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    months = 0
    NetTotal = 0
    MonthlyChangeSum = 0

    MonthsList = []
    PLChangeList =[]
    

    for row in csvreader:
        
    

        
#Total number of months
        months+=1
        print("Total Months:" + str(months))
#Total Profit/Losses
        NetTotal += int(row[1])
        print("Total:"+ str(NetTotal))
#Average     

while MonthlyChangeSum> 0:
    currentbalance = int()
Average = NetTotal/months
print("Average Change:"+ str(Average))
#Increase/Decrease
print(int(row[2])-int(row[1]))
