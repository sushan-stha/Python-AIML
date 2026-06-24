# atm vault simulator:

balance = 10000

while True:
    print("\n----Welcome to Python Atm----")
    print("1.Check Balace:")
    print("2.Deposit Funds:")
    print("3.WithDraw Funds:")
    print("4.Exit:")

    user_choice = int(input("Enter you choice(1-4):"))

    match user_choice:
        case 1:
            print(f"Current balance:{balance}")
        case 2:
            deposit = float(input("Enter the amount to deposit: "))
            balance += deposit
            print(f"New Balance:{balance}")
        case 3:
            withdraw = float(input("Enter the amount to withdraw:"))
            if(withdraw > balance):
                print("Insufficient Balance!!")
            else:
                balance -= withdraw
                print(f"Remaining Balance:{balance}")
        case 4:
            print("Thankyou for choosing us!")
        
            break

        case _:
            print("Invalid Choice!!")
