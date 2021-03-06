# coding: utf-8
import csv
from pathlib import Path

"""Part 4: Conditionally filter lists of loans.

In this section, you will use a loop to iterate through a series of loans and select only the inexpensive loans.

1. Create a new, empty list called `inexpensive_loans`.
2. Use a for loop to select each loan from a list of loans.
    a. Inside the for loop, write an if-statement to determine if the loan_price is less than or equal to 500
    b. If the loan_price is less than or equal to 500 then append that loan to the `inexpensive_loans` list.
3. Print the list of inexpensive_loans.
"""

loans = [
    {
        "loan_price": 700,
        "remaining_months": 9,
        "repayment_interval": "monthly",
        "future_value": 1000,
    },
    {
        "loan_price": 500,
        "remaining_months": 13,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 200,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 900,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
]

# @TODO: Create an empty list called `inexpensive_loans`
# YOUR CODE HERE!
inexpensive_loans = []

# @TODO: Loop through all the loans and append any that cost $500 or less to the `inexpensive_loans` list
# YOUR CODE HERE!
for loan in loans:
    if loan["loan_price"] <= 500:
        inexpensive_loans.append(loan)

#how to i call the full dictionary entry into inexpensive loans

# @TODO: Print the `inexpensive_loans` list
# YOUR CODE HERE
print(inexpensive_loans)

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

with open(output_path, 'w') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=",") 
    csvwriter.writerow(header)
    for loan in inexpensive_loans:
        csvwriter.writerow(loan.values())

# @TODO: Use the csv library and `csv.writer` to write the header row
# and each row of `loan.values()` from the `inexpensive_loans` list.
# YOUR CODE HERE!
