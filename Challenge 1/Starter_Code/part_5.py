# coding: utf-8
import csv
from pathlib import Path

#"""Part 5: Save the results.

#Output this list of inexpensive loans to a csv file
#    1. Use `with open` to open a new CSV file.
#        a. Create a `csvwriter` using the `csv` library.
#        b. Use the new csvwriter to write the header variable as the first row.
#        c. Use a for loop to iterate through each loan in `inexpensive_loans`.
#            i. Use the csvwriter to write the `loan.values()` to a row in the CSV file.

#    Hint: Refer to the official documentation for the csv library.
#    https://docs.python.org/3/library/csv.html#writer-objects"""


# Set the output header
header = ["loan_price", "remaining_months", "repayment_interval", "future_value"]

# Set the output file path
output_path = Path("inexpensive_loans.csv")

# @TODO: Use the csv library and `csv.writer` to write the header row
# and each row of `loan.values()` from the `inexpensive_loans` list.
# YOUR CODE HERE!