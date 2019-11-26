import os
import csv

csvpath = 'budget_data.csv'
with open(csvpath, newline = '') as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=',')
    
    #ignore header
    next(csvreader)
    
    total_months = 0
    sum_profits = 0
    greatest_increase = 0
    greatest_decrease = 0
    for row in csvreader:
        if total_months == 0:
            first_profit = int(row[1])
            current_profit = int(row[1])
        else:
            previous_profit = current_profit
            current_profit = int(row[1])
            if current_profit - previous_profit < greatest_decrease:
                greatest_decrease = current_profit - previous_profit
                greatest_decrease_month = row[0]
            if current_profit - previous_profit > greatest_increase:
                greatest_increase = current_profit - previous_profit
                greatest_increase_month = row[0]
        total_months = total_months + 1
        sum_profits = sum_profits + current_profit

print(f"Total Months: {total_months}")
print(f"Total: ${sum_profits}")
#there are total_months profit entries, so only total_months - 1 changes in profits
average_change = round(( current_profit - first_profit ) / (total_months - 1), 2)
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {greatest_increase_month}  (${greatest_increase})" )
print(f"Greatest Decrease in Profits: {greatest_decrease_month}  (${greatest_decrease})" )

file = open("results.txt", "w")
file.write(f"Total Months: {total_months}\n")
file.write(f"Total: ${sum_profits}\n")
file.write(f"Average Change: ${average_change}\n")
file.write(f"Greatest Increase in Profits: {greatest_increase_month}  (${greatest_increase})\n")
file.write(f"Greatest Decrease in Profits: {greatest_decrease_month}  (${greatest_decrease})\n" )
file.close()
