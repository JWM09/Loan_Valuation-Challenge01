loan_costs = [500, 600, 200, 1000, 450]

number_of_loans = len(loan_costs)
print(f"There are {number_of_loans} loans in this portfolio.")

portfolio_value = sum(loan_costs)
print(f"The value of this portfolio is ${portfolio_value: .2f}")

average_value = portfolio_value / number_of_loans
print(f"The average loan value in this portfolio is ${average_value: .2f}.")