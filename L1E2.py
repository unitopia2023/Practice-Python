# Exercise: Count Vowels in a String
# Task: Write a program that counts the number of vowels (a, e, i, o, u) in a given string entered by the user.

# Requirements:

# Prompt the user to enter a string.
# Count the number of vowels in the string.
# Print the total count of vowels.

print('This program counts the vowels in a given string.')

user_input = input('Enter a string below: \n')

vowels = []
for i in user_input.lower():
    if i in ['a', 'e', 'i', 'o', 'u']:
        vowels.append(i)

print(vowels, len(vowels))
