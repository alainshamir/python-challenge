# Python Homework PyBank
#In this challenge, you are tasked with creating a Python script for analyzing the financial records 
# of your company. You will be given two sets of revenue data (`budget_data_1.csv` and `budget_data_2.csv`). Each dataset is composed of two columns: `Date` and `Revenue`. (Thankfully, your company has rather lax standards for accounting so the records are simple.)
#Your task is to create a Python script that analyzes the records to calculate each of the following:
#The total number of months included in the dataset
#The total amount of revenue gained over the entire period
#The average change in revenue between months over the entire period
#The greatest increase in revenue (date and amount) over the entire period
#The greatest decrease in revenue (date and amount) over the entire period

#Modules
import os
import csv

# Set path for file
csvpath = os.path.join("C:\\Users\\Alain\\GWDC201805DATA3-Class-Repository-DATA\\Homework\\03-Python\\Instructions\\PyBank\\raw_data\\", "budget_data_1.csv")

# Create output file name
output_file = "C:/Users/Alain/GWDC201805DATA3-Class-Repository-DATA/Unit_3_Assignment/python-challenge/PyBank/budget_data_1_output.txt"  

# Track parameters
total_months = 0
prev_average = 0
month_of_change = []
average_change_list = []
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999999999]
total_revenue = 0
# Read the csv 
with open(csvpath) as financial_data:
    reader = csv.DictReader(financial_data)
#  Each row is read as a row
    for row in reader:
        print(row)
# track the total
        total_months = total_months + 1
        total_revenue= total_revenue + int(row["Revenue"])
 # track the average change
        average_change = int(row["Revenue"]) - prev_average
        prev_average= int(row["Revenue"])
        average_change_list = average_change_list + [average_change]
        month_of_change = month_of_change + [row["Date"]]
# Calculate the greatest increase
        if (average_change > greatest_increase[1]):
            greatest_increase[0] = row["Date"]
            greatest_increase[1] = average_change

        # Calculate the greatest decrease
        if (average_change < greatest_decrease[1]):
            greatest_decrease[0] = row["Date"]
            greatest_decrease[1] = average_change

# Calculate the Average Revenue Change
revenue_avg = sum(average_change_list) / len(average_change_list)

# Generate Output Summary
output = (
    f"\nFinancial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total Revenue: ${total_revenue}\n"
    f"Average Revenue Change: ${average_change}\n"
    f"Greatest Increase in Revenue: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Revenue: {greatest_decrease[0]} (${greatest_decrease[1]})\n")

# Print the output (to terminal)
print(output)

# Export the results to text file
with open(output_file, "w") as txt_file:
    txt_file.write(output)

#Modules
import os
import csv

# Set path for file
csvpath_2 = os.path.join("C:\\Users\\Alain\\GWDC201805DATA3-Class-Repository-DATA\\Homework\\03-Python\\Instructions\\PyBank\\raw_data\\", "budget_data_2.csv")

# Create output file name
output_file_2 = "C:/Users/Alain/GWDC201805DATA3-Class-Repository-DATA/Unit_3_Assignment/python-challenge/PyBank/budget_data_2_output.txt"  

# Track parameters
total_months = 0
prev_average = 0
month_of_change = []
average_change_list = []
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999999999]
total_revenue = 0
# Read the csv 
with open(csvpath_2) as financial_data:
    reader = csv.DictReader(financial_data)
#  Each row is read as a row
    for row in reader:
        print(row)
# track the total
        total_months = total_months + 1
        total_revenue= total_revenue + int(row["Revenue"])
 # track the average change
        average_change = int(row["Revenue"]) - prev_average
        prev_average= int(row["Revenue"])
        average_change_list = average_change_list + [average_change]
        month_of_change = month_of_change + [row["Date"]]
# Calculate the greatest increase
        if (average_change > greatest_increase[1]):
            greatest_increase[0] = row["Date"]
            greatest_increase[1] = average_change

        # Calculate the greatest decrease
        if (average_change < greatest_decrease[1]):
            greatest_decrease[0] = row["Date"]
            greatest_decrease[1] = average_change

# Calculate the Average Revenue Change
revenue_avg = sum(average_change_list) / len(average_change_list)

# Generate Output Summary
output_2 = (
    f"\nFinancial Analysis_2\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total Revenue: ${total_revenue}\n"
    f"Average Revenue Change: ${average_change}\n"
    f"Greatest Increase in Revenue: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Revenue: {greatest_decrease[0]} (${greatest_decrease[1]})\n")

# Print the output (to terminal)
print(output_2)

# Export the results to text file
with open(output_file_2, "w") as txt_file:
    txt_file.write(output_2)

