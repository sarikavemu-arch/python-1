
n = int(input("Enter number of products: "))

subtotal = 0

for i in range(n):
    print("Product", i + 1)
    price = float(input("Enter price: "))
    quantity = int(input("Enter quantity: "))

    amount = price * quantity
    subtotal = subtotal + amount

discount = 0

if subtotal >= 5000:
    discount = subtotal * 0.10
elif subtotal >= 2000:
    discount = subtotal * 0.05

if discount > 500:
    discount = 500

taxable_amount = subtotal - discount
tax = taxable_amount * 0.05
total = taxable_amount + tax

print("Subtotal: Rs.", round(subtotal, 2))
print("Discount: Rs.", round(discount, 2))
print("Tax: Rs.", round(tax, 2))
print("Final Bill: Rs.", round(total, 2))
