prompt = "\nWhich pizza topping would you prefer??"
prompt += "\nOnce you're done, type 'quit.': "

while True:
    topping = input(prompt)
    if topping != 'quit':
        print(f" I'll top your pizza with {topping}.")
    else:
        break

