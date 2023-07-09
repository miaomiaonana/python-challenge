# -*- coding: UTF-8 -*-
"""PyRamen Homework Starter."""

# @TODO: Import libraries
import csv
from pathlib import Path

# @TODO: Set file paths for menu_data.csv and sales_data.csv
menu_filepath = Path('Resources/menu_data.csv')
sales_filepath = Path('Resources/sales_data.csv')

# @TODO: Initialize list objects to hold our menu and sales data
menu = []
sales = []

# @TODO: Read in the menu data into the menu list
with open(menu_filepath, 'r') as menufile:
    menureader = csv.reader(menufile,delimiter=",")
    header = next(menureader)
    for row in menureader:
        menu.append(row)


# @TODO: Read in the sales data into the sales list
with open(sales_filepath, 'r') as salesfile:
    salesreader = csv.reader(salesfile,delimiter=",")
    header = next(salesreader)
    for row in salesreader:
        sales.append(row)



# @TODO: Initialize dict object to hold our key-value pairs of items and metrics
report = {}

# Initialize a row counter variable
row_count = 0

# @TODO: Loop over every row in the sales list object
for row in sales:



    # Line_Item_ID,Date,Credit_Card_Number,Quantity,Menu_Item
    # @TODO: Initialize sales data variables
    quantity = float(row[3])
    sales_item = row[4]

    # @TODO:
    # If the item value not in the report, add it as a new entry with initialized metrics
    # Naming convention allows the keys to be ordered in logical fashion, count, revenue, cost, profit
    if sales_item not in report:
        report[sales_item] = {
            "01-count": 0,"02-revenue": 0,"03-cogs": 0,"04-profit": 0,
        }


    # @TODO: For every row in our sales data, loop over the menu records to determine a match
    for x in menu:

        # Item,Category,Description,Price,Cost
        # @TODO: Initialize menu data variables
        item = x[0]
        price = float(x[3])
        cost = float(x[4])
      
        # @TODO: Calculate profit of each item in the menu data
        profit = price - cost
        # @TODO: If the item value in our sales data is equal to the any of the items in the menu, then begin tracking metrics for that item
        if item == sales_item:

            # @TODO: Print out matching menu data
            # print(item)
        

            # @TODO: Cumulatively add up the metrics for each item key
            report[item]["01-count"] += quantity
            report[item]["02-revenue"] += price * quantity
            report[item]["03-cogs"] += cost * quantity
            report[item]["04-profit"] += profit * quantity
            break


        # @TODO: Else, the sales item does not equal any fo the item in the menu data, therefore no match
    else:
        print(f"{sales_item} does not equal {item}! NO MATCH")


    # @TODO: Increment the row counter by 1

    row_count += 1
# @TODO: Print total number of records in sales data
print(row_count)

print(report)

# @TODO: Write out report to a text file (won't appear on the command line output)
report = str(report)

file_path = Path ("output.txt")
with open(file_path, 'w') as file:
    file.write(report)
   