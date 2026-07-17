holiday = input("Beach or Mountain? ")

if holiday == "Beach":
    swim = input("Swim? (yes/no) ")
    if swim == "yes":
        print("Go swimming!")
    else:
        print("Relax on the beach!")
else:
    hike = input("Hike? (yes/no) ")
    if hike == "yes":
        print("Go hiking!")
    else:
        print("Relax in a cabin!")