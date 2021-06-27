import os

total_withdrawal = 0

def display_withdrawal_option_title():
    os.system('cls' if os.name == 'nt' else 'clear')

    print()
    print('Selected: 2. Withdrawal')
    print()
    print('____Option_____')
    print('1. ¢20')
    print('2. ¢40')
    print('3. ¢60')
    print('4. ¢100')
    print('5. Custom')
    print('6. Exit')
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


def get_custom_withdraw_amount_via_input():
    amount = input('Please enter amount: ')

    try:
        amount = float(amount)
    except:
        print('❌ Please enter digits.')
        amount = get_custom_withdraw_amount_via_input()

    if amount < 5 or amount > 200:
        print('❌ Amount Out of Range: Minimum ¢5 and maximum ¢200 accepted.')
        amount = get_custom_withdraw_amount_via_input()

    if amount % 5 != 0:
        print('❌ Only amount in multiple of 5 can be withdrawn.')
        amount = get_custom_withdraw_amount_via_input()

    return amount


def is_withdrawable(amount, user):
    if total_withdrawal + amount > 500:
        print()
        print('❌ Your requested amount exceeds the limit of withdrawals in a session.')
        return False

    elif user['OVERDRAFT'] == True:
        return True

    elif user['BALANCE'] >= amount:
        return True

    return False


def calculate_balance(amount, user):
    user['BALANCE'] = user['BALANCE'] - amount
    return user['BALANCE']


def withdraw_withdrawable_amount(user):
    global total_withdrawal
    number = get_number_via_input()

    amount = None
    withdrawable = False

    if number == 1:
        amount = 20

    elif number == 2:
        amount = 40

    elif number == 3:
        amount = 60
        

    elif number == 4:
        amount = 100

    elif number == 5:
        amount = get_custom_withdraw_amount_via_input()

    elif number == 6:
        return

    if amount is not None:
        withdrawable = is_withdrawable(amount, user)

        if withdrawable:
            os.system('cls' if os.name == 'nt' else 'clear')

            balance = calculate_balance(amount, user)
            total_withdrawal += amount
            print()
            print(f"You have withdrawn {amount} (¢)")
            print()
            print(f"Balance: {balance} (¢)")
            print()

        else:
            print()
            print('❌ The amount you have entered is not withdrawable. Please try with different amount.')
            print()
            withdraw_withdrawable_amount(user)


def main(user):
    display_withdrawal_option_title()

    withdraw_withdrawable_amount(user)