import os

def run_user_main_menu(user):
    show_user_main_menu_title()

    number = get_number_via_input()

    if number == 1:
        from functions import change_pin
        change_pin.main(user)
        input('Press Enter to go back to the User Main Menu...')
        run_user_main_menu(user)

    elif number == 2:
        from functions import withdraw_money
        withdraw_money.main(user)
        input('Press Enter to go back to the User Main Menu...')
        run_user_main_menu(user)

    elif number == 3:
        from functions import lodge_money
        lodge_money.main(user)
        input('Press Enter to go back to the User Main Menu...')
        run_user_main_menu(user)

    elif number == 4:
        from functions import view_statement
        view_statement.main(user)
        input('Press Enter to go back to the User Main Menu...')
        run_user_main_menu(user)

    elif number == 5:
        from functions import logout
        logout.main()


def show_user_main_menu_title():
    os.system('cls' if os.name == 'nt' else 'clear')

    print()
    print('User Main Menu')
    print()
    print('____Option_____')
    print('1. Change PIN')
    print('2. Withdrawal')
    print('3. Lodgement')
    print('4. View Statement')
    print('5. Log Out')
    print()


def get_number_via_input():
    number = input('Please enter a number from 1 to 6: ')

    try:
        number = int(number)
    except:
        print('❌ Format Error: it is not a digit.')
        number = get_number_via_input()

    if number > 6 or number < 1:
        print('❌ Entered Digit Out of Range Error')
        number = get_number_via_input()

    return number