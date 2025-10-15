# --- Shop Selling Menu Program ---

def find_sum(prices):
    total = 0
    for p in prices:
        total += p
    return total

def find_max(prices):
    max_price = prices[0]
    for p in prices:
        if p > max_price:
            max_price = p
    return max_price

def find_min(prices):
    min_price = prices[0]
    for p in prices:
        if p < min_price:
            min_price = p
    return min_price


prices = ()

while True:
    print("\n----- SHOP SELLING MENU -----")
    print("1. Enter prices of sold items")
    print("2. Display total selling of the day")
    print("3. Display costliest item price")
    print("4. Display cheapest item price")
    print("5. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        n = int(input("Enter number of sold items: "))
        lst = []
        for i in range(n):
            price = float(input("Enter price of item: "))
            lst.append(price)
        prices = tuple(lst)
        print("Prices stored successfully!")

    elif choice == 2:
        if len(prices) == 0:
            print("No data entered yet.")
        else:
            print("Total selling of the day:", find_sum(prices))

    elif choice == 3:
        if len(prices) == 0:
            print("No data entered yet.")
        else:
            print("Costliest item sold:", find_max(prices))

    elif choice == 4:
        if len(prices) == 0:
            print("No data entered yet.")
        else:
            print("Cheapest item sold:", find_min(prices))

    elif choice == 5:
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Please try again.")

