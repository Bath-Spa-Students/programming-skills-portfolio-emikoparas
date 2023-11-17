sandwich_orders = [
    'Pastrami', 'Chicken', 'Cheese', 'Pastrami',
    'Beef', 'Veggie', 'Pastrami']
finished_sandwiches = []

print("We're all out of Pastrami today, I apologize.")
while 'Pastrami' in sandwich_orders:
    sandwich_orders.remove('Pastrami')

print("\n")
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print("As I work on your " + current_sandwich + " sandwich.")
    finished_sandwiches.append(current_sandwich)

print("\n")
for sandwich in finished_sandwiches:
    print("I created a " + sandwich + " sandwich.")