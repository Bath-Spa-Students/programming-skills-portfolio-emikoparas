pets = []

pet = {
    'Kind of Animal': 'Rabbit',
    'Name': 'Peter',
    'Owner': 'Vince',
    'Weight': 2,
    'Eats': 'Hay',
}
pets.append(pet)

pet = {
    'Kind of Animal': 'Dog',
    'Name': 'Kobe',
    'Owner': 'Emiko',
    'Weight': 45,
    'Eats': 'Vegetables',
}
pets.append(pet)

pet = {
    'Kind of Animal': 'Hamster',
    'Name': 'Nibbles',
    'Owner': 'Edward',
    'Weight': 1,
    'Eats': 'Carrots',
}
pets.append(pet)

for pet in pets:
    print(f"\nThis is what I am aware of {pet['Name'].title()}:")
    for key, value in pet.items():
        print(f"\t{key}: {value}")