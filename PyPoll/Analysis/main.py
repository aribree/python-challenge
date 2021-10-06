#Dependancies
import os
import csv
   
#Set File path for data
csvpath = os.path.join("PyBank/Resources/election_data.csv")
       
#Use csv module to read data
with open(csvpath, newline ='') as csvfile:
        
    #Specify delimiter and variables for data
    csvreader = csv.reader(csvfile, delimiter = ',')
       
#Set Variables
total_votes = 0
candidate_options = []
candidate_votes = {}
winning_candidate = ""
winning_count = 0

# Put the data into lists
with open(csvpath) as election_data:
    reader = csv.Dictreader(election_data)

#Skip header row
header = next(reader)
for row in reader:
    print(". ", end=""),
            
#Add votes to counter
total_votes = total_votes + 1
                
#Extract candidate names
candidate_name = row["Candidate"]
                    
#If candidate isnt in the list
if candidate_name not in candidate_options:
    candidate_options.append(candidate_name) #Amend the list to add candidate
        
#Add votes to counter
candidate_votes[candidate_name] = 0
       
#Add votes to candidates counter
candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1
    
#Usde csv module to write data
with open( "PyPoll/Analysis/analysis", 'w') as textfile:
    
# Print the final vote count
    election_results = (
    f"\n\nElection Results\n"
    f"-------------------------\n"
    f"Total Votes: {total_votes}\n"
    f"-------------------------\n")
    print(election_results)
#Update text file
'txt_file'.write(election_results)
       
# Loop through votes to find winner
for candidate in candidate_votes:
    votes = candidate_votes.get(candidate)
    vote_percentage = float(votes) / float(total_votes) * 100
               
#Find Winner
if (votes > winning_count):
    winning_count = votes
    winning_candidate = candidate
            
#Print counter for each voter
voter_output = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"
print(voter_output, end="")
   
#Update text file
'txt_file'.write(election_results)
        
#Print the winning candidate (to terminal)
winning_candidate = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"-------------------------\n")
        
print(winning_candidate)
