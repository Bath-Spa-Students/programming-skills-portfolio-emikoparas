locations = ['Japan', 'Australia', 'Italy', 'Canada', 'Spain']

print("Original Order:")
print(locations)

print("\nAlphabetical Order:")
print(sorted(locations))

print("\nOriginal Order:")
print(locations)

print("\nReverse Alphabetical:")
print(sorted(locations, reverse=True))

print("\nOriginal Order:")
print(locations)

print("\nReverse Alphabetical:")
locations.reverse()
print(locations)

print("\nOriginal Order:")
locations.reverse()
print(locations)

print("\nAlphabetical")
locations.sort()
print(locations)

print("\nReverse Alphabetical")
locations.sort(reverse=True)
print(locations)