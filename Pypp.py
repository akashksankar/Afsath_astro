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
        pin = int(input("Enter your pin number: "))

        if data[number]['Pin'] == pin:
            print("Login successful ✅")
        else:
            print("Wrong PIN ❌")
    else:
        print("Account not found ❌")
