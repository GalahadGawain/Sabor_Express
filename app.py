import os

restaurants = [
    {'name': 'Clandestino', 'category': 'Mexican', 'status': False},
    {'name': 'Napoletana', 'category': 'Italian', 'status': True},
    {'name': 'Coyote', 'category': 'Burger', 'status': True}
]

def display_program_name():
    ''' Displays the program's title. '''
    os.system('cls')
    print('''
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
    ''')

def display_menu_options():
    ''' Displays the main menu options. '''
    print('1. Register restaurant')
    print('2. List restaurants')
    print('3. Toggle restaurant status')
    print('4. Exit\n')

def end_app():
    ''' Ends the application. '''
    display_subtitle('Thank you for using Sabor Express!\n')
    print('Closing the program...')

def return_to_main_menu():
    ''' Waits for user confirmation and returns to the main menu. '''
    input('\nPress Enter to return to the main menu...\n')
    main()

def display_subtitle(text):
    ''' Displays a subtitle with formatting. '''
    os.system('cls')
    line = '*' * (len(text))
    print(line)
    print(text)
    print(line)

def invalid_option():
    ''' Informs the user of an invalid menu option. '''
    print('Invalid option. Try again.\n')
    return_to_main_menu()

def register_restaurant():
    ''' Registers a new restaurant. '''
    display_subtitle('Restaurant Registration')
    restaurant_name = input('Enter the restaurant name:\n')
    restaurant_category = input(f'Enter the category for {restaurant_name}:\n')
    restaurant_data = {'name': restaurant_name, 'category': restaurant_category, 'status': False}
    restaurants.append(restaurant_data)
    print(f'Restaurant {restaurant_name} registered successfully!\n')
    return_to_main_menu()

def list_restaurants():
    ''' Lists all registered restaurants. '''
    display_subtitle('Restaurant List')
    print(f'\n  {'Restaurant Name'.ljust(20)} | {'Category'.ljust(20)} | {'Status'}')
    print('-' * 60)
    for restaurant in restaurants:
        name = restaurant['name']
        category = restaurant['category']
        status = 'Active' if restaurant['status'] else 'Inactive'
        print(f'- {name.ljust(20)} | {category.ljust(20)} | {status}\n')
    return_to_main_menu()

def toggle_restaurant_status():
    ''' Toggles the status of a selected restaurant. '''
    display_subtitle('Toggle Restaurant Status')
    restaurant_name = input('Enter the name of the restaurant to toggle status:\n')
    found = False
    for restaurant in restaurants:
        if restaurant_name == restaurant['name']:
            found = True
            restaurant['status'] = not restaurant['status']
            message = f'{restaurant_name} successfully activated!\n' if restaurant['status'] else f'{restaurant_name} successfully deactivated!'
            print(message)
    if not found:
        print(f'Restaurant {restaurant_name} not found.\n')
    return_to_main_menu()

def choose_option():
    ''' Handles the user's menu option selection. '''
    try:
        chosen_option = int(input('Choose an option: '))

        if chosen_option == 1:
            register_restaurant()
        elif chosen_option == 2:
            list_restaurants()
        elif chosen_option == 3:
            toggle_restaurant_status()
        elif chosen_option == 4:
            end_app()
        else:
            invalid_option()
    except:
        invalid_option()  

def main():
    ''' Runs the program. '''
    os.system('cls')
    display_program_name()
    display_menu_options()
    choose_option()

if __name__ == '__main__':
    main()
