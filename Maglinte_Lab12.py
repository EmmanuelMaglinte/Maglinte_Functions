# Food data
Food_List = ["Adobo", "Menudo", "Fried Rice", "Plain Rice", "Sinigang", "Pinakbet", "Tapsilog", "Pancit Canton", "Chopseuy", "Lechon Kawali"]
Food_Numbering = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Food_Cost = [42, 43, 20, 15, 50, 35, 50, 27, 42, 78]

# Display menu
print("Hi! Welcome to our food corner! What food are you interested in?")
print()
print(f"{' ':>1}{'Food':<20}{'Price (PHP)':>10}")
print(" - " * 30)

for numbering, food, price in zip(Food_Numbering, Food_List, Food_Cost):
    print(f"{numbering:>2}.{food:<20}{price:>10}")
print()

# Order process
Food_Order = []
while True:
        print("Enter food number (1 - 10 only)")
        user = input("Your order (or type 'done' to finish): ").strip()
        
        if user.lower() == "done":
            break
        elif user.isdigit() and int(user) in Food_Numbering:
            food_index = int(user) - 1
            Food_Order.append((Food_List[food_index], Food_Cost[food_index]))
            print(f"Added {Food_List[food_index]} to your order.")
        else:
            print("Invalid input. Please enter a valid food number.")

# Calculate total cost
if not Food_Order:
    print("\nNo items ordered. Thank you for visiting!")
    exit()

print("\nYour order summary:")
total_cost = 0
for food, price in Food_Order:
    print(f"{food:<20} - {price} PHP")
    total_cost += price

print(f"\nTotal cost: {total_cost} PHP")

# Payment processing
while True:
    try:
        cash = float(input("Enter cash amount: "))
        if cash >= total_cost:
            change = cash - total_cost
            print(f"\nPayment successful! Your change is {change:.2f} PHP.")
            print("Thank you for ordering! Have a great day!")
            break
        else:
            print(f"Insufficient cash. You need at least {total_cost - cash:.2f} PHP more.")
    except ValueError:
        print("Invalid input. Please enter a valid amount.")
