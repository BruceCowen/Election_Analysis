# The data we need to retrieve
import csv
import random
import os


file_to_load = os.path.join("Resources", "election_results.csv")


#open txt file with with statement
file_to_save = os.path.join("analysis", "election_analysis.txt")
#Write three counties to the txt file.
with open(file_to_save, "w") as txt_file:
    txt_file.write("Counties in the Election\n----------------------\nArapahoe\nDenver\nJefferson")

#Open the election results and read the file.
with open(file_to_load) as election_data:

    # To do: read and analyze the data here
    file_reader = csv.reader(election_data)

    # Print the header row.
    headers = next(file_reader)
    print(headers)
    
    
# Close the file.

# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote
