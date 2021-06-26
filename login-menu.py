from data.users import user_list

def show_login_menu_title():
    print()
    print("ATM Training App Login Page")
    print()


def get_userid_input():
    id = input("Please enter your USERID: ")

    try:
        id = int(id)
    except:
        print("❌ Format Error: Please enter digits.")
        id = get_userid_input()

    return id


def get_pin_input():
    pin = input("Please enter your PIN: ")

    try:
        pin = int(pin)
    except:
        print("❌ Format Error: Please enter digits.")
        pin = get_pin_input()

    if len(str(pin)) != 4:
        print("❌ Error: PIN should be four digits.")
        pin = get_pin_input()
    
    return pin


def get_user_by_id(id, users):
    for user in users:
        if user['USERID'] == id:
            return user
    return None


def is_pin_matched(pin, user):
    if user['PIN'] == pin:
        return True
    return False


def try_login():
    id_attempsts = 0
    pin_attempts = 0
    user = None
    userid = None
    pin_is_matched = False

    while user is None:
        if id_attempsts >= 1:
            print("❌ Cannot find the user. Wrong USERID?")

        userid = get_userid_input()
        user = get_user_by_id(userid, user_list)

        id_attempsts += 1

    print("⭕️ USERID: ", userid)

    while not pin_is_matched:
        if pin_attempts >= 1:
            print("❌ Wrong PIN.")

        if pin_attempts >= 3:
            print("❌ Too many times")
            return False

        pin = get_pin_input()
        pin_is_matched = is_pin_matched(pin, user)

        pin_attempts += 1

    return True


def main():
    show_login_menu_title()
    login_successful = try_login()

    if login_successful:
        print("welcome!")
    else:
        print("Sorry, bye bye")
    

if __name__ == "__main__":
    main()
