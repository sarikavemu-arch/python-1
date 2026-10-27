
days = int(input("Enter required validity days: "))
budget = int(input("Enter your budget: "))

plans = [
    ["Plan A", 199, 2, 28],
    ["Plan B", 299, 3, 56],
    ["Plan C", 399, 5, 84]
]

best_cost = 99999
best_plan = "No eligible plan"

for plan in plans:
    name = plan[0]
    price = plan[1]
    data = plan[2]
    validity = plan[3]

    if validity >= days and price <= budget:
        if price < best_cost:
            best_cost = price
            best_plan = name

print("Best Plan:", best_plan)

if best_plan != "No eligible plan":
    print("Plan Cost: Rs.", best_cost)
else:
    print("No plan satisfies the conditions.")
