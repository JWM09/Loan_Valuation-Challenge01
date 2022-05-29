loan_costs = [500, 600, 200, 1000, 450]

number_of_loans = len(loan_costs)
print(f"There are {number_of_loans} loans in this portfolio.")

portfolio_value = sum(loan_costs)
print(f"The value of this portfolio is ${portfolio_value: .2f}")

average_value = portfolio_value / number_of_loans
print(f"The average loan value in this portfolio is ${average_value: .2f}.")

loan = {
    "loan_price": 500,
    "remaining_months": 9,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

future_value = loan.get("future_value")
remaining_months = loan.get("remaining_months")
print(f"The loan has a future value of ${future_value: .2f}, and has {remaining_months} months left on the term.")

discount_rate = .20
present_value = future_value / (1 + discount_rate/12) ** remaining_months
print(f"The loan is currently worth ${present_value: .2f}")

loan_price = loan.get("loan_price")
if present_value >= loan_price:
    print(f"We should buy this loan.  It is worth ${present_value - loan_price: .2f} than the asking price.")
else:
    print(f"Walk away.  We will lose ${loan_price - present_value: .2f} on this deal.")