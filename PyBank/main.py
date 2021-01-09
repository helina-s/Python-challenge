#import required modules
import os
import csv

#create lists to append to
total_months = []
net_profit = []
profit_change = []

csvpath = os.path.join('PyBank/Resources/budget_data.csv')
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")  
    header = next(csvreader)
    
    #iterate values to add to list
    for row in csvreader:
        total_months.append(row[0])
        net_profit.append(int(row[1]))
        
    for i in range(len(net_profit)-1):
        profit_change.append(net_profit[i+1]-net_profit[i])

# review min and max values
increase = max(profit_change)
decrease = min(profit_change)

# check index
monthly_increase = profit_change.index(max(profit_change))+1
monthly_decrease = profit_change.index(min(profit_change))+1

# print results
print("Financial Analysis")
print("-------------------")
print(f"Total Months:{len(total_months)}")
print(f"Total: ${sum(net_profit)}")
print(f"Average Change:{round(sum(profit_change)/len(profit_change),2)}")
print(f"Greatest Increase in Profits: {total_months[monthly_increase]} (${(str(increase))})")
print(f"Greatest Decrease in Profits: {total_months[monthly_decrease]} (${(str(decrease))})")