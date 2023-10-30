# You change it to 'green', 'yellow' 'red' to change color
alien_color = 'yellow'

# ANSI text colors
green = '\033[92m'
yellow = '\033[93m'
red = '\033[91m'
reset = '\033[0m'

if alien_color == 'green':
    print(green + "Player earned 5 points for shooting the green alien." + reset)

elif alien_color == 'yellow':
    print(yellow + "Player earned 10 points for shooting the yellow alien." + reset)

elif alien_color == 'red':
    print(red + "Player earned 15 points for shooting the red alien." + reset)