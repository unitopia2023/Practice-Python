# Level 1 Exercise1: Find the Largest Number
# Objective: Write a Python program that takes three numbers as input from the user and finds the largest number among them.

# Instructions:

# Prompt the user to enter three numbers.
# Create a function named find_largest that takes three numbers as input and returns the largest one.
# Print the largest number.
# Try this out, and let me know if you'd like to see the solution or need any assistance!

print('This program finds and prints the largest number.')

def input_func(prompt):
    while True:
        num = input(prompt)
        if num.isdigit():
            return int(num)
        else:
            print('\nPlease enter a numeric value!\n')

my_nums = [
    input_func('Input first number: '),
    input_func('Input second number: '),
    input_func('Input third number: ')
]

print(f'The largest number among {my_nums[0]}, {my_nums[1]} and {my_nums[2]} is {max(my_nums)}.')

