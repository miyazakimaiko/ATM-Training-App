## ATM Training App Overview

The application is presumed to be used for a training purpose only: used by their training team to guide new customers and staff through the process of accessing an ATM system. This page describes the objectives and goal of the system and models the functional requirements with use cases, structure chart and data flow diagram. This is intended to direct the design and implementation of the system using the procedural programming paradigm.

## Functional Objectives

### Log In
- The system shall allow the customer to log in using their USERID and current PIN.
- The system shall disable the login functionality after three attempts with the same USERID and enable the login functionality again if the app is restarted.

### Change PIN
- The system shall allow the customer to change their PIN after logging in.

![change pin DFD](./images/Change PIN DFD.jpg)

### Withdraw money from their account
- The system shall allow the customer to withdraw money up to ¢500, and the limit of withdrawal shall be reset as soon as the customer logs out.
- The system shall allow the customer to withdraw money from the minimum of ¢5 to the maximum of ¢200 at once.
- The system shall only allow withdrawals in multiples of ¢5.
- The system shall allow the customer to select predefined values: 20, 40, 60, and 100 when withdrawing. It shall also allow the customer to enter a custom amount which must be in multiples of ¢5.

### Lodge money into their account
- The system shall allow the customer to lodge money into their account
- The system shall allow the customer to lodge money from the minimum of ¢5 to the maximum of ¢2,000 at once.
- The system shall only allow lodgements in multiples of ¢5.
- The system shall allow the customer to lodge money up to ¢5,000, and the limit of the lodgement shall be reset as soon as the customer logs out.

### View statement
- The system shall allow the customer to view their USERID
- The system shall allow the customer to view their current balance
- The system shall allow the customer to view whether or not they are registered for an overdraft facility

### View their transaction history
- The system shall allow the customer to view their last 10 transactions ( PIN change/Withdrawal/Lodgement )
- The system shall display…
    - Date of Transaction ( yyyy-mm-dd format )
    - Transaction Type (Withdrawal, Lodgement, or Pin Change)
    - Amount (¢) ( if applicable )
    - Balance (¢)

### Log out
- The system shall reset total amount of withdrawal that has made in a session.
- The system shall reset total amount of lodgement that has made in a session.
- The system shall store the updated user’s data into a list of users.
