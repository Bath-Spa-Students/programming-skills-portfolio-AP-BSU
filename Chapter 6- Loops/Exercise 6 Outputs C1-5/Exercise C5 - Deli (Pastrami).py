# Sandwich orders and finished sandwiches lists
sandwich_orders = ["Turkey Sausage & Egg", "Breakfast Bagel", "Grilled Cheese Panini", "Fillet o Fish", "pastrami", "pastrami", "pastrami"]
finished_sandwiches = []

# Checking if 'pastrami' is in sandwich_orders
if "pastrami" in sandwich_orders:
    # Print a message saying the deli has run out of 'pastrami'
    print("The deli has run out of pastrami.\n")

    # Remove of all pastrami occurrences
    while "pastrami" in sandwich_orders:
        sandwich_orders.remove("pastrami")

# Looping of given list of sandwich orders
while sandwich_orders:
    current_order = sandwich_orders.pop(0)

    # Ordering of sandwiches
    print(f"Your order {current_order} is ready.")

    # Moving sandwich_orders via Dictionary append
    finished_sandwiches.append(current_order)

# Printing of listed sandwich that was made excluding pastrami
print("\nFinished Meal:\n")
for sandwich in finished_sandwiches:
    print(sandwich.capitalize())