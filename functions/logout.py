import os
from data import users

def main():
    os.system('cls' if os.name == 'nt' else 'clear')

    users.overwrite_users_csv()

    print()
    print('Thank you. Logged out successfully.')
    print()
