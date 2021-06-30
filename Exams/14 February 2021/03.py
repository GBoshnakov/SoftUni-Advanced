def stock_availability(inventory, *args):
    command = args[0]
    if command == "delivery":
        for el in args[1:]:
            inventory.append(el)
    elif command == "sell":
        if len(args) == 1:
            inventory = inventory[1:]
        else:
            for el in args[1:]:
                if type(el) == int:
                    inventory = inventory[int(el):]
                else:
                    if el in inventory:
                        inventory = [word for word in inventory if word != el]

    return inventory

print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie","banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))
