# Python Homework PyPoll
#In this challenge, you are tasked with helping a small, rural town modernize its vote-counting process. (Up until now, Uncle Cleetus had been trustfully tallying them one-by-one, but unfortunately, his concentration isn't what it used to be.)
#You will be given two sets of poll data (`election_data_1.csv` and `election_data_2.csv`). Each dataset is composed of three columns: `Voter ID`, `County`, and `Candidate`. Your task is to create a Python script that analyzes the votes and calculates each of the following:
#The total number of votes cast
#A complete list of candidates who received votes
#The percentage of votes each candidate won
#The total number of votes each candidate won
#The winner of the election based on popular vote.

# Modules
import csv
import os

# Set path for file
csvpath = os.path.join("C:\\Users\\Alain\\GWDC201805DATA3-Class-Repository-DATA\\Homework\\03-Python\\Instructions\\PyPoll\\raw_data\\", "election_data_1.csv")

# Create output file name
output_file = "C:/Users/Alain/GWDC201805DATA3-Class-Repository-DATA/Unit_3_Assignment/python-challenge/PyPoll/election_data_1.txt"  


# Total Vote Counter
total_votes = 0

# Candidate Options and Vote Counters
candidate_options = []
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0

# Read the csv and convert it into a list of dictionaries
with open(csvpath) as election_data:
    reader = csv.DictReader(election_data)

    # For each row...
    for row in reader:

        

        # Total number of votes cast
        total_votes = total_votes + 1

        # Extract the candidate name from each row
        candidate_name = row["Candidate"]

        
        if candidate_name not in candidate_options:

            # Add it to the list of candidates in the running
            candidate_options.append(candidate_name)

            # And begin tracking that candidate's voter count
            candidate_votes[candidate_name] = 0

        # Then add a vote to that candidate's count
        candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1

# Print the results and export the data to our text file
with open(output_file, "w") as txt_file:

    # Determine the winner by looping through the counts
    for candidate in candidate_votes:

        # Retrieve vote count and percentage
        votes = candidate_votes.get(candidate)
        vote_percentage = float(votes) / float(total_votes) * 100

        # Determine winning vote count and candidate
        if (votes > winning_count):
            winning_count = votes
            winning_candidate = candidate

        # Generate Output Summary
output_1 = (
    f"\nElection Results\n"
    f"----------------------------\n"
    f"The total number of votes cast: {total_votes}\n"
    f"A complete list of candidates who received votes: {candidate_votes}\n"
    f"Each Candidate voter percentage and counts {candidate}: {vote_percentage:.3f}% ({votes})\n"
    f"The total number of votes each candidate won: {votes}\n"
    f"The winner of the election based on popular vote: {winning_candidate}\n")

# Print the output (to terminal)
print(output_1)

# Export the results to text file
with open(output_file, "w") as txt_file:
    txt_file.write(output_1)

# Python Homework PyPoll
#In this challenge, you are tasked with helping a small, rural town modernize its vote-counting process. (Up until now, Uncle Cleetus had been trustfully tallying them one-by-one, but unfortunately, his concentration isn't what it used to be.)
#You will be given two sets of poll data (`election_data_1.csv` and `election_data_2.csv`). Each dataset is composed of three columns: `Voter ID`, `County`, and `Candidate`. Your task is to create a Python script that analyzes the votes and calculates each of the following:
#The total number of votes cast
#A complete list of candidates who received votes
#The percentage of votes each candidate won
#The total number of votes each candidate won
#The winner of the election based on popular vote.

# Modules
import csv
import os

# Set path for file
csvpath_2 = os.path.join("C:\\Users\\Alain\\GWDC201805DATA3-Class-Repository-DATA\\Homework\\03-Python\\Instructions\\PyPoll\\raw_data\\", "election_data_2.csv")

# Create output file name
output_file_2 = "C:/Users/Alain/GWDC201805DATA3-Class-Repository-DATA/Unit_3_Assignment/python-challenge/PyPoll/election_data_2.txt"  


# Total Vote Starting point
total_votes = 0

# Candidate Options and Vote Counters
candidate_options = []
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0

# Read the csv and convert it into a list of dictionaries
with open(csvpath_2) as election_data_2:
    reader = csv.DictReader(election_data_2)

    # For each row...
    for row in reader:

        

        # Total number of votes cast
        total_votes = total_votes + 1

        # Extract the candidate name from each row
        candidate_name = row["Candidate"]

        
        if candidate_name not in candidate_options:

            # Add it to the list of candidates in the running
            candidate_options.append(candidate_name)

            # And begin tracking that candidate's voter count
            candidate_votes[candidate_name] = 0

        # Then add a vote to that candidate's count
        candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1

# Print the results and export the data to our text file
with open(output_file_2, "w") as txt_file:

    # Determine the winner by looping through the counts
    for candidate in candidate_votes:

        # Retrieve vote count and percentage
        votes = candidate_votes.get(candidate)
        vote_percentage = float(votes) / float(total_votes) * 100

        # Determine winning vote count and candidate
        if (votes > winning_count):
            winning_count = votes
            winning_candidate = candidate

        # Generate Output Summary
output_2 = (
    f"\nElection Results\n"
    f"----------------------------\n"
    f"The total number of votes cast: {total_votes}\n"
    f"A complete list of candidates who received votes: {candidate_votes}\n"
    f"Each Candidate voter percentage and counts {candidate}: {vote_percentage:.3f}% ({votes})\n"
    f"The total number of votes each candidate won: {votes}\n"
    f"The winner of the election based on popular vote: {winning_candidate}\n")

# Print the output (to terminal)
print(output_2)

# Export the results to text file
with open(output_file_2, "w") as txt_file:
    txt_file.write(output_2)