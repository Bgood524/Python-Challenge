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
    counter = 0

    MonthsList = []
    PL_List =[]
    MonthlyChangeList = []


    for row in csvreader:
        
    

        
#Total number of months
        months = months+1
        print("Total Months:" + str(months))
#Total Profit/Losses
        PL_List.append(row[1])
        MonthsList.append(row[0])
        NetTotal = int(NetTotal) + int(row[1])
        print("Total:"+ str(NetTotal))
#Average     

while counter< len(PL_List)-1:
        currentbalance = int(PL_List[int(counter)+1])-int(PL_List[int(counter)])

    