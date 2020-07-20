#import required modules
import csv
import os

csvpath = os.path.join("/Users/Munit/Repository/gwu-arl-data-pt-06-2020-u-c/02-Homework/03-Python/Instructions/PyPoll/Resources/election_data.csv")
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    total_votes = len(list(csvreader))
    print(total_votes)
    