user_details = []
user_finance = []


def banking_user_login():
    incorrect = True
    while incorrect:
        incorrect = False

        global username_log
        username_log = input("Enter your username: ")
        if username_log in user_details:
            print("You have logged in successfully")
            menu = True
            while menu:
                user_choice = input("Enter: \n 1. To check balance\n 2. To deposit money\n "
                                    "3. To withdraw money\n Any other key to exit the menu: ")
                if user_choice == "1":
                    bank_balance()
                elif user_choice == "2":
                    bank_user_fin()
                elif user_choice == "3":
                    bank_withdraw()
                else:
                    incorrect = False
                    menu = False
        elif username_log not in user_details:
            print("Username is not found")
            incorrect = True


def bank_user_reg():
    username_reg = input("Enter a username for your account: ")

    if username_reg in user_details:
        print("Username already taken")

    else:
        user_details.insert(0, username_reg)
        user_finance.insert(0, 0)
        print("Your username has been created")


def bank_user_fin():
    cash = float(input("Enter the deposit amount: "))
    for i in range(len(user_details)):
        name = user_details[i]
        if name == username_log:
            user_finance[i] += cash
            print("Your new bank balance now is:", user_finance[i])
            nope = False


def bank_balance():
    for i in range(len(user_details)):
        user_bal = user_details[i]
        if user_bal == username_log:
            print("Your bank balance is:", user_finance[i])


def bank_withdraw():
    for i in range(len(user_details)):
        user_wit = user_details[i]
        if user_wit == username_log:
            if user_finance[i] > 0:
                withdraw = float(input("Enter your withdraw amount: "))
                if withdraw <= user_finance[i]:
                    left_amt = user_finance[i] - withdraw
                    print("Your current is now:", left_amt)
                else:
                    print("Withdrawal cannot exceed balance")
            else:
                print("You cannot withdraw anything, you BROKE!")


stay = True

print("Welcome To BankSA")
while stay:
    stay = False
    logging = input("Enter:\n1. To login\n2. To create a new account\n3. To exit \n")

    if logging == "1":
        banking_user_login()
        stay = True

    elif logging == "2":
        bank_user_reg()
        stay = True

    elif logging == "3":
        print("Thank you for using BankSA")
        stay = False

    else:
        print("Incorrect input")
        stay = True
