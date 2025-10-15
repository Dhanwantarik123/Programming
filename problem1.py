# --- Inventory Shop Menu Program ---

items = []

while True:
    print("\n----- INVENTORY SHOP MENU -----")
    print("1. Enter item numbers")
    print("2. Display total number of items")
    print("3. Display last item number")
    print("4. Display sorted list of items")
    print("5. Check if item number 515 is present")
    print("6. Remove first and last items and show modified list")
    print("7. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        n = int(input("Enter total number of items: "))
        items = []
        for i in range(n):
            num = int(input("Enter item number: "))
            items.append(num)
        print("Items added successfully!")

    elif choice == 2:
        print("Total number of items:", len(items))

    elif choice == 3:
        if len(items) > 0:
            print("Last item number:", items[-1])
        else:
            print("List is empty.")

    elif choice == 4:
        print("Sorted list of items:", sorted(items))

    elif choice == 5:
        if 515 in items:
            print("Yes, 515 is present in the list.")
        else:
            print("No, 515 is not present in the list.")

    elif choice == 6:
        if len(items) > 2:
            modified_list = items[1:-1]
            modified_list.sort()
            print("Modified list (after removing first & last):", modified_list)
        else:
            print("Not enough items to modify.")

    elif choice == 7:
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Please try again.")

