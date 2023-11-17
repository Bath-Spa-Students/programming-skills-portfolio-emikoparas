sandwich_orders = ['Cheese', 'Chicken', 'Veggie', 'Lamb']
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print("As I work on your " + current_sandwich + " sandwich.")
    finished_sandwiches.append(current_sandwich)

print("\n")
for sandwich in finished_sandwiches:
    print("I created a " + sandwich + " sandwich.")