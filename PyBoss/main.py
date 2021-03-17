""" PyBoss.py """
#-*- coding: UTF-8 -*-
import os
import json
import csv
import string
import re
import us_state_abbrev

#Need the state key - need to preprocess the state.py

filepath = os.path.join("employee_data.csv")
abbreviations = {}
employee_data = []
#Read data into a dictionary
with open(filepath) as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        emp_id = row["Emp ID"]
        name = row["Name"]
        dob = row["DOB"]
        SocialSecurity = row["SSN"]
        ssn = re.sub("\d","*",SocialSecurity,5)
        #print(ssn)
        state = row["State"] 
        MyState=us_state_abbrev.us_state_abbrev[state]

        employee_data.append(
            {
                "emp_id":row["Emp ID"],
                "name":row["Name"],
                "dob":row["DOB"],
                "ssn": ssn,
                "state":MyState
                
            }
        )

_, filename = os.path.split(filepath)



csvpath = os.path.join("output", filename)
with open(csvpath, 'w') as csvfile:
    fieldnames = ["emp_id","name","dob","ssn","state"]
    writer = csv.DictWriter(csvfile,fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(employee_data)