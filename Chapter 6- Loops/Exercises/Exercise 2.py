prompt = "\nWhat is your age?"
prompt += "\nOnce you're done, type 'quit.' "

while True:
    age = input(prompt)
    if age == 'quit':
        break
    age = int(age)

    if age < 3:
        print("  You enter at no cost!")
    elif age < 13:
        print("  It costs $10 to enter.")
    else:
        print("  Tickets cost $15.")