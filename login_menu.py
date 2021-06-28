import os
import getpass
from data import users

def show_login_menu_title():
    os.system('cls' if os.name == 'nt' else 'clear')

    print()
    print("ATM Training App Login Page")
    print()


def get_userid_via_input():
    id = input("Please enter your USERID: ")

    try:
        id = int(id)
    except:
        print("❌ Format Error: Please enter digits.")
        id = get_userid_via_input()

    return id


def get_pin_via_input():
    pin = getpass.getpass(prompt="Please enter your PIN: 🔑", stream=None)

    try:
        pin = int(pin)
    except:
        print("❌ Format Error: Please enter digits.")
        pin = get_pin_via_input()

    if len(str(pin)) != 4:
        print("❌ Error: PIN should be four digits.")
        pin = get_pin_via_input()
    
    return pin


def get_user_by_id(id):
    for user in users.user_list:
        if user['USERID'] == id:
            return user
    return None


def is_pin_matched(pin, user):
    if user['PIN'] == pin:
        return True
    return False


def login_user():
    id_attempsts = 0
    pin_attempts = 0
    user = None
    userid = None
    pin_is_matched = False

    while user is None:
        if id_attempsts >= 1:
            print("❌ Cannot find the user. Wrong USERID?")

        userid = get_userid_via_input()
        user = get_user_by_id(userid)

        id_attempsts += 1

    print("⭕️ USERID: ", userid)

    while not pin_is_matched:
        if pin_attempts >= 1:
            print("❌ Wrong PIN.")

        if pin_attempts >= 3:
            print("❌ You have attempted to login too many times. Please try again later.")
            return None

        pin = get_pin_via_input()
        pin_is_matched = is_pin_matched(pin, user)

        pin_attempts += 1

    return user
