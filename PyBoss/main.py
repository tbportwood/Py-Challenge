import os
import csv

#set path of file
csvpath = 'employee_data.csv'
#set path for updated file
output_path = "updated_employee_data.csv"

#us state abbreviations dictionary
us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

#open file
with open(csvpath, newline = '') as csvfile:
    
    #create reader stream
    csvreader = csv.reader(csvfile, delimiter = ',')
    
    #ignore header
    next(csvreader)
    
    #output list
    employees = []
    
    #iterate through all rows in reader stream, manipulate data, and store in employees list
    for row in csvreader:
            emp_id = row[0]
            
            #split names, birthdates, ssn so we can manipulate position of substrings or remove unwanted characters, like /
            full_name = row[1].split(" ")
            birthdate_l = row[2].split("-")
            updated_db = str(birthdate_l[1]) + "/" + str(birthdate_l[2]) + "/" + str(birthdate_l[0])
            ssn_l = row[3].split("-")
            updated_ssn = "***-**-" + str(ssn_l[2])
            first_name = full_name[0]
            last_name = full_name[1]
            state = row[4]
            
            #abbreviated state comes from dictionary
            updated_state = us_state_abbrev[state]
            
            #use temporary list to store update values and append this list to employees list
            temp = [emp_id, first_name, last_name, updated_db, updated_ssn, updated_state]
            employees.append(temp)
    
#write csv file
with open(output_path, mode = "w", newline = '') as csvfilex:
    csvwriter = csv.writer(csvfilex, delimiter = ',')
    csvwriter.writerow(["Employee ID", "First Name", "Last Name", "Date of Birth", "SSN", "State"])
    for row in employees:
        csvwriter.writerow(row)
                           
        