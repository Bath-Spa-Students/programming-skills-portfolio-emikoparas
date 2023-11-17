guests = ['Althea', 'Edward', 'Eric']

name = guests[0].title()
print(f"{name}, You are invited to the dinner.")

name = guests[1].title()
print(f"{name}, You are invited to the dinner.")

name = guests[2].title()
print(f"{name}, You are invited to the dinner.")

name = guests[1].title()
print(f"\nSorry, {name} I'm unable to attend dinner.")

del(guests[1])
guests.insert(1, 'Kobe')

name = guests[0].title()
print(f"\n{name}, You are invited to the dinner.")

name = guests[1].title()
print(f"{name}, You are invited to the dinner.")

name = guests[2].title()
print(f"{name}, You are invited to the dinner.")