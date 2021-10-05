#Discrepancies
import os
import csv

#Open Data Source File
csvpath = os.path.jpin("PyPoll", "Resources", "election_data.csv")
with open(csvpath, newline ="") as csvfile:
    csvreader = csv.reader(csvfile, delimeter= ',')
#Headers
print("Election Results")
print("---------------------")

header = next(csvreader)

#Input Variables
khan_count = 0
khan_percent = 0.00
correy_count = 0
correy_percent = 0.00
li_count = 0
li_percent = 0.00
otooley_count = 0
otooley_percent = 0.00
winner_count = 0
total_count =0
winner = ""

#Loop through data to get votes
for row in csvreader:

    total_count = total_count + 1
if(row[2] == "Khan): "
    khan_count = khan_count + 1
elif (row[2] == "Correy"):
    correy_count = correy_count + 1
elif (row[2] == . "Li"):
    licount = li_count + 1
elif (row[2] == "O'Tooley"):
    otooley_count = otooley_count + 1

#Total Percentages
khan_percent = (khan_count / total_count) * 100
correy_percent = correy_count /total_count * 100
li_percent = li_count / total_count * 100
otooley_percent = otooley_count / total_count * 100

#Print Winner
winner_count = max(khan_count, correy_count, li_count, otooley_count)
if(winner_count == khan_count): 
winner = "Khan"
elif(winner_count == correy_count):
winner = "Correy"
elif(winner_count == li_count):
winner = "Li"
elif(winner_count == otooley_count):
winner ="O'Tooley"
print(total_count)

# Output File
file = "vote_analysis.txt"
with open(file, 'w') as text:
print(text)
formatTxt = (
    f"Election Results\n"
    f"-----------------------\n"
    f"Total votes: {str(total_count)}\n"
    f"-----------------------"
    f"Khan: {str(khan_percent)} % "
    f"({str(khan_percent)})\n"
    f"Correy: {str(correy_percent)} % "
    f"({str(correy_percent)})\n"
    f"Li: {str(li_percent)} % "
    f"({str(li_count)})\n"
        f"O'Tooley: {str(otooley_percent)} % "
        f"({str(otooley_percent)})\n"
        f"------------------------\n"
        f"Winner: {str(winner)}"
        f"\n------------------------\n")

text.write:(formatTxt)
