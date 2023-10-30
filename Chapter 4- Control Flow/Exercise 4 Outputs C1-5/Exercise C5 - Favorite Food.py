# List of popular European foods (Not fruits)
food_list = ["Pizza", "Pasta", "Croissant", "Paella", "Sausages", "Schnitzel", "Goulash", "Moussaka"]

user_input = input("Choose a European food: \n Pizza, Pasta, Croissant, Paella, Sausages, Schnitzel, Goulash, Moussaka \n:")

if user_input in ["Pizza", "Sausages", "Pasta"]:
    print(f"You really like {user_input}!")
else:
    print("That's not my favorite")