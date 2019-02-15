# monthly_sales.py

# TODO: import some modules and/or packages here
import os

# TODO: write some Python code here to produce the desired functionality...

#Introduces the program
print("--------------------------------------------")
print("--------------------------------------------")
print("Welcome to the Executive Dashboard Program!")
print("This program will allow you to quickly summarize")
print("the sales details of the month of your choosing.")
print("Below is a list of .csv files which correspond")
print("to months for which we have data.")
print("--------------------------------------------")
print("--------------------------------------------")

#Prints the list of available csv files in the "data" sub-directory of the current repository
current_directory = os.getcwd()
csv_file_list = os.listdir(current_directory + "/data")
print(csv_file_list)

#Asks which month the user wants to explore
print("--------------------------------------------")
print("--------------------------------------------")
print("Please type in the name of the file for the ")
print("month you want to explore:")

print("-----------------------")
print("MONTH: March 2018")

print("-----------------------")
print("CRUNCHING THE DATA...")

print("-----------------------")
print("TOTAL MONTHLY SALES: $12,000.71")

print("-----------------------")
print("TOP SELLING PRODUCTS:")
print("  1) Button-Down Shirt: $6,960.35")
print("  2) Super Soft Hoodie: $1,875.00")
print("  3) etc.")

print("-----------------------")
print("VISUALIZING THE DATA...")