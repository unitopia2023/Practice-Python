# Exercise: Create a Simple To-Do List Application
# Objective:
# Build a simple command-line To-Do List application that allows users to add, view, and remove tasks.

# Requirements:
# Add Task: Prompt the user to input a task and add it to the list.
# View Tasks: Display all the current tasks in the list with their corresponding index numbers.
# Remove Task: Prompt the user to select a task to remove by index.


task_list = []

def prompt(a):
    while True:
        action = input(a)
        if action == '1':
            task_list.append(input('Add a task: '))
        elif action == '2':
            break
        else:
            print('Error: command unidentified.')

prompt('Enter [1] to add task, [2] to exit: \n')

# for task in task_list:
#     i = task_list.index(task) + 1
#     print(i, task)

for i, task in enumerate(task_list, start=1):
    print(i, task)