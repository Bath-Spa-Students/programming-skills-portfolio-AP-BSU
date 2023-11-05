# Dictionary for different pet and their owner
pet1 = {'Kind': 'Dog', 'Owner': 'Matthew'}
pet2 = {'Kind': 'Cat', 'Owner': 'Agatha'}
pet3 = {'Kind': 'Bird', 'Owner': 'Amel'}
pet4 = {'Kind': 'Snake', 'Owner': 'Dank'}

# Variables
pets = [pet1, pet2, pet3, pet4]

# Looping of given list and printing of information about each pet
for pet in pets:
    print(f"Animal: {pet['Kind']}")
    print(f"Owner: {pet['Owner']}")
    print()
