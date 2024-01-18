#Assignment 2.1: I/O with Python
# Jerome Reaux Jr.
# 01/21/2024

import math

# The code wants to get the user's name
name = input("Hello User, What is your name?\n")

name =str(name)

# The AI relays the name
print( 'Its nice to meet you ' + name)

print("\nI'm pretty good at math")
print("I can square any number\n ")

# Take user input for a number
sqr = input("Give it a try, enter a number: ")
sqr = int(sqr)

# Calculate the square root of the number the user gave
square_root = math.sqrt(sqr)

# Print the message of the AI doing math
print(f'Good pick of the number {sqr}, the square root of your number is {square_root}')

#User has to give another number
print('\n\nPretty good huh?\n I can also make numbers bigger as well by multiplying the number by itself')
multi = input('Give another number: ')

# Convert the user input to a numeric type
number = float(multi)

# The AI is putting the number to the 2nd power
multiplication = number ** 2

print('Thats easy the number is',multiplication)

print('\n That will be all for today\n till next time ' + name)


