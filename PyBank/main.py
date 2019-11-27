import os
import csv

#set path of file
csvpath = 'budget_data.csv'

#open csv file
with open(csvpath, newline = '') as csvfile:
    
    #initialize i/o stream
    csvreader = csv.reader(csvfile, delimiter=',')
    
    #ignore header
    next(csvreader)
    
    total_months = 0
    
    #sum_profits holds the total profits over all months
    sum_profits = 0
    
    #greatest_increase and #greatest_decrease hold the greatest increase in profits and the greatest decrease in profits
    greatest_increase = 0
    greatest_decrease = 0
    
    #iterate over all rows
    for row in csvreader:
        
        #if this is the first record, we set the first_profit to this row's profit
        if total_months == 0:
            first_profit = int(row[1])
            current_profit = int(row[1])
            
        #if this is not the first month, we check to see if the change in profit for current row is greater than the greatest increase or less than the lowest decrease
        #also will set the greatest_increase_month and greatest_decrease_month to 
        else:
            #current_profit has not yet been updated. so we can get the previous_profit by setting it to current_profit
            previous_profit = current_profit
            #update current_profit
            current_profit = int(row[1])
            
            if current_profit - previous_profit < greatest_decrease:
                greatest_decrease = current_profit - previous_profit
                greatest_decrease_month = row[0]
            if current_profit - previous_profit > greatest_increase:
                greatest_increase = current_profit - previous_profit
                greatest_increase_month = row[0]
                
        #update total months
        total_months = total_months + 1
        
        #add the profits of the current row to the total profits
        sum_profits = sum_profits + current_profit

#print results
print(f"Total Months: {total_months}")
print(f"Total: ${sum_profits}")

#there are total_months profit entries, so only total_months - 1 changes in profits
average_change = round(( current_profit - first_profit ) / (total_months - 1), 2)
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {greatest_increase_month}  (${greatest_increase})" )
print(f"Greatest Decrease in Profits: {greatest_decrease_month}  (${greatest_decrease})" )

#create new file and add results
file = open("results.txt", "w")
file.write(f"Total Months: {total_months}\n")
file.write(f"Total: ${sum_profits}\n")
file.write(f"Average Change: ${average_change}\n")
file.write(f"Greatest Increase in Profits: {greatest_increase_month}  (${greatest_increase})\n")
file.write(f"Greatest Decrease in Profits: {greatest_decrease_month}  (${greatest_decrease})\n" )
file.close()
