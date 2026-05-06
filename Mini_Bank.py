import json

FILE_NAME = "bank.json"

print("WELCOME 👋")


def load_bank():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except:
        return []


def save_bank():
    with open(FILE_NAME, "w") as file:
        json.dump(Bank, file)


Bank = load_bank()


def Creat_Account():

    AccountName = input("Enter Account Name: ").strip().lower()

    for acc in Bank:
        if acc["Name"] == AccountName:
            print("Account already exists ❌")
            return

    Account = {"Name": AccountName, "Balance": 0}
    Bank.append(Account)
    save_bank()

    print("Creat Account Is Done.")

    Quistion = input("Do You Want Deposit Money In Your account? (yes/no): ").strip().lower()

    if Quistion == "yes":
        try:
            amount = int(input("Enter Amount: "))
            if amount > 0:
                Account["Balance"] += amount
                save_bank()
                print("Deposit Done ✔")
            else:
                print("Wrong Value ❌")
        except:
            print("Invalid Entry ❌")


def Deposit():

    AccountName = input("Enter The Account Name: ").strip().lower()

    for account in Bank:
        if account["Name"] == AccountName:
            try:
                Amount = int(input("Enter The Deposit Amount: "))

                if Amount > 0:
                    account["Balance"] += Amount
                    save_bank()
                    print(f"Operation Is Done \nBalance = {account['Balance']} $")
                else:
                    print("Wrong Amount ❌")
            except:
                print("Invalid Entry ❌")
            return

    print("Account Is Not Found ❌")


def Withdraw():

    AccountName = input("Enter Account Name: ").strip().lower()

    for account in Bank:
        if account["Name"] == AccountName:
            try:
                Amount = int(input("Enter The Withdraw Amount: "))

                if 0 < Amount <= account["Balance"]:
                    account["Balance"] -= Amount
                    save_bank()
                    print(f"The Withdraw Operation Is Done, Balance = {account['Balance']}")
                else:
                    print("Wrong Entry ❌")
            except:
                print("Invalid Entry ❌")
            return

    print("Account Is Not Found ❌")


def Show_Your_Account():

    AccountName = input("Enter The Account Name: ").strip().lower()

    for account in Bank:
        if account["Name"] == AccountName:
            print(f"ACC: {account['Name']} | Balance = {account['Balance']} $")
            return

    print("Account Is Not Found ❌")


def Transfer():

    sender = input("Enter Sender Account: ").strip().lower()
    receiver = input("Enter Receiver Account: ").strip().lower()

    sender_acc = None
    receiver_acc = None

    for account in Bank:
        if account["Name"] == sender:
            sender_acc = account
        if account["Name"] == receiver:
            receiver_acc = account

    if not sender_acc or not receiver_acc:
        print("Account Not Found ❌")
        return

    try:
        Amount = int(input("Enter Amount To Transfer: "))

        if 0 < Amount <= sender_acc["Balance"]:
            sender_acc["Balance"] -= Amount
            receiver_acc["Balance"] += Amount
            save_bank()

            print("Transfer Done ✔")
            print(f"{sender} Balance = {sender_acc['Balance']}")
            print(f"{receiver} Balance = {receiver_acc['Balance']}")
        else:
            print("Wrong Amount ❌")

    except:
        print("Invalid Entry ❌")


while True:

    print("=" * 40)
    print("1- Creat Account")
    print("2- Deposit")
    print("3- Withdraw")
    print("4- Show Balance")
    print("5- Transfer Money")
    print("6- Exit")
    print("=" * 40)

    try:
        Choice = int(input("Enter Number Of Choice: "))

        if Choice == 1:
            Creat_Account()
        elif Choice == 2:
            Deposit()
        elif Choice == 3:
            Withdraw()
        elif Choice == 4:
            Show_Your_Account()
        elif Choice == 5:
            Transfer()
        elif Choice == 6:
            print("Bye 👋")
            break
        else:
            print("Wrong Choice ❌")

    except:
        print("Invalid Entry ❌")