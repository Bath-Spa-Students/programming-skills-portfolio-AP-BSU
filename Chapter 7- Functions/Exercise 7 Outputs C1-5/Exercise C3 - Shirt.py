# Creating the functions and displaying of argument statement 
def make_shirt(size, message_text = "M&S"):

# Displaying the sentence summarizing the T-shirt size and message in set parameters with position priority
    print(f"A {size}-sized T-shirt is created with print: '{message_text}'.")

# Calling the 1st function argument
make_shirt("medium")

# Calling the 2nd function argument
make_shirt(size="large")