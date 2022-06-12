# The data we need to retrieve
import csv
import random
import os


file_to_load = os.path.join("Resources", "election_results.csv")


#open txt file with with statement
file_to_save = os.path.join("analysis", "election_analysis.txt")
#Write three counties to the txt file.
#with open(file_to_save, "w") as txt_file:
    #txt_file.write("Counties in the Election\n----------------------\nArapahoe\nDenver\nJefferson")

#initialize variable/accumulator to 0
total_votes = 0

#declare a list for candidate_name
candidate_options = []

#declare dictionary to count votes for each candidate
candidate_votes = {}

winning_candidate = ""
winning_count = 0
winning_percentage = 0

#Open the election results and read the file.
with open(file_to_load) as election_data:

    # To do: read and analyze the data here
    file_reader = csv.reader(election_data)

    # Print the header row.
    headers = next(file_reader)
    print(headers)

    #Print each row in the CSV file.
    for row in file_reader:

        #increment variable total votes by 1
        total_votes += 1
        #get all candidates name
        candidate_name = row[2]

        #add candidate name to list
        #candidate_options.append(candidate_name)

        #if statement to check if name is already on list
        if candidate_name not in candidate_options:
            #add candidates name
            candidate_options.append(candidate_name)
            #set candidate dictionary to 0
            candidate_votes[candidate_name] = 0
            
        #add candidates votes
        candidate_votes[candidate_name] += 1
        

with open(file_to_save,"w") as txt_file:
    election_results = (f"Election Results\n---------------------------\nTotal Votes: {total_votes:,}\n---------------------------\n")
    print(election_results, end="")
    txt_file.write(election_results)

    #for loop to get percentage of total votes
    for candidate_name in candidate_votes:
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_results)
        txt_file.write(candidate_results)

        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name
    winning_candidate_summary = (
        f"---------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"----------------------------\n")
    txt_file.write(winning_candidate_summary)
    print(winning_candidate_summary)



# 3. Print the toal votes.
#print(total_votes)
#print candidate list
#print(candidate_options)
#print candidates votes
#print(candidate_votes)
    
    

    
# Close the file.

# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote
