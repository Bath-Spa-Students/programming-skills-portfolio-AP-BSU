# You choose it to 'green', 'yellow' or 'red' to change color
alien_color = 'red'

# ANSI text colors
green = '\033[92m'
yellow = '\033[93m'
red = '\033[91m'
reset = '\033[0m'

if alien_color == 'green':
    print(green + "+5 points." + reset)
elif alien_color == 'yellow' or alien_color == 'red':
    print(yellow + "output ended" + reset)
else:
    print("Invalid alien color.")