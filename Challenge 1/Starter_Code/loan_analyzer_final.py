# coding: utf-8
import csv
from pathlib import Path

#List of loan costs as provided in initial documention
loan_costs = [500, 600, 200, 1000, 450]

#Determining the number of loans, with result presented
number_of_loans = len(loan_costs)
print(f"There are {number_of_loans} in this portfolio.")

# Calculating the total size (in dollars) of the portfolio, and presenting results
portfolio_value = sum(loan_costs)
print(f"The value of this portfolio is ${portfolio_value}.00")

# Determining the average value of a loan in the portfolio and presenting results
average_value = portfolio_value / number_of_loans
print(f"The average loan value in this portfolio is ${average_value: .2f}.")


"""-------------------------------------------"""


# Given the following loan data, you will need to calculate the present value for the loan
loan = {
    "loan_price": 500,
    "remaining_months": 9,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

# Using the get function to extract relevant data for present value calculation.
future_value = loan.get("future_value")
remaining_months = loan.get("remaining_months")
print(f"The loan has a future value of ${future_value: .2f}, and has {remaining_months} months left on the term.")

# Calculation of the loan present value, including and presenting the result
discount_rate = .20
present_value = future_value / (1 + discount_rate/12) ** remaining_months
print(f"The loan is currently worth ${present_value: .2f}")

# Conditional statment that compares present value of loan to a pre-defined hurdle rate and presenting a recommendation.
loan_price = loan.get("loan_price")
if present_value >= loan_price:
    print(f"We should buy this loan.  It is worth ${present_value - loan_price: .2f} than the asking price.")
else:
    print(f"Walk away.  We will lose ${loan_price - present_value: .2f} on this deal.")


"""-------------------------------------------"""


#Data provided as part of hte assignment.  Note: we have been instructed to use 0.2 as the Annual Discount Rate
new_loan = {
    "loan_price": 800,
    "remaining_months": 12,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

#Function to calculate the present value of the loan referenced above
def loan_pv(future_value, remaining_months, annual_discount_rate):
  
    present_value =  future_value / (1 + annual_discount_rate / 12) ** remaining_months
    return(present_value)
    print(present_value)

# Using function defined above to calculate and present the present value of the loan
annual_discount_rate = 0.20
loan_present_value = loan_pv(new_loan["future_value"], new_loan["remaining_months"], annual_discount_rate)
print(f"The present value of the loan is: ${loan_present_value: .2f}")


"""-------------------------------------------"""


# Data provided as part of the assignment
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

# Empty list that will be populated with data from loans list
inexpensive_loans = []

#create loop to find loans that are $500 or smaller, and present the results
for loan in loans:
    if loan["loan_price"] <= 500:
        inexpensive_loans.append(loan)
print(inexpensive_loans)

# Defining column headers and path for CSV output
header = ["loan_price", "remaining_months", "repayment_interval", "future_value"]
output_path = Path("inexpensive_loans.csv")

# Export data from inexpensive loans to a csv file
with open(output_path, 'w') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=",") 
    csvwriter.writerow(header)
    for loan in inexpensive_loans:
        csvwriter.writerow(loan.values())

