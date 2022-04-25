"""
Program: payroll.py
Project 4.12

Print a payroll report.

Input
   A file in which each line has the form
   
   <last name> <hourly wage> <hours worked>

Output
   A report in tabular format.  Each line has the form

   <last name> <hours worked> <total wages>
   
"""

# Take the inputs
fileName = input("Enter the file name: ")

# Open the input file
inputFile = open(fileName, 'r')

# Read the data and print the report
print("%-15s%-10s%-15s%7s%15s" % ("Name","EmpNum","Hours", "PayRate", "Total Pay"))
print("#" * 67)
for line in inputFile:
    dataList = line.split('\t')
    name = dataList[0]
    empNum = int(dataList[1])
    adress = dataList[2]
    hours = int(dataList[3])
    payRate = float(dataList[4])
    totalPay = hours * payRate
    print("%-16s%-9s%-20s%6s%8s%8.2f" % (name,adress,hours,payRate,"$",totalPay))
    
