# Guided Exploration No. 3
# ETHAN CUNNINGHAM

# Imports the random library. We're using random.randint() in the program
import random

# Sets possible_names as an empty list, which is where the rap names from rap-names.txt will be stored
possible_names = []

# Opens a new file rap-names-output.txt that is in write mode in the variable outputFile
outputFile = open('rap-names-output.txt', 'w')

# Opens rap-names.txt in read and with it, executes the below
with open('rap-names.txt', 'r') as dataFile:
    # A loop that looks at all the words in rap-names.txt
    for name in dataFile:
        # Appends each word from rap-names.txt using .rstrip() into the possible_names list
        possible_names.append(name.rstrip())

# Asks user to input the amount of rap names they want to create in count, stored as an int
count = int(input('How many rap names would you like to create? '))
# Asks user to input the amount of parts in the name they want to create in parts, stored as an int
parts = int(input('How many parts should the name contain? '))

# loops through each rap name the user wants to create
for i in range(count):
    # sets name_parts as an empty list, where the rap name parts will be held
    name_parts = []
    # loops through each part of the name that the user wants to create
    for j in range(parts):
        # For each iteration, one name from possible_names is taken at random using random.randint. Then, that name is appended onto the name_parts list
        name_parts.append(
            possible_names[random.randint(0, len(possible_names)-1)])

    # Adds the created rap name from name_parts to rap-names-output.txt, joining the words in name_parts together with a space seperating them
    outputFile.write(f"{' '.join(name_parts)}\n")
    # Prints the rap name in the VS terminal, joining the words in name_parts together with a space seperating them
    print(f"{' '.join(name_parts)}")

# Closes the rap-names-output.txt file
outputFile.close()
