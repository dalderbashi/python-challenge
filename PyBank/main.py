# Your task is to create a Python script that analyzes the records to calculate each of the following:


# The total number of months included in the dataset
# The net total amount of "Profit/Losses" over the entire period
# The average of the changes in "Profit/Losses" over the entire period
# The greatest increase in profits (date and amount) over the entire period
# The greatest decrease in losses (date and amount) over the entire period


# As an example, your analysis should look similar to the one below:


#   Financial Analysis
#   ----------------------------
#   Total Months: 86
#   Total: $38382578
#   Average  Change: $-2315.12
#   Greatest Increase in Profits: Feb-2012 ($1926159)
#   Greatest Decrease in Profits: Sep-2013 ($-2196167)



import os
import csv


csvpath = os.path.join('budget_data.csv')

with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

   # print(csvreader)

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    #print(f"CSV Header:{csv_header}")
   
    # set variables
    row_count = 0
    profit_total = 0
    total_change = 0
    prior_month_profit = None
    greatest_increase = ("",0)
    greatest_decrease = ("",0) 

    # Read each row of data after the header
    # The net total amount of "Profit/Losses" over the entire period
    for row in csvreader:
        current_month_profit = int(row[1])
        row_count += 1 
        profit_total += current_month_profit

        #The average of the changes in "Profit/Losses" over the entire period
        #subtract current month profit/loss value from previous month 
        #apply average function or answer / row_count - 1 
        if prior_month_profit == None:
            prior_month_profit = current_month_profit
        else:
            profit_change = current_month_profit - prior_month_profit 
            total_change += profit_change
            prior_month_profit = current_month_profit

             
# The greatest increase in profits (date and amount) over the entire period
            if greatest_increase[0] == "" or greatest_increase[1] < profit_change:
                greatest_increase = (row[0], profit_change)
# The greatest decrease in losses (date and amount) over the entire period
            if greatest_decrease[0] == "" or greatest_decrease[1] > profit_change:
                greatest_decrease = (row[0], profit_change)

 #create a list for the output to make it easier    
    financial_analysis = [
        "Financial Analysis",
        "----------------------------",
        f"Total Months: {row_count}",    
        f"Total: ${profit_total}",
        f"Average Change: ${round(total_change/(row_count-1),2)}",
        f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})",
        f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})"
        ]
#print verything in financia_analysis and separate each item in a this list by a new line
print(*financial_analysis, sep = "\n")

#write into text file
with  open("PyBank.txt","w") as textfile:
    print(*financial_analysis, sep = "\n", file = textfile)
    