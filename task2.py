units = int(input("Enter electricity units: "))
previous = int(input("Enter previous month bill: "))

if units <= 100:
    bill = units * 2
elif units <= 200:
    bill = 200 + (units - 100) * 3
else:
    bill = 500 + (units - 200) * 5

bill = bill + 50

if units > 200:
    bill = bill + 100

if units <= 100:
    bill = bill - 20

print("Current Bill:", bill)

if bill > previous * 1.5:
    print("Unusual Increase")
else:
    print("Normal Bill")

