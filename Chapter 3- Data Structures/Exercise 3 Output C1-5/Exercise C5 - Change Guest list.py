group_a = ["Adrian", "Alp", "Amel"]

if "Alp" in group_a:
    group_a[group_a.index("Alp")] = "Arven"

for name in group_a:
    print(f"Dear {name},\nYou are invited to dinner.\n")

if "Alp" not in group_a and "Arven" in group_a:
    print("Note: Alp has declined \n Arven has joined the dinner.")
