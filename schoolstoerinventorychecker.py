items=['pencils','math book','erasers','waterbottle']
stock=[100,50,100,0]
inventory={item:count for item, count in zip(items,stock)}
print(inventory)
in_stock_inventory=[item for item in items if inventory[item]>0]
print(in_stock_inventory)
chosen_item=input('what item do you want to buy')
if chosen_item not in inventory or inventory[chosen_item]==0:
    print('there is no',chosen_item)
    exit()
prices=[1,15,1,25]
markup=int(input('enter the markup amount '))
markup_prices=list(map(lambda p:p+markup,prices))
print(markup_prices)