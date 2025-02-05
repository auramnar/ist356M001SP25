items = {}
while True:
    item_name = input("Enter item name: ")
    if item_name == "quit":
        for i in items:
            print(i, items[i])
        break
    try: item_quantity = int(input("Enter item quantity: "))
    except ValueError:
        print("Please enter a number")
        continue
    if item_name in items.keys():
        items[item_name] += item_quantity
    else:
        items[item_name] = item_quantity