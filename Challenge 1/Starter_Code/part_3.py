# coding: utf-8
import csv
from pathlib import Path


"""Part 3: Perform Financial Calculations.

Perform financial calculations using functions.

1. Define a new function that will be used to calculate present value.
    a. This function should include parameters for `future_value`, `remaining_months`, and the `annual_discount_rate`
    b. The function should return the `present_value` for the loan.
2. Use the function to calculate the present value of the new loan given below.
    a. Use an `annual_discount_rate` of 0.2 for this new loan calculation.
"""
def loan_pv(future_value, remaining_months, annual_discount_rate):
  
    present_value =  future_value / (1 + annual_discount_rate / 12) ** remaining_months
    return(present_value)
    print(present_value)

# Given the following loan data, you will need to calculate the present value for the loan

new_loan = {
    "loan_price": 800,
    "remaining_months": 12,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

# @TODO: Define a new function that will be used to calculate present value.
#    This function should include parameters for `future_value`, `remaining_months`, and the `annual_discount_rate`
#    The function should return the `present_value` for the loan.
# YOUR CODE HERE!
annual_discount_rate = 0.20
loan_present_value = loan_pv(new_loan["future_value"], new_loan["remaining_months"], annual_discount_rate)
print(loan_present_value)


# @TODO: Use the function to calculate the present value of the new loan given below.
#    Use an `annual_discount_rate` of 0.2 for this new loan calculation.
# YOUR CODE HERE!
print(f"The present value of the loan is: {loan_present_value}")