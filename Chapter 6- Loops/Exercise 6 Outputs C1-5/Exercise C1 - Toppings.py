# Variable to list
pizza_toppings = []

# Saved user inputs
user_input_text = ""

# Input and statement with a custom prompt and user input to break the loop
while True:
    topping = input("Would you like to add a pizza topping? Type 'quit' or exit program to end: ")
    
    if topping.lower() == 'quit':
        break
    else:
        pizza_toppings.append(topping)
        user_input_text += topping + " "  # Append the input to the user_input_text variable

# Printing of text and user's history of entered texts
print("You have placed the following pizza toppings:")
for topping in pizza_toppings:
    print(f"- {topping}")
print("\nEnd of program ")
