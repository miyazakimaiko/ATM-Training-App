import os
from datetime import datetime

transaction_list = []

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
transactions_csv = os.path.join(THIS_FOLDER, 'transactions.csv')

with open(transactions_csv, newline='\n') as csv_file:

    # Extract header individually
    # It contains: DATE,USERID,TRANSACTION,AMOUNT,BALANCE_BEFORE,BALANCE_AFTER
    header = csv_file.readline().rstrip('\n')
    keys = header.split(',')

    # Read rest of lines
    for row in csv_file.read().splitlines():
        user = {}
        values = row.split(',')

        for index, value in enumerate(values):

            # values[0] is DATE (string inside "")
            # values[1] is USERID (integer)
            # values[2] is TRANSACTION (string inside "")
            # values[3] is AMOUNT (float) (Could be empty!)
            # values[4] is BALANCE_BEFORE (float)
            # values[5] is BALANCE_AFTER (float)
            if index == 0:
                value = datetime.strptime(value, '"%Y-%m-%d"').date()
            elif index == 1:
                value = int(value)
            elif index == 2:
                value = value.replace('"', '')
            elif index in [3, 4, 5]:
                try:
                    value = float(value)
                except:
                    value = None        

            user[keys[index]] = value

        transaction_list.append(user)

    csv_file.close()