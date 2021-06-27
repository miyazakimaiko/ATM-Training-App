import os
import getpass

def display_change_pin_option_title():
    os.system('cls' if os.name == 'nt' else 'clear')

    print()
    print('Selected: 1. Change PIN')
    print()


def get_pin_via_input(message):
    pin = getpass.getpass(prompt=message, stream=None)

    try:
        pin = int(pin)
    except:
        print("❌ Format Error: Please enter digits.")
        pin = get_pin_via_input(message)

    if len(str(pin)) != 4:
        print("❌ Error: PIN should be four digits.")
        pin = get_pin_via_input(message)

    return pin


def is_pin_matched(pin, user):
    if pin == user['PIN']:
        return True

    return False


def verify_current_pin(user):
    pin_matched = False

    pin = get_pin_via_input(message='Please enter CURRENT PIN: 🔑')
    pin_matched = is_pin_matched(pin, user)

    if not pin_matched:
        print('❌ Wrong PIN.')
        pin = verify_current_pin(user)

    
def set_new_pin(user):
    new_pin = get_pin_via_input(message='Please enter NEW PIN: 🔑')
    new_pin_retype = get_pin_via_input(message='Please re-enter the NEW PIN: 🔑')

    if new_pin == new_pin_retype:
        user['PIN'] = new_pin
        print()
        print('Thank you. New PIN is set to the current PIN successfully.')
        print()
        # user_main_menu.py guides the user to the User Main Menu... 
    else:
        print('New PIN does not match...')
        set_new_pin(user)


def main(user):
    display_change_pin_option_title()

    verify_current_pin(user)

    set_new_pin(user)

