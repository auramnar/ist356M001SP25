items ={}

while True:
    item = input("Enter an item: ")
    if item == 'quit':
        break
    qty = int(input("Enter quantity: "))
    if item in items.keys():
        items[item] = items[item] + qty
    else:
        items[item] = qty
    print("ITEMS:", items)
print("Final ITEMS:", items)
