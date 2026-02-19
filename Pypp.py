# ATM Database
data = {
    '000001': {'name': 'Ashik', 'pin': 2211, 'balance': 50000},
    '000002': {'name': 'Manu',  'pin': 6611, 'balance': 15000},
    '000003': {'name': 'Ram',   'pin': 1002, 'balance': 25000},
    '000004': {'name': 'Hari',  'pin': 0023, 'balance': 4500},
    '000005': {'name': 'Rahul', 'pin': 2551, 'balance': 150000}
}

# ---------------- FUNCTIONS ----------------

def login():
    acc = input("Enter account number: ")
    pin = int(input("Enter PIN: "))

    if acc in data and data[acc]['pin'] == pin:
        print(f"\nWelcome {data[acc]['name']} ✅")
        return acc
    else:
        print("Invalid account or PIN ❌")
        return None


def check_balance(acc):
    print("Current Balance:", data[acc]['balance'])


def withdraw(acc):
    amt = int(input("Enter amount to withdraw: "))

    if amt <= data[acc]['balance']:
        data[acc]['balance'] -= amt
        print("Withdrawal successful 💸")
        print("Remaining balance:", data[acc]['balance'])
    else:
        print("Insufficient balance ❌")


def deposit(acc):
    amt = int(input("Enter amount to deposit: "))
    data[acc]['balance'] += amt
    print("Deposit successful ✅")
    print("Updated balance:", data[acc]['balance'])


# ---------------- MAIN PROGRAM ----------------

def atm():
    acc = login()
    if not acc:
        return

    while True:
        print("\n----- ATM MENU -----")
        print("1. Check Balance")
        print("2. Withdraw")
        print("3. Deposit")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            check_balance(acc)
        elif choice == '2':
            withdraw(acc)
        elif choice == '3':
            deposit(acc)
        elif choice == '4':
            print("Thank you for using ATM 🙏")
            break
        else:
            print("Invalid choice")


# Run ATM
atm()
