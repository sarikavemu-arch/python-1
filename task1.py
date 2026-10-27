
marks = int(input("Enter aggregate marks: "))
subject = int(input("Enter minimum subject marks: "))
attendance = int(input("Enter attendance percentage: "))
income = int(input("Enter family income: "))

if marks >= 75 and subject >= 40 and attendance >= 75 and income <= 200000:
    print("Scholarship Eligible")
else:
    print("Scholarship Not Eligible")
