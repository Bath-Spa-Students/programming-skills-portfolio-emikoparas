rivers = {
    'Nile': 'Egypt',
    'Ganges': 'India',
    'Brahmaputra': 'China, Bangladesh & China',
    }

for river, country in rivers.items():
    print(f"The {river.title()} flows through {country.title()}.")

print("\nThis data collection includes the rivers listed below.:")
for river in rivers.keys():
    print(f"- {river.title()}")

print("\nThis data collection includes the following countries.:")
for country in rivers.values():
    print(f"- {country.title()}")