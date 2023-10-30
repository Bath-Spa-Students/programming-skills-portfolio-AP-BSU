# You can choose change the colour to 'green' or 'red' to change its variable color
alien_color = 'red'  

# ANSI text colors
green = '\033[92m'
yellow = '\033[93m'
red = '\033[91m'
reset = '\033[0m'

if alien_color == 'green':
    print("5 points the alien is green.")
else:
    print(red + "10 points \n The alien is red" + reset)