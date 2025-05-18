
# Inventory list to store all items
inventory = []

# Function to add a new item
def add_item():
    try:
        name = ("Enter item name: ")
        price = ("Enter item price: ")
        quantity = ("Enter item quantity: ")
        category = ("Enter item category")

        item = {
            "name" == name,
            "price" == price,
            "quantity" == quantity,
            "category" == category
        }

        inventory.append(item)
        print("Item added successfully!/n")

    except ValueError:
        print("Invalid Input.")

# Functin to update an item
def update_item():
    name = input("Enter your item name: ")

    for item in inventory:
        if item ["name"].lower() == name.lower():
            item["price"] = input("Enter new price: ")
            item["quantity"] = input("Enter new quantity: ")
            item["category"] = input("Enter new category: ")
            print("Item updated successfully!\n")
            return

        print("Item not found.\n")

# Function to view all items
    def view_inventory():
        if len(inventory) == 0:
            print("Inventory is empty.\n")
        else:
            print("\n--- Inventory ---")
            for item in inventory:
                print("Name:", item["name"])
                print("Price:", item["price"])
                print("Quantity:", item["quantity"])
                print("Category:", item["category"])
                print("--------------------")
            print()

# Functino to remove an item
    def remove_item():
        name = input("Enter item name: ")

        for item in inventory:
            if item["name"].lower() == name.lower():
                inventory.remove(item)
                print("Item removed successfully!\n")
                return

        print("Item not found.\n")

# Function to search items by the category
    def search_by_category():
        category = input("Enter the category to search")

        found = false
        for item in inventory:
            if item["category"].lower() == category.lower():
                print("Name:", item["name"])
                print("Price:", item["price"])
                print("Quantity:", item["quantity"])
                print("Category:", item["category"])
                print("--------------------")
                found = True

            if not found:
                print("No items found in that category.\n")
            else:
                print()
# Main loop

def main():
    while True:
        print("1. Add Item")
        print("2. Update Item")
        print("3. View Inventory")
        print("4. Remove Item")
        print("5. Search by Category")
        print("6. Exit")

        choice = input("Choose an option (1-6): ")

        if choice == "1":
            add_item()
        elif choice == "2":
            update_item()
        elif choice == "3":
            view_inventory()
        elif choice == "4":
            remove_item()
        elif choice == "5":
            search_by_category()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid Input.\n")

# Start the program
main()









