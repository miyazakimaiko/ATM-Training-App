import os
from data.transactions import transaction_list


def display_view_statement_option_title():
    os.system('cls' if os.name == 'nt' else 'clear')

    print()
    print('Your Account Statement')
    print()


def display_account_statement(user):
    print(f"USERID: {user['USERID']}")
    print(f"Current Balance: {user['BALANCE']}")

    overdraft_statement_message = 'Not registered for overdraft facility'
    if user['OVERDRAFT'] == True:
        overdraft_statement_message = 'Registered for overdraft facility'

    print(overdraft_statement_message)
    print()


def display_transaction_history(user, transaction_list):
    my_transactions = []

    for transaction in transaction_list:
        if transaction['USERID'] == user['USERID']:
            my_transactions.append(transaction)

        if len(my_transactions) >= 10:
            break

    print('Transactions')
    print()
    print("DATE".ljust(22) + "TRANSACTION".ljust(22) + "AMOUNT".ljust(22) + "BALANCE")
    print("---------------------------------------------------------------------------")
    
    for tr in my_transactions:
        print(f"{str(tr['DATE']).ljust(10)}\
            {tr['TRANSACTION'].ljust(10)}\
            {str(tr['AMOUNT']).ljust(10)}\
            {str(tr['BALANCE_AFTER'])}")

    print()


def main(user):
    display_view_statement_option_title()

    display_account_statement(user)

    display_transaction_history(user, transaction_list)
