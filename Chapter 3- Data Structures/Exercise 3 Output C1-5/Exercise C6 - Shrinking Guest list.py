group_a = ["Adrian", "Alp", "Amel", "Arven"]

print("Remaining members:")
print(group_a)

while len(group_a) > 2:
    remove_members = group_a.pop(0)
    print(f"{remove_members} is no longer invited.")


for guest in group_a:
    print(f"{guest}, Is still invited to dinner.")

del group_a[0]
del group_a[0]

print("Final list:")
print(group_a)
