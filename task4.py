
basic = int(input("Enter basic salary: "))
allowance = int(input("Enter allowance: "))
overtime = int(input("Enter overtime amount: "))

gross = basic + allowance + overtime

if gross <= 20000:
    deduction = gross * 5 / 100
elif gross <= 40000:
    deduction = gross * 10 / 100
else:
    deduction = gross * 15 / 100

net = gross - deduction

print("Gross Salary:", gross)
print("Deduction:", deduction)
print("Net Salary:", net)
