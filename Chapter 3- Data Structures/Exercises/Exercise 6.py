guests = ['Eric', 'Edward', 'Althea']

name = guests[0].title()
print(f"{name}, You're invited to the dinner that's coming up.")

name = guests[1].title()
print(f"{name}, You're invited to the dinner that's coming up.")

name = guests[2].title()
print(f"{name}, You're invited to the dinner that's coming up.")

name = guests[1].title()
print(f"\nSorry, {name} I'm unable to attend dinner.")

del(guests[1])
guests.insert(1, 'Kobe')

name = guests[0].title()
print(f"\n{name}, You're invited to the dinner that's coming up.")

name = guests[1].title()
print(f"{name}, You're invited to the dinner that's coming up.")

name = guests[2].title()
print(f"{name}, You're invited to the dinner that's coming up.")

print("\nThe table is larger now.!")
guests.insert(0, 'Lua')
guests.insert(2, 'Hamood')
guests.append('Ali')

name = guests[0].title()
print(f"{name}, You're invited to the dinner that's coming up.")

name = guests[1].title()
print(f"{name}, You're invited to the dinner that's coming up.")

name = guests[2].title()
print(f"{name}, You're invited to the dinner that's coming up.")

name = guests[3].title()
print(f"{name}, You're invited to the dinner that's coming up.")

name = guests[4].title()
print(f"{name}, You're invited to the dinner that's coming up.")

name = guests[5].title()
print(f"{name}, You're invited to the dinner that's coming up.")

print("\nWe apologize, but we can only have two dinner invitations.")

name = guests.pop()
print(f"Sorry, {name.title()} the table is completely full.")

name = guests.pop()
print(f"Sorry, {name.title()} the table is completely full.")

name = guests.pop()
print(f"Sorry, {name.title()} the table is completely full.")

name = guests.pop()
print(f"Sorry, {name.title()} the table is completely full.")

name = guests[0].title()
print(f"{name}, You're invited to the dinner that's coming up.")

name = guests[1].title()
print(f"{name}, You're invited to the dinner that's coming up.")

del(guests[0])
del(guests[0])

print(guests)