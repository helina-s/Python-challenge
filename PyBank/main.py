#import required modules
import csv
import os

csvpath = os.path.join("/Users/Munit/Repository/gwu-arl-data-pt-06-2020-u-c/02-Homework/03-Python/Instructions/PyBank/Resources/budget_data.csv")
#open CSV files
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #print(csvreader)
#skip the header (first row)
    csv_header = next(csvreader)
#total number of months
    total_months = len(list(csvreader))
    
with open(csvpath) as csvfile:
    reader = csv.DictReader(csvfile)
    rows = list(reader)
    total = sum(float(row["Profit/Losses"]) for row in rows)
    average = total/total_months
    greatest_increase = max(int(row["Profit/Losses"]) for row in rows)
    greatest_decrease = min(int(row["Profit/Losses"]) for row in rows)

    total_months += 1
    month_of_change += [row[0]]
  
print("Financial Analysis")
print("--------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total}")
print(f"Average Change: ${round(average, 2)}")
print(f"Greatest Increase in Profits: ${greatest_increase}")
print(f"Greatest Decrease in Profits: ${greatest_decrease}")

output = os.path.join("budget_data" "budget_analysis.txt")
with open ("output", "w") as text_file:
    text_file.write(output)

    text_file.write("Financial Analysis\n")
    text_file.write("--------------------------\n")
    text_file.write(f"Total Months: {total_months}\n")
    text_file.write(f"Total: ${total}\n")
    text_file.write(f"Average Change: ${round(average, 2)}\n")
    text_file.write(f"Greatest Increase in Profits: ${greatest_increase}\n")
    (f"Greatest Decrease in Profits: ${greatest_decrease}\n")