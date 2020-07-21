#import required modules
import csv
import os
csvpath = os.path.join("/Users/Munit/Repository/gwu-arl-data-pt-06-2020-u-c/02-Homework/03-Python/Instructions/PyPoll/Resources/election_data.csv")

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)
   
total_vote=0
array_len=0
candidates_list=[]
total_candidate_vote=[]
candidate_name=0

with open (csvpath) as csvfile:
    csvreader=csv.reader(csvfile)
    csv_header = next(csvreader)
    
    for row in csvreader:
        total_votes += 1
        candidates_list.append(str(row[2]))
        array_len=len(candidates_list)
        
for votes in range(0,array_len):
    with open (csvpath) as csvfile:
        csvreader=csv.reader(csvfile)
        csv_header = next(csvfile)
        total_vote=0
        for row in csvreader:
            if row[2]==candidates_list[votes]:
                total_vote = total_votes + int(row[0])
                total_candidate_vote.append(total_vote)

for votes in range(0,array_len):
    candidate_vote[0].append(candidates_list[votes])
    candidate_vote[1].append(total_candidate_vote [votes])
