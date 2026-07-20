customers = 2
totals = []

customer = 1
while customer <= customers:
    print("Customer", customer)
    total = 0
    items = 2

    while items > 0:
        price = float(input("Enter item price: "))

        if price < 0:
            print("Invalid price!")
            continue

        total += price
        items -= 1

    totals.append(total)
    customer += 1

print("Final Report")

for i in range(len(totals)):
    print("Customer", i + 1)
    for j in range(1):
        if totals[i] >= 20:
            print("Total:", totals[i], "- Expensive")
        else:
            print("Total:", totals[i], "- Cheap")