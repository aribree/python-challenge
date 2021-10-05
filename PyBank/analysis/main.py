from ast import Str
import csv
import os

csvpath = os.path.join("..","resources", "budget+data.csv")

with open(csvpath, newline ='') as csvfile:
    csvreader = csv.reader("csvfile", delimeter = ',')

print("Financial Analysis")
print("-------------------------")

header = next(csvreader)

count = 0
total = 0
average = 0
current = 0
high_profit = 0
high_loss = 0
profit_loss_date = ""
loss_date = ""
for row in csvreader:
    total += int(row[1])
    count += 1
    current = int(row[1])
    if(current >= [0]): 
        if(current> high_loss):
            high_profit = current
            profit_date =str(row[0])
        elif(current < [0]):
            if(current < high_loss):
                high_loss = current
                loss_date = str(row[0])
    average = total / count 
    print (total)
file = "analysis.txt"
with open('analysis', 'w') as text:
    print(text)
    formatTxt =(f"Financial Analysis\n"
                f"---------------------\n"
                f"Total Months: {str(count)}\n"
                f"Total: $ {str(total)}\n"
                f"Gteateset Increase in Profits: {str(Profit_date)}"
                f"($ {str(high_profit)})\n "
                f"Greatest Decrease In Profits: {str(loss_date)}"
                f"(${Str(high_loss)})\n"
text.write(formatTxt)
