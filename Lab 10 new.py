'''
script: lab 10
action: opens a csv of employees and create a new csv with password for each employee
author: Sandra
date  : 04/23/2026
'''


import csv
import random
import string


def gen_pass(length):
        '''generate random password f a given length'''
        all = string.ascii_letters + string.digits + "!@#$%^&*()-_+=~[]{};<>?/\\|"
        password = "".join(random.sample(all,length))
        return password
    
def main():
    
 # Length of the generated password
    PASS_LENGTH = 16
   
    #opening and reading employee.csv file 
    employees = open("employees.csv")
    employeeData = csv.DictReader(employees)
    print("Done reading employees.csv")

    #writing to new file 
    employeeFileName = "employees_with_password.csv"
    employeeFile = open(employeeFileName, "w",newline="")
    employeeWriter = csv.DictWriter(employeeFile,["fname", "lname", "email","password"])
    #writing header to file 
    employeeWriter.writeheader()
    
    #looping through rows and generating passwords
    for index, row in enumerate(employeeData):
        if index == 0:
            header = list(row.keys()) # had to read keys beacuse fname appeared as \ufeffname
        password = gen_pass(PASS_LENGTH)
        #writing new row with password to file 
        employeeWriter.writerow({"fname": row[header[0]], "lname": row[header[1]], "email": row[header[3]], "password": password})

    print(f"wrote to file, {employeeFileName}")
    #closing read and write files 
    employeeFile.close()
    employees.close()

main()
# Employee Password Generator

#A Python script that reads a CSV file of employees and generates a secure,
#random 16-character password for each one, writing the results to a new CSV file.

## What it does

#- Reads employee data (first name, last name, email) from employees.csv
#- Generates a unique 16-character password for each employee using letters,
 # numbers, and special characters
'''
- Writes the original employee data plus the generated passwords to a new file
  called employees_with_password.csv

## Why I built it

This was built as part of a Python programming lab to automate a task that
IT teams handle manually — assigning initial passwords to new employee accounts.
Automating it reduces human error and saves time during onboarding.

## How to run it

1. Make sure employees.csv is in the same folder as the script
2. Run: python lab10.py
3. A new file called employees_with_password.csv will be created

## Requirements

Python 3.x — no external libraries needed, only built-in modules (csv, random, string)
'''
