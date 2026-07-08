cost=float(input("enter the actual cost"))
sold_cost=float(input("enter the sold cost"))
if sold_cost>cost:
    profit=sold_cost-cost
    print("total profit={0}".format(profit))
else:
    print("no profit")