user_monthly_income = float(input("Enter your monthly income:"))
user_monthly_expenses= float(input("Enter your monthly expenses:"))

monthly_savings = user_monthly_income - user_monthly_expenses

annual_savings = monthly_savings * 12
interest = annual_savings * 0.05
projected_savings = annual_savings + interest

print(f"Your monthly saving is ${monthly_savings}")
print(f"projected savings after one year with interest is ${projected_savings}")