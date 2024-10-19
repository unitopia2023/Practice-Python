# Exercise: Build a Simple Contact Book Application
# Objective
# Create a command-line contact book that allows users to add, view, search, update, and delete contacts. Each contact will have a name, phone number, and email address.


contact_list = []
deleted_list= []

def view_contact(prompt):
    print(f'{prompt} CONTACT LIST')
    print()
    for index, dict_item in enumerate(contact_list):
        print(f'Contact: {index}')
        for key, value in dict_item.items():
            print(f'{key}: {value}')
        print()

def add_contact():
    print('\nADDING A CONTACT\n')
    contact = {}
    contact['name'] = input('Name: ')
    contact['phone_number'] = input('Phone number: ')
    contact['email'] = input('Email: ')
    contact_list.append(contact)
#     print(f'''
# Contact successfully added!

# {view_contact('UPDATED')}
# ''')
    # return contact_list
 
def search(search_type):
    search_term = input(f'Input {search_type}: ').lower()
    found = False
    for dict_item in contact_list:
        if search_type == 'name' and search_term in dict_item['name'].lower():
            for key, value in dict_item.items():
                print(f'{key}: {value}')
            print()
            found = True
        elif search_type == 'phone_number' and search_term in dict_item['phone_number'].lower():
            for key, value in dict_item.items():
                print(f'{key}: {value}')
            print()
            found = True
        elif search_type == 'email' and search_term in dict_item['email'].lower():
            for key, value in dict_item.items():
                print(f'{key}: {value}')
            print()
            found = True
        if not found:
                print(f'Sorry {search_type} not found!')
        
def search_contact():
    print('\nSEARCH A CONTACT\n')
    while True:
        try:
            search_type = input('Type of search: [1]Name, [2]Phone number, [3]Email, [4]Exit\nType the number of your option: ')
            if search_type == '1': 
                search('name')
            elif search_type == '2':
                search('phone_number')
            elif search_type == '3':
                search('email')
            elif search_type == '4':
                menu_options()
        except ValueError:
            print('Sorry, invalid option!')

def update_contact():
    upd_index = int(input(f'''

UPDATING CONTACT DETAILS
                      
Select the index of the contact you want to update:
{view_contact('DISPLAYING')}

Delete the contact in index: ')
'''))
    contact_list[upd_index]['name'] = input('Name: ')
    contact_list[upd_index]['phone_number'] = input('Phone number: ')
    contact_list[upd_index]['email'] = input('Email: ')
    print(f'''

This contact was updated successfully.

{upd_index}\n\n{view_contact('UPDATED')}
          
''')

def delete_contact():
    try:
        del_index = int(input(f'''
Removing a contact
Select the index of the contact you want to remove:
{view_contact('Displaying')}
Select the number: 
'''))

        x = contact_list.pop(del_index)
        deleted_list.append(x)
        print(f'''

Contact deleted successfully!
          
{view_contact('UPDATED')}
        
''')
    except ValueError:
        print('Invalid index selected')

def menu_options():
    while True:
        try:
            option = input(
'''
SELECT OPTIONS: [1]Add, [2]View, [3]Search, [4]Update, [5]Delete:
''')
            if option == '1':
                add_contact()
            elif option == '2':
                view_contact('\nDISPLAYING')
            elif option == '3':
                search_contact()
            elif option == '4':
                update_contact()
            elif option == '5':
                delete_contact()
            else:
                print('Sorry, invalid input!')
        except ValueError:
            print('Sorry, invalid input!')

list_length = len(contact_list)
if  list_length == 0:
    add_contact()
menu_options()

    


