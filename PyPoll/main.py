#import required modules
import csv
import os
csvpath = os.path.join(/Users/Munit/Repository/gwu-arl-data-pt-06-2020-u-c/02-Homework/03-Python/Instructions/PyPoll/Resources/election_data.csv")

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)
   
total_vote=0
array_len=0
candidates_list=[]
total_candidate_vote=[]
candidate_name=0
candidate_vote=[[],[]]

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

index=0
candidate1_name=candidate_vote[0][0]
candidate1_vote=candidate_vote[1][0]
candidate1_vote_percent=0
for x in range(0,array_len):
    if candidate_vote[1][x]>candidate1_vote:
        candidate1_vote=candidate_vote[1][x]
        candidate1_name=candidate_vote[0][x]
        index=x
candidate_vote[1][index]=0   
candidate1_vote_percent=(candidate1_vote/total_vote)*100

index=0
candidate2_name=candidate_vote [0][0]
candidate2_vote=candidate_vote[1][0]
candidate2_vote_percent=0
for y in range(0,array_len):
    if candidate_vote[1][y]>winner_2_vote:
        candidate2_vote=candidate_vote[1][y]
        candidate2_name=candidate_vote[0][y]
        index=y

candidate_vote[1][index]=0      
candidate2_vote_percent=(candidate1_vote/total_vote)*100      

index=0
candidate3_name=candidate_vote[0][0]
candidate3_vote=candidate_vote[1][0]
candidate3_vote_percent=0
for z in range(0,array_len):
    if candidate_vote[1][z]>candidate3_vote:
        candidate3_vote=candidate_vote[1][z]
        candidate3_name=candidate_vote[0][z]
        index=z

candidate_vote[1][index]=0       
candidate3_vote_percent=(candidate3_vote/total_vote)*100  

index=0
candidate4_name=candidate_vote[0][0]
candidate4_vote=candidate_vote[1][0]
candidate4_vote_percent=0
for k in range(0,array_len):
    if candidate_vote[1][k]>winner_4_vote:
        candidate4_vote=candidate_vote[1][k]
        candidate4_name=candidate_vote[0][k]
        index=k
candidate_vote[1][index]=0      
candidate4_vote_percent=(winner_4_vote/total_vote)*100

print("Election Results")
print("-----------------------")
print(f"Total Votes: {int(total_votes)}")    
print("-------------------------")
print(f"{candidate1_name}: {candidate1_vote_percent}% ({candidate1_vote})")
print(f"{candidate2_name}: {candidate2_vote_percent}% ({candidate2_vote})")
print(f"{candidate3_name}: {candidate3_vote_percent}% ({candidate3_vote})")
print(f"{candidate4_name}: {candidate4_vote_percent}% ({candidate4_vote)")
print("---------------------------")
print(f"Winner: {candidate1_name}")
print("----------------------------")