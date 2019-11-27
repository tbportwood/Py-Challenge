import os
import csv

#set file path
csvpath = 'election_data.csv'

#open file
with open(csvpath, newline = '') as csvfile:
    
    #start i/o stream
    csvreader = csv.reader(csvfile, delimiter=',')
    
    #ignore header
    next(csvreader)
    
    #initialize candidates dictionary
    candidates = {}
    
    #initialize total votes variable
    total = 0
    
    for row in csvreader:
        #add 1 to vote total for each row
        total = total + 1
        
        #set a variable, key, to the 3rd index of the row (name)
        key = row[2]
        
        #check to see if the name is in the dictionary
        if key in candidates.keys():
            #if the name is in the dictionary, add 1 to their vote total
            candidates[key] = candidates[key] + 1
        else:
            #if the name is not in the dictionary, create a key in the dictionary
            candidates.update({key : 1})
            
#create new file
file = open("election_results.txt", "w")

#print output and write to the file
print("Election Results")
print(f"Total Votes: {total}")
file.write("Election Results \n")
file.write(f"Total Votes: {total}\n")

#winning vote total, need this variable to keep track of who has the max number of votes
winner = 0

#write results to file
for x in candidates:
    file.write(f"{x}: {round(candidates[x] / total * 100, 3)}%  ({candidates[x]})\n")
    print(f"{x}: {round(candidates[x] / total * 100, 3)}%  ({candidates[x]})")
    
    #also check to see if the candidate has greatest number of votes, if so change the winner name and winner vote total
    if candidates[x] > winner:
        winner = candidates[x]
        winner_name = x

#print winner / write to file
print(f"Winner: {winner_name}")
file.write(f"Winner: {winner_name}")
