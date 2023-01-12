import csv
import os

input_file = os.path.join("Resources/election_data.csv")
output_file = os.path.join("Analysis","election_analysis.txt")

Total_Votes = 0
Candidates_List = []
Candidates_Votes = {}
Winning_Count= 0

with open(input_file) as file:
    csvreader = csv.reader(file)
    # file has a header, code below to exclude 
    header = next(csvreader)

    for line in csvreader:
        Total_Votes += 1
        Candidate_Name = line[2]

        #if statement for listing all 3 candidates
        if Candidate_Name not in Candidates_List:
            Candidates_List.append(Candidate_Name)
            Candidates_Votes[Candidate_Name] = 0
        
        #adding all votes for each candidate
        Candidates_Votes[Candidate_Name] += 1
        
with open(output_file,'w') as file:
    Election_Outlook = f"""
Election Results
-------------------------
Total Votes: {Total_Votes}
-------------------------
"""
    print(Election_Outlook)
    file.write(Election_Outlook)

    for Candidate in Candidates_Votes:
        Count = Candidates_Votes.get(Candidate)
        Candidates_Percentage =  Count/Total_Votes*100

        if Count > Winning_Count:
            Winning_Count = Count
            Winner = Candidate

        Candidate_Outlook = f"{Candidate}: {Candidates_Percentage:.3f}% ({Count})\n"
        print(Candidate_Outlook)
        file.write(Candidate_Outlook)

    Winner_Outlook = f"""-------------------------
Winner: {Winner}
-------------------------
"""
    print(Winner_Outlook)
    file.write(Winner_Outlook)
