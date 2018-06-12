# Python Homework PyBank
#In this challenge, you are tasked with creating a Python script for analyzing the financial records 
# of your company. You will be given two sets of revenue data (`budget_data_1.csv` and `budget_data_2.csv`). Each dataset is composed of two columns: `Date` and `Revenue`. (Thankfully, your company has rather lax standards for accounting so the records are simple.)
#Your task is to create a Python script that analyzes the records to calculate each of the following:
#The total number of months included in the dataset
#The total amount of revenue gained over the entire period
#The average change in revenue between months over the entire period
#The greatest increase in revenue (date and amount) over the entire period
#The greatest decrease in revenue (date and amount) over the entire period

#Depencies
import os
import csv

#Prompt user for file lookup
budget_data_1 = input("budget_data_1.csv:")

# Set path for file
csvpath = os.path.join("C:\\Users\\Alain\\GWDC201805DATA3-Class-Repository-DATA\\Homework\\03-Python\\Instructions\\PyBank\\raw_data\\", "budget_data_1.csv")

# Create output file name
output_file = "budget_data_1_output.txt"

# Declare variables
month_count=0
total_revenue=0
largest_loss=0
loss_date="unknown"
gain_date="unknown"
largest_gain=0
avg_delta = 0
current_month_rev=0
prior_month_rev=0
delta=0

#Open the csv
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

# looping process to get the output
    for row in csvreader:
        prior_month_rev=current_month_rev 
        if prior_month_rev==0:
            exclude=int(row["Revenue"])
        total_revenue=total_revenue+ int(row["Revenue"])
        month_count = month_count + 1
        # calculates the change in current month revenue and keeps total     
        current_month_rev=int(row["Revenue"])
        delta=current_month_rev-prior_month_rev
        avg_delta=avg_delta+delta
        # flags the largest loss or largest gain
        if delta > largest_gain:
            largest_gain=delta
            gain_date=row["Date"]
        elif delta < largest_loss:
            largest_loss=delta
            loss_date=row["Date"]

#calculates the average change over the period
avg_delta=avg_delta-exclude
delta_percentage=avg_delta/(month_count-1)

#outputs the results and closes the output file
text_file =open(output_file, "budget_data_1_output")
print("  ")
text_file.write(" \n")
print("--------------------------------------------------------------------")
text_file.write("-------------------------------------------------------------------- \n")
print(" Financial Analysis")
text_file.write("  Financial Analysis \n")
print("--------------------------------------------------------------------")
text_file.write("-------------------------------------------------------------------- \n")
print("Total number of months included in the dataset: " + str(month_count))
text_file.write("Total number of months included in the dataset: " + str(month_count) + "\n")
print("The total amount of revenue gained over the entire period: $ " + str(total_revenue))
text_file.write("The total amount of revenue gained over the entire period: $ " + str(total_revenue) + "\n")
print("The average change in revenue between months over the entire period : $" + str(delta_percentage))
text_file.write("The average change in revenue between months over the entire period : $" + str(delta_percentage) + "\n")
print("The greatest increase in revenue (date and amount) over the entire period : " + str(gain_date) + "   $ " + str(largest_gain))
text_file.write("The greatest increase in revenue (date and amount) over the entire period : " + str(gain_date) + "   $ " + str(largest_gain) + "\n")
print("The greatest decrease in revenue (date and amount) over the entire period : " + str(loss_date) + "   $ " + str(largest_loss))
text_file.write("The greatest decrease in revenue (date and amount) over the entire period : " + str(loss_date) + "   $ " + str(largest_loss) + "\n")
print("--------------------------------------------------------------------")
text_file.write("-------------------------------------------------------------------- \n")
text_file.close()
