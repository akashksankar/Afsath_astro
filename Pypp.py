data={
    '000001':{'Name':'Sam','Pin':1122,'Acc_amount':50600},
    '000002':{'Name':'Alex','Pin':1044,'Acc_amount':15000},
    '000003':{'Name':'Max','Pin':1023,'Acc_amount':25000},
    '000004':{'Name':'Joe','Pin':1212,'Acc_amount':4500},
    '000005':{'Name':'Anny','Pin':1412,'Acc_amount':1500000}
}

atm = 100000

while True:
    number = input("Enter your Account Number: ")

    if number in data:
        pin = int(input("Enter your PIN: "))

        if data[number]['Pin'] == pin:
            print("Login successful ✅")

            # -------- MENU LOOP --------
            while True:
                print("\n1. Balance Check")
                print("2. Withdrawal")
                print("3. Exit")

                choice = input("Enter your choice: ")

                if choice == '1':
                    print("Your balance is:", data[number]['Acc_amount'])

                elif choice == '2':
                    amt = int(input("Enter amount to withdraw: "))

                    if amt <= data[number]['Acc_amount'] and amt <= atm:
                        data[number]['Acc_amount'] -= amt
                        atm -= amt
                        print("Please collect your cash 💸")
                        print("Remaining balance:", data[number]['Acc_amount'])
                    else:
                        print("Insufficient balance or ATM cash ❌")

                elif choice == '3':
                    print("Thank you for using ATM 🙏")
                    break

                else:
                    print("Invalid choice ❌")

        else:
            print("Wrong PIN ❌")

    else:
        print("Account not found ❌")
