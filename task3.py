
consultation = int(input("Enter consultation charge: "))
diagnostic = int(input("Enter diagnostic charge: "))
treatment = int(input("Enter treatment charge: "))

total = consultation + diagnostic + treatment

if total >= 5000:
    discount = total * 10 / 100
else:
    discount = 0

bill = total - discount

print("Total Charges:", total)
print("Discount:", discount)
print("Final Bill:", bill)

if bill >= 5000:
    print("High Payment")
else:
    print("Normal Payment")
