import os

total_lodgement = 0
MAX_LODGEMENT_PER_SESSION = 5000


def display_lodgement_option_title():
    os.system('cls' if os.name == 'nt' else 'clear')

    print()
    print('Selected: 3. Lodgement')
    print()
    print('____Option_____')
    print('1. Custom')
    print('2. Exit')
    print()


def get_number_via_input():
    number = input('Please enter a number 1 or 2: ')

    try:
        number = int(number)
    except:
        print('❌ Format Error: it is not a digit.')
        number = get_number_via_input()

    if number not in [1, 2]:
        print('❌ Entered Digit Out of Range Error')
        number = get_number_via_input()

    return number


def get_custom_lodgement_amount_via_input():
    amount = input('Please enter amount: ')

    try:
        amount = float(amount)
    except:
        print('❌ Please enter digits.')
        amount = get_custom_lodgement_amount_via_input()

    if amount < 5 or amount > 2000:
        print('❌ Amount Out of Range: Minimum ¢5 and maximum ¢2,000 accepted.')
        amount = get_custom_lodgement_amount_via_input()

    if amount % 5 != 0:
        print('❌ Only amount in multiple of 5 can be lodged.')
        amount = get_custom_lodgement_amount_via_input()

    return amount


def is_lodgeable(amount):
    if total_lodgement + amount > MAX_LODGEMENT_PER_SESSION:
        print()
        print('❌ Your requested amount exceeds the limit of lodgements in a session.')
        return False

    return True


def calculate_balance(amount, user):
    user['BALANCE'] = user['BALANCE'] + amount
    return user['BALANCE']


def lodge_lodgeable_amount(user):
    global total_lodgement
    number = get_number_via_input()

    amount = None
    lodgeable = False

    if number == 1:
        amount = get_custom_lodgement_amount_via_input()

    elif number == 2:
        return

    if amount is not None:
        lodgeable = is_lodgeable(amount)

        if lodgeable:
            os.system('cls' if os.name == 'nt' else 'clear')

            balance = calculate_balance(amount, user)
            total_lodgement += amount
            print()
            print(f"You have lodged {amount} (¢)")
            print()
            print(f"Balance: {balance} (¢)")
            print()

        else:
            print()
            print('❌ The amount you have entered is not lodgeable. Please try with different amount.')
            print()
            lodge_lodgeable_amount(user)


def main(user):
    display_lodgement_option_title()

    lodge_lodgeable_amount(user)