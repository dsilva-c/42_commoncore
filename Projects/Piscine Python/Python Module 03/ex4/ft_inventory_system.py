import sys


def parse_inventory(args: list[str]) -> dict[str, int]:
    """Parse inventory items from command-line arguments."""
    inventory: dict[str, int] = {}
    for arg in args:
        parts = arg.split(":")
        if len(parts) != 2:
            print(f"Error - invalid parameter '{arg}'")
            continue

        name = parts[0].strip()
        qty_str = parts[1].strip()
        if not name:
            print(f"Error - invalid parameter '{arg}'")
            continue

        if name in inventory:
            print(f"Redundant item '{name}' - discarding")
            continue

        try:
            qty = int(qty_str)
        except ValueError as exc:
            print(f"Quantity error for '{name}': {exc}")
            continue

        inventory.update({name: qty})
    return inventory


def ft_inventory_system() -> None:
    """Manage game inventory using dictionaries."""
    print("=== Inventory System Analysis ===")

    if len(sys.argv) < 2:
        print("Usage: python3 ft_inventory_system.py item:qty ...")
        return

    inventory = parse_inventory(sys.argv[1:])
    if not inventory:
        print("No valid inventory items provided.")
        return

    print(f"Got inventory: {inventory}")
    item_list = list(inventory.keys())
    print(f"Item list: {item_list}")

    total_qty = sum(inventory[name] for name in inventory)
    print(f"Total quantity of the {len(inventory)} items: {total_qty}")

    for name in inventory:
        pct = (inventory[name] / total_qty) * 100
        print(f"Item {name} represents {pct:.1f}%")

    inv_iter = iter(inventory)
    most_name = next(inv_iter)
    least_name = most_name
    for name in inv_iter:
        qty = inventory[name]
        if qty > inventory[most_name]:
            most_name = name
        if qty < inventory[least_name]:
            least_name = name

    print(
        f"Item most abundant: {most_name} "
        f"with quantity {inventory[most_name]}"
    )
    print(
        f"Item least abundant: {least_name} "
        f"with quantity {inventory[least_name]}"
    )

    inventory.update({"magic_item": 1})
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    ft_inventory_system()
