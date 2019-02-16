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

#Checks to make sure the typed file exists (and includes false-input message)
if os.path.isfile(os.path.join(os.path.dirname(__file__), "data", chosen_file)) == False:
    print("--------------------------------------------")
    print("--------------------------------------------")
    print("Uh oh! It doesn't seem like the typed file exists.")
    print("Please make sure the file you typed is in the list")
    print("above and that it is in the format 'sales-YYYYMM.csv'")
    print("and make sure NOT to type the quotation marks.")
    print("--------------------------------------------")
    print("--------------------------------------------")
    sys.exit("Please re-run the program and try again!") #Got this from stack exchange

#Gets month and year values from file name
first_reduction = chosen_file[:12]
second_reduction = first_reduction[-6:]
year_value = int(second_reduction[:4])
month_value = int(second_reduction[-2:])
if month_value == 1:
    month_name = "January"
elif month_value == 2:
    month_name = "February"
elif month_value == 3:
    month_name = "March"
elif month_value == 4:
    month_name = "April"
elif month_value == 5:
    month_name = "May"
elif month_value == 6:
    month_name = "June"
elif month_value == 7:
    month_name = "July"
elif month_value == 8:
    month_name = "August"
elif month_value == 9:
    month_name = "September"
elif month_value == 10:
    month_name = "October"
elif month_value == 11:
    month_name = "November"
elif month_value == 12:
    month_name = "December"
#print(month_name)
#print(year_value)

#Reads the csv file and converts the data to a list of dictionaries
chosen_file_path = os.path.join(os.path.dirname(__file__), "data", chosen_file)
sales_list = []
with open(chosen_file_path, "r") as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        sales_list.append(dict(row))
        #print(row["product"], row["sales price"])
#print(type(sales_list))
#print(type(sales_list[0]))

#Creates list of products in file as list and what will become the list of sales sums for each product
product_list = []
summed_dictionary_list = []
for row in sales_list:
    test_var = row["product"] in product_list
    if test_var == False:
        product_list.append(row["product"])
        summed_dictionary_list.append({"Product":row["product"], "Monthly Sales":float(0)})
#print(product_list)
#print(summed_dictionary_list)

#Perform summation calculations
for row in sales_list:
    current_product = row["product"]
    for list_item in summed_dictionary_list:
        test_var2 = current_product == list_item["Product"]
        if test_var2 == True:
            list_item["Monthly Sales"] = list_item["Monthly Sales"] + float(row["sales price"])
#print(summed_dictionary_list)

#Creates sorted list (by sales) for top-selling products section and a list of product names in that order for chart
summed_dictionary_list.sort(key=operator.itemgetter("Monthly Sales"), reverse=True)
#for list_item in summed_dictionary_list:
    #product_list.append(list_item["Product"])

#Calculates total monthly sales as a variable
total_monthly_sales = 0
for list_item in summed_dictionary_list:
    total_monthly_sales = total_monthly_sales + list_item["Monthly Sales"]
#print(total_monthly_sales)

#Prints monthly sales by product and total monthly sales
print("--------------------------------------------")
print("--------------------------------------------")
print("Total Sales per Product for ", month_name, ",", year_value)
print("--------------------------------------------")
for list_item in summed_dictionary_list:
    print(list_item["Product"], ": ${0:,.2f}".format(list_item["Monthly Sales"]))
print("--------------------------------------------")
print("Total Monthly Sales: ${0:,.2f}".format(total_monthly_sales))
print("--------------------------------------------")
print("--------------------------------------------")
print("Top-Selling Products")
print("--------------------------------------------")
print("1. ", summed_dictionary_list[0]["Product"], ": ${0:,.2f}".format(summed_dictionary_list[0]["Monthly Sales"]))
print("2. ", summed_dictionary_list[1]["Product"], ": ${0:,.2f}".format(summed_dictionary_list[1]["Monthly Sales"]))
print("3. ", summed_dictionary_list[2]["Product"], ": ${0:,.2f}".format(summed_dictionary_list[2]["Monthly Sales"]))
print("--------------------------------------------")
print("--------------------------------------------")
print("Creating pie chart depicting product sales")
print("as a percent of total monthly sales...")
print("--------------------------------------------")

import matplotlib.pyplot as plt
import numpy as np

pie_data = summed_dictionary_list

sales_percents = []
pie_labels = []
for list_item in summed_dictionary_list:
    temp_percent = list_item["Monthly Sales"] / total_monthly_sales
    sales_percents.append(round(temp_percent, 2))
    pie_labels.append(list_item["Product"])

fig1, ax1 = plt.subplots()
ax1.pie(sales_percents, labels=pie_labels, autopct='%1.1f%%', shadow=True, startangle=90)
ax1.axis("equal")  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()

#print("-----------------------")
#print("MONTH: March 2018")

#print("-----------------------")
#print("CRUNCHING THE DATA...")

#print("-----------------------")
#print("TOTAL MONTHLY SALES: $12,000.71")

#print("-----------------------")
#print("TOP SELLING PRODUCTS:")
#print("  1) Button-Down Shirt: $6,960.35")
#print("  2) Super Soft Hoodie: $1,875.00")
#print("  3) etc.")

#print("-----------------------")
#print("VISUALIZING THE DATA...")