# In this challenge, you are tasked with helping a small, rural town modernize its vote-counting process. (Up until now, Uncle Cleetus had been trustfully tallying them one-by-one, but unfortunately, his concentration isn't what it used to be.)

# You will be given a set of poll data called election_data.csv. The dataset is composed of three columns:
# Voter ID, County, and Candidate. Your task is to create a Python script that analyzes the votes and calculates each of the following:


# The total number of votes cast **add to total starting at zero
# A complete list of candidates who received votes ** row 2 unique values 
# The percentage of votes each candidate won **
# The total number of votes each candidate won
# The winner of the election based on popular vote.


# As an example, your analysis should look similar to the one below:


#   Election Results
#   -------------------------
#   Total Votes: 3521001
#   -------------------------
#   Khan: 63.000% (2218231)
#   Correy: 20.000% (704200)
#   Li: 14.000% (492940)
#   O'Tooley: 3.000% (105630)
#   -------------------------
#   Winner: Khan
#   -------------------------

# In addition, your final script should both print the analysis to the terminal and export a text file with the results.

import os
import csv

csvpath = os.path.join('election_data.csv')

with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    #print(csvreader)

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    #print(f"CSV Header:{csv_header}")
   
   #Set variables 
    row_count = 0
    candidates_votes = {}
   

    # Read each row of data after the header to get total number of votes row_count = total votes
    for row in csvreader:
        row_count+= 1
        candidate_name = row[2]
        
        if candidate_name in candidates_votes:
            candidates_votes[candidate_name] +=1
        else:
            candidates_votes[candidate_name] = 1

    # create a list for the output to make it easier    

    elections = [
        "Election Results",
        "-------------------------",
        f"Total Votes: {row_count}",
        "-------------------------"
    ]

    winner = ""

    for candidate_name, total_votes in candidates_votes.items():
        # print(candidate_name, total_votes)
        # calculate percentage of votes for each candidate, round to 3 decimals
        percentage_votes = total_votes /row_count
        # create string output for each candidate
        candidate_string = f"{candidate_name}: {percentage_votes:.3%} ({str(total_votes)})"
        elections.append(candidate_string)
        if winner == "":
            winner = candidate_name
        elif candidates_votes[winner] < total_votes:
            winner = candidate_name
    elections.append("-------------------------")
    elections.append(f"Winner: {winner}")
    elections.append("-------------------------")
    
 
#print verything in financia_analysis and separate each item in a this list by a new line
print(*elections, sep = "\n")

#write into text file
with  open("PyPoll.txt","w") as textfile:
    print(*elections, sep = "\n", file = textfile)
    