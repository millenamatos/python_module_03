import sys 

def main() -> None:
    print("=== Inventory System Analysis ===")

    inventory: dict[str, int] = {}

    for arg in sys.argv[1:]:
        original: str = arg
        parts: list[str] = arg.split(":")

        if len(parts) != 2:
            print(f"Error - invalid parameter '{original}'")
            continue

        item: str = parts[0]
        try:
            quantity: int = int(parts[1])
        except ValueError as error:
            print(f"Quantity error for '{item}': {error}")
            continue

        if item in inventory:
            print(f"Redundant item '{item}' - discarding")
        else:
            inventory[item] = quantity

    print(f"Got inventory: {inventory}")

    item_list: list[str] = list(inventory.keys())
    print(f"Item list: {item_list}")

    total_quantity: int = sum(inventory.values())
    print(f"Total quantity of the {len(inventory)} items: {total_quantity}")

    if item_list:
        for item in item_list:
            qty: int = inventory[item]
            percentage: float = round((qty / total_quantity) * 100, 1)
            print(f"Item {item} represents {percentage}%")

        most_abundant: str = item_list[0]
        most_quantity: int = inventory[item_list[0]]
        for item in item_list:
            qty = inventory[item]
            if qty > most_quantity:
                most_abundant = item
                most_quantity = qty
        print(f"Item most abundant: {most_abundant} with quantity {most_quantity}")

        least_abundant: str = item_list[0]
        least_quantity: int = inventory[item_list[0]]
        for item in item_list:  
            qty = inventory[item]
            if qty < least_quantity:
                least_abundant = item
                least_quantity = qty
        print(f"Item least abundant: {least_abundant} with quantity {least_quantity}")

    inventory.update({"magic_item": 1})
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    main()