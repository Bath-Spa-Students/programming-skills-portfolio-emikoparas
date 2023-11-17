glossary = {
    'Interpreter': 'Translates and executes instructions in high-level language.',
    'Assembler': 'Uses short words for instructions instead of binary numbers.',
    'Fetch': 'Read the next instructions from memory into CPU.',
    'Compiler': 'Translates high-level language program into seperate machine language.',
    'Syntax': "Set of rules to be followed when writing prgram",
    'Key': 'The first item in a key-value pair in a dictionary.',
    'Value': 'An item associated with a key in a dictionary.',
    'Conditional test': 'A comparison between two values.',
    'Float': 'A numerical value with a decimal component.',
    'Boolean expression': 'An expression that evaluates to True or False.',
    }

for word, definition in glossary.items():
    print("\n" + word.title() + ": " + definition)