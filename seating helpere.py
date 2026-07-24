def total_bill(bill_amount, tip_perc):
    total = bill_amount + (bill_amount * tip_perc / 100)
    print("Total bill: $", total)
total_bill(150, 20)
def seating_arrangements(guests):
    """Calculates the number of seating arrangements for guests."""
    if guests == 0 or guests == 1:
        return 1
    return guests * seating_arrangements(guests - 1)
print(seating_arrangements.__doc__)
print("1 guest:", seating_arrangements(1))
print("2 guests:", seating_arrangements(2))
print("3 guests:", seating_arrangements(3))
print("5 guests:", seating_arrangements(5))