# import required modules
import csv
import os

#create lists for calculations
total_votes = 0
candidates = []
vote_counts = []

csvpath = os.path.join('PyPoll/Resources/election_data.csv')
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)
    
    #iterate through data
    for row in csvreader:
        total_votes = total_votes + 1

        #the candidate voted for
        candidate = row[2]

        #if the candidate has other votes then add to total vote
        if candidate in candidates:
            candidate_index = candidates.index(candidate)
            vote_counts[candidate_index] = vote_counts[candidate_index] + 1
        #else create new spot in list for candidate
        else:
            candidates.append(candidate)
            vote_counts.append(1)

    # create list for calculations
    percentages = []
    max_votes = vote_counts[0]
    max_index = 0

    #compute percentage of vote for each candidate and the winner
    for count in range(len(candidates)):
        vote_percentage = vote_counts[count]/total_votes*100
        percentages.append(vote_percentage)
        if vote_counts[count] > max_votes:
            max_votes = vote_counts[count]
            print(max_votes)
            max_index = count
    winner = candidates[max_index]

#print results
print("Election Results")
print("--------------------------")
print(f"Total Votes: {total_votes}")

#round percentages
percentages = [round(i,2) for i in percentages]

for count in range(len(candidates)):
    print(f"{candidates[count]}: {percentages[count]}% ({vote_counts[count]})")
    print("---------------------------")
print(f"Winner: {winner}")

#export results to a text file
output_file = os.path.join("PyPoll","pypoll_output.txt")
output = open(output_file,"w")
output.write("Election Results")
output.write("\n--------------------------")
output.write(f"\nTotal Votes: {total_votes}")
for count in range(len(candidates)):
    output.write(f"\n{candidates[count]}: {percentages[count]}% ({vote_counts[count]})")
output.write("\n---------------------------")
output.write(f"\nWinner: {winner}")