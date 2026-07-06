# ========================================
#        Inventory Management System
# ========================================

# Main inventory list
# Each item = [ID, Name, Quantity, Price]
inventory = []


# ----------------------------
#        Add New Item
# ----------------------------
def add_item():
    item_id = input("Enter Item ID: ").strip()

    if item_id == "":
        print("Error: Item ID cannot be empty.")
        return

    # Check duplicate ID
    for item in inventory:
        if item[0] == item_id:
            print("Error: This Item ID already exists.")
            return

    name = input("Enter Item Name: ").strip()

    if name == "":
        print("Error: Item name cannot be empty.")
        return

    try:
        quantity = int(input("Enter Quantity: "))
        price = float(input("Enter Price: "))
    except ValueError:
        print("Error: Quantity must be an integer and price must be a number.")
        return

    if quantity < 0 or price < 0:
        print("Error: Quantity and price cannot be negative.")
        return

    inventory.append([item_id, name, quantity, price])

    print("Success: Item added successfully!")


# ----------------------------
#      View Inventory
# ----------------------------
def view_inventory():

    if len(inventory) == 0:
        print("\nInventory is empty.")
        return

    print("\n" + "=" * 60)
    print(f"{'ID':<10}{'Name':<20}{'Qty':<10}{'Price':<10}")
    print("=" * 60)

    total_value = 0

    for item in inventory:
        print(f"{item[0]:<10}{item[1]:<20}{item[2]:<10}${item[3]:.2f}")
        total_value += item[2] * item[3]

    print("=" * 60)
    print(f"Total Products : {len(inventory)}")
    print(f"Inventory Value: ${total_value:.2f}")


# ----------------------------
#      Update Quantity
# ----------------------------
def update_quantity():

    if len(inventory) == 0:
        print("Inventory is empty.")
        return

    item_id = input("Enter Item ID to update: ").strip()

    for item in inventory:

        if item[0] == item_id:

            try:
                new_quantity = int(input("Enter New Quantity: "))
            except ValueError:
                print("Error: Quantity must be an integer.")
                return

            if new_quantity < 0:
                print("Quantity cannot be negative.")
                return

            item[2] = new_quantity

            print("Success: Quantity updated.")
            return

    print("Error: Item not found.")


# --------------------------
#       Delete Item
# --------------------------
def delete_item():

    if len(inventory) == 0:
        print("Inventory is empty.")
        return

    item_id = input("Enter Item ID to delete: ").strip()

    for item in inventory:

        if item[0] == item_id:

            confirm = input(
                f"Delete '{item[1]}'? (Y/N): ").strip().lower()

            if confirm == "y":
                inventory.remove(item)
                print("Success: Item deleted.")
            else:
                print("Deletion cancelled.")

            return

    print("Error: Item not found.")


# -------------------------
#       Search Item
# -------------------------
def search_item():

    if len(inventory) == 0:
        print("Inventory is empty.")
        return

    item_id = input("Enter Item ID to search: ").strip()

    for item in inventory:

        if item[0] == item_id:

            print("\nItem Found")
            print("-" * 30)
            print(f"ID       : {item[0]}")
            print(f"Name     : {item[1]}")
            print(f"Quantity : {item[2]}")
            print(f"Price    : ${item[3]:.2f}")

            return

    print("Error: Item not found.")


# --------------------------
#       Main Program
# --------------------------
while True:

    print("\n" + "=" * 35)
    print(" INVENTORY MANAGEMENT SYSTEM ")
    print("=" * 35)

    print("1. Add New Item")
    print("2. View Inventory")
    print("3. Update Item Quantity")
    print("4. Delete Item")
    print("5. Search Item")
    print("6. Exit")

    choice = input("\nEnter your choice (1-6): ").strip()

    if choice == "1":
        add_item()

    elif choice == "2":
        view_inventory()

    elif choice == "3":
        update_quantity()

    elif choice == "4":
        delete_item()

    elif choice == "5":
        search_item()

    elif choice == "6":
        print("\n" + "=" * 40)
        print("Thank you for using")
        print("Inventory Management System")
        print("Goodbye!")
        print("=" * 40)
        break

    else:
        print("Invalid choice! Please enter a number between 1 and 6.")