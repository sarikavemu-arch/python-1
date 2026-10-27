
distance = int(input("Enter distance in km: "))
age = int(input("Enter passenger age: "))
travel_class = input("Enter class (Sleeper/AC): ")

if distance <= 100:
    fare = distance * 1
elif distance <= 500:
    fare = distance * 1.5
else:
    fare = distance * 2

if travel_class == "AC":
    fare = fare * 2

if age >= 60:
    fare = fare * 0.9

reservation_fee = 30
total = fare + reservation_fee

print("Base Fare: Rs.", round(fare, 2))
print("Reservation Fee: Rs.", reservation_fee)
print("Total Fare: Rs.", round(total, 2))

cancel = input("Cancel ticket? (yes/no): ")

if cancel == "yes":
    penalty = total * 0.2
    print("Cancellation Penalty: Rs.", round(penalty, 2))
    print("Refund: Rs.", round(total - penalty, 2))
