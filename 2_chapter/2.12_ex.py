initial_amount = 100
p = 5.5 # interest 2025-08-20 07:02
amount = initial_amount
years = 0
while amount <= 1.5*initial_amount:
    amount = amount + p/100*amount
    years = years + 1
print(years)
