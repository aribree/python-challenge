import csv
import os
        
        
#Set file path for data
csvpath = os.path.join("Resources/budget_data.csv")
with open(csvpath, newline ='') as csvfile:
                    
        #Specify delimiter and variables for data
        csvreader = csv.Dictreader(csvfile, delimiter = ',')
    
#Variable lists to be added to:
number_months = 0
month_total = []
profit = []
profit_difference = []
    
#Read header rows
header = next(csvreader)
first_row = next(csvreader)
profit = int(first_row[1])
    
#Count Months
for number_of_month in range:
   
    #Loop through lists adding value
    for row in csvreader:
        month_total.append(row[0])
    profit.append(int(row[1]))
for i in range:(len(profit)-1)
profit_difference.append(profit[i+1]-profit[1])
                                    
#Calcuate the average monthly change
net_month_average = round(sum(profit_difference)/len(profit_difference))
                                   
#Calculate Min Values
decrease = min(profit_difference)
decrease = profit_difference.index(min(profit_difference))+1
                                    
#Calculate Max Values
increase = max(profit_difference)
increase = profit_difference.index(max(profit_difference))+1
                    
#Print Headers
Output = (
    f"\nFinancial Analysis\n"
    f"Total Months:[len(number_months)]\n"
    f"Total: $(sum(profit)\n"
    f"Average Change: ${net_month_average: .2f}\n"
    f"Greatest Decrease in Profits: {month_total[decrease]} (${(str(decrease))}\n"
    f"Greatest Increase in Profits: {month_total[increase]} (${(str(increase))}")

#Print to Terminal
print(Output)
                   
#Export file path in "write" mode ('w')
analysis = open('analysis.txt')
with open(analysis, 'w') as txt_file:
    csvwriter = csv.Dictwriter(analysis)
    txt_file.write(Output)

analysis.close ()


