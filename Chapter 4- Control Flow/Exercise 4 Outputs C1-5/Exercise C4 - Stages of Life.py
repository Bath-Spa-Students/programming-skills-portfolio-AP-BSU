age = int(input("Variable Age: "))

# ANSI text colors
green = '\033[92m'
yellow = '\033[93m'
red = '\033[91m'
reset = '\033[0m'

if age <2:
    print(green + "Your a baby." + reset)
elif age >= 2 and age < 4:
    print (green + "You are a toddler" + reset)
elif age >= 4 and age < 13:
    print (yellow + "You are a child" + reset)
elif age >= 13 and age < 18:
    print (yellow + "You are a teenager" + reset)
elif age >= 18 and age < 60:
    print(yellow + "You are a adult." + reset)
else:
    print (red + "You are a elder" + reset)
