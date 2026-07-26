def calculate_change(paid,price):
    return paid-price

ticket_price=30

print("=== Parking Ticket Payment Helper ===")
print("Accepted coins: 1, 5, 10, 25")

total_inserted=0
coins_inserted=0

while True:
    coin=int(input("Insert a coin: "))

    if coin not in [1,5,10,25]:
        print("Invalid coin.")
        continue

    total_inserted+=coin
    coins_inserted+=1

    print("Total inserted:",total_inserted)

    if total_inserted>=ticket_price:
        break

change=calculate_change(total_inserted,ticket_price)

if change==0:
    pass
else:
    print("Change:",change)

print("Payment complete!")
print("Ticket price:",ticket_price)
print("Total inserted:",total_inserted)
print("Coins inserted:",coins_inserted)
print("Thank you!")