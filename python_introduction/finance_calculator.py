user_monthly_income = float(input("Enter your monthly income:"))
user_monthly_expenses= float(input("Enter your monthly expenses:"))

monthly_savings = user_monthly_income - user_monthly_expenses
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

print(f"Your monthly saving is ${monthly_savings}")
print(f"projected savings after one year with interest is ${projected_savings}")