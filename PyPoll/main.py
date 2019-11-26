import os
import csv

csvpath = 'election_data.csv'
with open(csvpath, newline = '') as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=',')
    
    #ignore header
    next(csvreader)
    candidates = {}
    total = 0
    for row in csvreader:
        total = total + 1
        key = row[2]
        if key in candidates.keys():
            candidates[key] = candidates[key] + 1
        else:
            candidates.update({key : 1})
file = open("election_results.txt", "w")

print("Election Results")
print(f"Total Votes: {total}")
file.write(f"Total Votes: {total}\n")

winner = 0

for x in candidates:
    file.write(f"{x}: {round(candidates[x] / total * 100, 3)}%  ({candidates[x]})\n")
    print(f"{x}: {round(candidates[x] / total * 100, 3)}%  ({candidates[x]})")
    if candidates[x] > winner:
        winner = candidates[x]
        winner_name = x

print(f"Winner: {winner_name}")
file.write(f"Winner: {winner_name}")
