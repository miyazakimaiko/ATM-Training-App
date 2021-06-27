import os
import csv

user_list = []

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
users_csv = os.path.join(THIS_FOLDER, 'users.csv')

with open(users_csv, newline='\n') as csv_file:

    # Extract header individually
    # It contains: USERID, PIN, BALANCE, OVERDRAFT
    header = csv_file.readline().rstrip('\r\n')
    keys = header.split(',')

    # Read rest of lines
    for row in csv_file.read().splitlines():
        user = {}
        values = row.split(',')

        for index, value in enumerate(values):
            # values[0] is USERID (integer)
            # values[1] is PIN (integer)
            # values[2] is BALANCE (float)
            # values[3] is OVERDRAFT (Yes/No)
            if index in [0, 1]:
                value = int(value)

            elif index == 2:
                value = float(value)

            elif index == 3:
                if value == "Yes" or "True":
                    value = True
                elif value == "No" or "False":
                    value = False

            user[keys[index]] = value

        user_list.append(user)

    csv_file.close()


def overwrite_users_csv():
    if os.path.isfile(users_csv):
        os.remove(users_csv)
    else:    ## Show an error ##
        print("Error: %s file not found" % users_csv)

    with open(users_csv, 'w+', newline='\n') as csv_file:
        line = 0
        writer = csv.writer(csv_file)
        
        for user in user_list:
            if line == 0:
                header = list(user.keys())
                writer.writerow(header)

            data = list(user.values())
            writer.writerow(data)

            line += 1