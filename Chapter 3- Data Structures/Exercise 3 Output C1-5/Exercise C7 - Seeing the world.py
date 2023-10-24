countries = ["United Kingdom", "Philippines", "United States", "Spain", "Maxico"]

print("Original List:")
print(countries)

print("\nAlphabetical Order:")
print(sorted(countries))

print("\nOriginal List again:")
print(countries)

print("\nReverse Order (Starting from US):")
print(sorted(countries, reverse=True))

print("\nOriginal List again, again:")
print(countries)

countries.reverse()

print("\nReversed Order:")
print(countries)

countries.reverse()

print("\nOriginal Order (Reversed):")
print(countries)

countries.sort()

print("\nAlphabetical Order:")
print(countries)

countries.sort(reverse=True)

print("\nReversed Alphabetical Order:")
print(countries)
