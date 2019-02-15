# monthly_sales.py

# TODO: import some modules and/or packages here
import os
import sys
import csv
import operator

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
##current_directory = os.getcwd()
##csv_file_list = os.listdir(current_directory + "/data")
csv_file_list = os.listdir(os.path.join(os.path.dirname(__file__), "data"))
print(csv_file_list)

#Asks which month the user wants to explore
print("--------------------------------------------")
print("--------------------------------------------")
print("Please type in the name of the file for the ")
chosen_file = input("month you want to explore: ")

#Checks to make sure the typed file exists
if os.path.isfile(os.path.join(os.path.dirname(__file__), "data", chosen_file)) == False:
    print("--------------------------------------------")
    print("--------------------------------------------")
    print("Uh oh! It doesn't seem like the typed file exists.")
    print("Please make sure the file you typed is in the list")
    print("above and that it is in the format 'sales-YYYYMM.csv'")
    print("and make sure NOT to type the quotation marks.")
    print("--------------------------------------------")
    print("--------------------------------------------")
    sys.exit("Please re-run the program and try again!")

#Reads the csv file and converts the data to a list of dictionaries
chosen_file_path = os.path.join(os.path.dirname(__file__), "data", chosen_file)
sales_list = []
with open(chosen_file_path, "r") as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        sales_list.append(dict(row))
        #print(row["product"], row["sales price"])
print(type(sales_list))
print(type(sales_list[0]))

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