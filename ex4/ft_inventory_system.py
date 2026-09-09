import sys 

print("=== Inventory System Analysis ===")

inventory = {}

for args in sys.argv[1:]:
    original = args
    args = args.split(":")
    if len(args) != 2:
        print(f"Error - invalid parameter '{original}'")
        continue
    item = args[0]
    try:
        quantity = int(args[1])
    except ValueError as error:
        print(f"Quantity error for '{item}': {error}")
        continue
    if item in inventory:
        print(f"Redundant item '{item}' - discarding")
    else:
        inventory[item] = quantity

print(f"Got inventory: {inventory}")
item_list = list(inventory.keys())
print(f"Item list: {item_list}")
total_quantity = sum(inventory.values())
print(f"Total quantity of the {len(inventory)} items: {total_quantity}")

if item_list:
    for item in item_list:
        quantity = inventory[item]
        percentage = round((quantity / total_quantity) * 100, 1)
        print(f"Item {item} represents {percentage}%")

    most_abundant = item_list[0]
    most_quantity = inventory[item_list[0]]
    for item in item_list:
        quantity = inventory[item]
        if quantity > most_quantity:
            most_abundant = item
            most_quantity = quantity
    print(f"Item most abundant: {most_abundant} with quantity {most_quantity}")

    least_abundant = item_list[0]
    least_quantity = inventory[item_list[0]]
    for item in item_list:  
        quantity = inventory[item]
        if quantity < least_quantity:
            least_abundant = item
            least_quantity = quantity
    print(f"Item least abundant: {least_abundant} with quantity {least_quantity}")

inventory.update({"magic_item": 1})
print(f"Updated inventory: {inventory}")