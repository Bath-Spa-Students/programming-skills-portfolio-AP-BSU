# sandwich orders and finished sandwiches lists
sandwich_orders = ["Turkey Sausage & Egg", "Breakfast Bagel", "Grilled Cheese Panini", "Fillet o Fish"]
finished_sandwiches = []

# Looping of given list of sandwich orders
while sandwich_orders:
    current_order = sandwich_orders.pop(0)

    # Ordering of sandwiches
    print(f"Your order {current_order} is ready.")

    # Moving sandwich_orders via Dictionary append
    finished_sandwiches.append(current_order)

# Printing of listing each sandwich that was made
print("\nFinished Meal:\n")
for sandwich in finished_sandwiches:
    print(sandwich.capitalize())