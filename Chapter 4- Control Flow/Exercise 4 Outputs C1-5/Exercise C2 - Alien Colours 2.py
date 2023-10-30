# You choose it to 'green' or 'red' to change color
alien_color = 'green'

# ANSI text colors
green = '\033[92m'
yellow = '\033[93m'
red = '\033[91m'
reset = '\033[0m'

if alien_color == 'green':
    print(green + "5 points! \n The alien is green." + reset)
else:
    print("10 points!")