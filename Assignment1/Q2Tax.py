grossIncome = float(input("Enter gross income: "))
dependents = float(input("Enter number of dependents: "))
taxableIncome = grossIncome - 10000 - dependents * 3000
tax = taxableIncome * 0.2
print("Your tax is: ", tax)
